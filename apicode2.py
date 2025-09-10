# apicode2.py
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil, os
from typing import List

from new9 import PDFExtractor   # <-- use your new9.py extractor
from filecode2 import convert_docx_to_pdf

app = FastAPI(title="Document Extraction Service v2")

# Allow frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract_files(
    files: List[UploadFile] = File(...),
    engines: str = Form("tesseract"),     # comma-separated: tesseract,easyocr,paddleocr
    tools: str = Form("pdfplumber"),      # comma-separated: pdfplumber,pymupdf,pdfminer
    outputFormat: str = Form("txt"),      # txt/docx
    outputName: str = Form(None)          # optional custom name
):
    results = []
    for file in files:
        temp_filename = f"temp_{file.filename}"
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            # Convert DOCX to PDF if needed
            extracted_pdf_path = temp_filename
            if file.filename.lower().endswith(".docx"):
                extracted_pdf_path = f"{os.path.splitext(temp_filename)[0]}.pdf"
                convert_docx_to_pdf(temp_filename, extracted_pdf_path)
            elif not file.filename.lower().endswith(".pdf"):
                raise HTTPException(status_code=400, detail="Only PDF and DOCX supported.")

            # Run extraction
            extractor = PDFExtractor(
                extracted_pdf_path,
                engines=engines.split(","),
                tools=tools.split(",")
            )
            data = extractor.extract()

            # Build output file
            base_name = outputName if outputName else os.path.splitext(file.filename)[0]
            if outputFormat == "txt":
                result_file = f"{base_name}.txt"
                extractor.save_to_txt(data, result_file)
            elif outputFormat == "docx":
                result_file = f"{base_name}.docx"
                extractor.save_to_docx(data, result_file)
            else:
                raise HTTPException(status_code=400, detail="Invalid output format")

            results.append({
                "filename": file.filename,
                "output_file": result_file,
                "pages_extracted": len(data)
            })

        except Exception as e:
            results.append({"filename": file.filename, "error": str(e)})

        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            if extracted_pdf_path != temp_filename and os.path.exists(extracted_pdf_path):
                os.remove(extracted_pdf_path)

    return JSONResponse(content=results)

# Run with:
# python -m uvicorn apicode2:app --reload
# http://127.0.0.1:8000/webcode2.html

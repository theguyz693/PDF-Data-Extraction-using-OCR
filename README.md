🚀 Multi-OCR Document Extraction Service
This is a web application that provides a powerful and flexible way to extract text from PDF and DOCX documents. It leverages multiple Optical Character Recognition (OCR) engines and text extraction tools to provide accurate and reliable results.

The project is built as a client-server application with a modern, responsive web interface and a robust Python backend powered by FastAPI.

✨ Features
Multi-Engine OCR: Supports popular OCR engines including Tesseract, EasyOCR, and PaddleOCR.

Multiple Extraction Tools: Utilizes PDFPlumber, PyMuPDF, and PDFMiner for direct text extraction from documents.

Flexible Output: Extracted text can be saved in either plain text (.txt) or Microsoft Word (.docx) format.

Modern UI: A sleek, dark-themed web interface built with Tailwind CSS for a great user experience.

Cross-Platform: The Python backend can be run on any operating system, and the web interface is accessible from any modern browser.

📦 Getting Started
Prerequisites
To run the backend, you'll need Python 3.8+ installed. The required Python packages are listed in requirements.txt.

Installation
Clone the repository:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

Install the Python dependencies:

pip install -r requirements.txt

Note: Some OCR engines may require additional system-level installations (e.g., Tesseract).

Running the Application
The application consists of a backend server and a frontend web page.

Start the backend server:
Open your terminal and run the following command from the project's root directory:

uvicorn apicode2:app --reload

This will start the server on http://127.0.0.1:8000.

Open the frontend:
Open your index.html file in a web browser. It will automatically connect to the running backend server.

🛠️ Technologies Used
Frontend
HTML5: For the page structure.

Tailwind CSS: For styling and a responsive design.

JavaScript: For handling user interactions and communicating with the backend API.

Backend
Python: The core programming language.

FastAPI: A modern, high-performance web framework for building the API.

PyMuPDF (fitz): A fast library for handling PDF files.

pdfplumber: A library for extracting data from PDFs.

pytesseract: A Python wrapper for Google's Tesseract OCR.

easyocr: An easy-to-use OCR library.

paddleocr: Another powerful OCR library from PaddlePaddle.

python-docx: For creating .docx files.

reportlab: For handling PDF creation from DOCX.

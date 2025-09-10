# 🚀 Multi-OCR Document Extraction Service

This is a web application that provides a powerful and flexible way to extract text from PDF and DOCX documents. It leverages multiple Optical Character Recognition (OCR) engines and text extraction tools to provide accurate and reliable results.

The project is built as a client-server application with a modern, responsive web interface and a robust Python backend powered by **FastAPI**.

Note: This ⤵️ requires your project to run locally to give outputs, this is just a preview.

[Preview of project hosted on github](https://theguyz693.github.io/PDF-Data-Extraction-using-OCR/)

---

## ✨ Features
- 🔎 **Multi-Engine OCR**: Supports popular OCR engines including **Tesseract**, **EasyOCR**, and **PaddleOCR**.  
- 📑 **Multiple Extraction Tools**: Utilizes **PDFPlumber**, **PyMuPDF**, and **PDFMiner** for direct text extraction from documents.  
- 💾 **Flexible Output**: Extracted text can be saved in either plain text (`.txt`) or Microsoft Word (`.docx`) format.  
- 🎨 **Modern UI**: A sleek, dark-themed web interface built with **Tailwind CSS** for a great user experience.  
- 🌍 **Cross-Platform**: The Python backend can be run on any operating system, and the web interface is accessible from any modern browser.  

---

---
## 📦 Getting Started

### Prerequisites
- Python 3.8+ 
- Required Python packages (listed in `requirements.txt`)
- Some OCR engines may require additional system-level installations (e.g., Tesseract). 

### Installation
1.  **Clone the repository:**
    ```
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
    ⚠️ Note: Some OCR engines may require additional system-level installations (e.g., Tesseract).

---

## 🚀 Running the Application

The application consists of a backend server and a frontend web page.

### Start the backend server
Open your terminal and run the following command from the project’s root directory:
uvicorn apicode2:app --reload

This will start the server on:
👉 http://127.0.0.1:8000

### Open the frontend
Open your `index.html` file in a web browser. It will automatically connect to the running backend server.

---

## 🛠️ Technologies Used

### Frontend
- HTML5 – Page structure
- Tailwind CSS – Styling and responsive design
- JavaScript – Handles user interactions and communicates with the backend API

### Backend
- Python – Core programming language
- FastAPI – Modern, high-performance web framework for building the API
- PyMuPDF (`fitz`) – Fast library for handling PDF files
- `pdfplumber` – Extracting data from PDFs
- `pytesseract` – Python wrapper for Google’s Tesseract OCR
- `easyocr` – Easy-to-use OCR library
- `paddleocr` – Powerful OCR library from PaddlePaddle
- `python-docx` – For creating .docx files
- `reportlab` – For generating PDFs from DOCX




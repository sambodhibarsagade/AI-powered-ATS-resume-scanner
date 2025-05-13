# AI Resume Scanner

This project is a backend tool I built as part of my learning journey in AI and automation. It's an **ATS-style resume scanner** that can take resumes (PDF or DOCX format), extract important information like name,number, emai_id, links, qualifications, experience, and skills, and then export that data into an organized Excel file.

The idea came from observing how companies use software to scan through job applications — I wanted to recreate something similar using Python and machine learning techniques.

## What It Does

- Lets users upload resumes in **PDF or DOCX** format.
- Extracts useful data such as:
  - Full Name
  - Number
  - Email_id
  - Education/Qualifications
  - Work Experience
  - Skills (technical and soft)
  - Links
  - Outputs all the information into a clean, structured **Excel (.xlsx)** file.
## Image Presentation 
![image](https://github.com/user-attachments/assets/52aff47e-fee1-4505-a3a8-69e6e4b1de5e)


![image](https://github.com/user-attachments/assets/afc08649-ae01-46bd-945d-c500b39768c4)



![image](https://github.com/user-attachments/assets/e951944a-c836-4540-91d6-3f99a8325f9d)


## Technologies & Tools Used

- **Python**: Core logic
- **Flask**: For handling backend endpoints
- **PyPDF2 / python-docx**: To read PDF and Word files
- **Pandas**: For data manipulation and exporting to Excel
- **OpenPyXL**: To create styled Excel files
- **Regex (re module)**: For text parsing and pattern matching
- **scikit-learn (optional)**: Used in parts where pattern classification or future ML integration might be needed

## Folder Structure
```
 ats_resume_scanner/
 ├── app.py                # Main application file (Flask backend)
 ├── document_parsers/
 │   ├── pdf_processor.py  # Extracts text from PDFs
 │   └── docx_processor.py # Extracts text from DOCX files
 ├── ai_modules/
 │   └── resume_analyzer.py # NLP logic for extracting entities
 ├── templates/
 │   └── index.html        # Upload page
 ├── static/
 │   └── style.css         # CSS styles
 └── requirements.txt      # Required packages
```

## How to Run It Locally

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/AI-Resume-Scanner.git
cd AI-Resume-Scanner
```
2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the app:**
```bash
python app.py
```
Then use something like Postman or CURL to test the file upload and see the generated Excel output.

Note: If you're new to Flask or don't have Postman, I recommend checking a simple Flask file-upload tutorial. The app runs in the background, so there's no UI for now.

## Why I Made This
I wanted to create something practical that combined my interest in AI, automation, and real-world applications. While learning about how companies use Applicant Tracking Systems (ATS) to filter resumes, I realized most people never see how these systems work behind the scenes.

So I decided to build my own version — a tool that could extract useful information from resumes (like name, skills, and experience) and organize it in a clean, readable format like Excel.

This project helped me:

- Practice working with unstructured text data (PDFs, DOCX)
- Understand how data parsing and pattern recognition can be used in resume analysis
- Learn how to connect a frontend and backend in a real-world web application
- Simulate part of what happens in AI-driven recruitment systems

Ultimately, I built this project to sharpen my skills, explore how ATS systems work, and make something that could actually help users or companies handle resumes more efficiently.


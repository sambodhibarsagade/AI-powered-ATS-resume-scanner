from flask import Flask, request, render_template, send_file
import os
import pandas as pd
from document_parsers.pdf_processor import parse_pdf
from document_parsers.docx_processor import parse_docx
from ai_modules.resume_analyzer import ResumeParser

app = Flask(__name__)

# Set up upload directory
app.config['UPLOADS'] = 'temp_uploads'
os.makedirs(app.config['UPLOADS'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return "No file selected", 400

    file = request.files['resume']
    if file.filename == '':
        return "Empty file", 400

    # Save uploaded file temporarily
    save_path = os.path.join(app.config['UPLOADS'], file.filename)
    file.save(save_path)

    try:
        # Extract text from file
        if file.filename.lower().endswith('.pdf'):
            text = parse_pdf(save_path)
        elif file.filename.lower().endswith('.docx'):
            text = parse_docx(save_path)
        else:
            return "Unsupported format", 400

        # Analyze resume content
        analyzer = ResumeParser()
        results = analyzer.extract_data(text)

        # File path for storing all results
        all_data_path = 'all_resumes_data.xlsx'

        # Append new results to all_resumes_data.xlsx
        if os.path.exists(all_data_path):
            existing_df = pd.read_excel(all_data_path)
            updated_df = pd.concat([existing_df, pd.DataFrame([results])], ignore_index=True)
        else:
            updated_df = pd.DataFrame([results])
        updated_df.to_excel(all_data_path, index=False, engine='openpyxl')

        # Save individual result to analysis_results.xlsx
        result_path = 'analysis_results.xlsx'
        pd.DataFrame([results]).to_excel(result_path, index=False, engine='openpyxl')

        return send_file(result_path, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}", 500

    finally:
        if os.path.exists(save_path):
            os.remove(save_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

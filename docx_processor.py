from docx import Document

def parse_docx(filepath):
    try:
        doc = Document(filepath)
        paragraphs = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
        return "\n".join(paragraphs)
    except Exception as e:
        raise RuntimeError(f"DOCX parsing failed for {filepath}: {str(e)}")

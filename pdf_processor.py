import pdfplumber

def parse_pdf(filepath):
    full_text = []
    try:
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:  # Avoid appending None if a page has no text
                    full_text.append(text.strip())
                else:
                    print(f"[Warning] No extractable text on page {i+1}")
        return "\n".join(full_text).strip()
    except Exception as e:
        raise RuntimeError(f"PDF parsing failed for {filepath}: {str(e)}")

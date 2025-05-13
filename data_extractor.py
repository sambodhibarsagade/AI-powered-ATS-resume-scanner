import spacy
import re
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_data(text):
    print("========= RAW TEXT =========")
    print(text[:500])  # Limit output to avoid flooding
    print("============================")
    
    # Clean text
    text = re.sub(r'\s+', ' ', text).strip()
    doc = nlp(text)
    
    name = None

    # Rule 1: Named Entity Recognition
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    # Rule 2: First line fallback
    if not name:
        lines = text.split('\n')
        first_line = lines[0].strip() if lines else ""
        if 1 <= len(first_line.split()) <= 3:
            name = first_line

    # Rule 3: Regex-based fallback (supports both Title Case and UPPER CASE)
    if not name:
        match = re.search(r'^([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)', text)
        if match:
            name = match.group(1)
        else:
            # Match uppercase names like "JOHN DOE"
            match_upper = re.search(r'^([A-Z]{2,}(?:\s[A-Z]{2,})+)', text)
            if match_upper:
                name = match_upper.group(1)

    # Final fallback
    if not name:
        name = "Not Found"

    # Return DataFrame with just name for now
    return pd.DataFrame({
        "Name": [name]
        # You can add email, phone, skills etc. here
    })

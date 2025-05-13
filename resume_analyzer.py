import spacy
import re
from datetime import datetime

class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.skill_db = {
            'technical': [
                'Python', 'Machine Learning', 'SQL', 'Flask', 'Pandas', 'Java', 'DSA', 'FrontEnd',
                'PHP', 'AngularJs', 'Natural Language Processing', 'NumPy', 'Scikit-learn',
                'TensorFlow', 'Power BI', 'Tableau', 'Network security', 'Ethical hacking',
                'Docker', 'Jenkins', 'Kubernetes'
            ],
            'soft': [
                'Communication', 'Teamwork', 'Leadership', 'Communication Skills',
                'Verbal and written communication', 'Technical documentation', 'Problem-Solving',
                'Logical thinking', 'Analytical reasoning', 'Teamwork & Collaboration',
                'Adaptability', 'Open to new tools and technologies', 'Time Management',
                'Meeting deadlines', 'Prioritizing tasks', 'Critical Thinking', 'Leadership Skills',
                'Leading projects or teams', 'Creativity & Innovation', 'Emotional Intelligence',
                'Self-awareness', 'Empathy in teamwork', 'Decision-Making'
            ]
        }

    def extract_data(self, text):
        clean_text = re.sub(r'\s+', ' ', text)
        doc = self.nlp(clean_text)

        return {
            'name': self._get_name(doc, clean_text),
            'email': self._get_email(clean_text),
            'phone': self._get_phone(clean_text),
            'education': self._find_education(clean_text),
            'experience': self._find_experience(clean_text),
            'skills': self._find_skills(clean_text),
            'links': self._get_links(clean_text)
        }

    def _get_name(self, doc, text):
        linkedin_match = re.search(r'linkedin\.com/in/([\w-]+)', text)
        if linkedin_match:
            return linkedin_match.group(1).replace('-', ' ').title()

        lines = text.split('\n')[:5]
        header_text = " ".join(lines)

        for ent in doc.ents:
            if ent.label_ == "PERSON" and ent.text.lower() in header_text.lower():
                return ent.text

        name_regex = r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)"
        match = re.search(name_regex, header_text)
        return match.group(1) if match else "Not Found"

    def _get_email(self, text):
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        return match.group(0) if match else "Not Found"

    def _get_phone(self, text):
        phone_match = re.search(
            r'(\+?\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?\d{3,5}[\s-]?\d{4,6}', text)
        return phone_match.group(0) if phone_match else "Not Found"

    def _get_links(self, text):
        links = []
        linkedin = re.search(r'https?://(www\.)?linkedin\.com/in/[^\s,]+', text)
        github = re.search(r'https?://(www\.)?github\.com/[^\s,]+', text)

        if linkedin:
            links.append(f"LinkedIn: {linkedin.group(0)}")
        if github:
            links.append(f"GitHub: {github.group(0)}")

        return ", ".join(links) if links else "None Found"

    def _find_education(self, text):
        edu_keywords = r'\b(' \
                       r'B\.?S\.?|B\.?A\.?|M\.?S\.?|M\.?A\.?|Ph\.?D|Bachelor|Master|' \
                       r'BCA|MCA|B\.?Tech|M\.?Tech|' \
                       r'SSC|S\.?S\.?C\.?|HSC|H\.?S\.?C\.?|' \
                       r'Diploma|Polytechnic|I\.?T\.?I\.?|' \
                       r'PG\s?Diploma|Post\s?Graduate\s?Diploma' \
                       r')\b'
        found = re.findall(edu_keywords, text, re.I)
        return ", ".join(sorted(set(found))) if found else "Not Found"

    def _find_experience(self, text):
        match = re.search(r'(\d+)\+?\s*(years?|yrs?)\b', text, re.I)
        return match.group(0) if match else "Fresher"

    def _find_skills(self, text):
        found = []
        for category in self.skill_db:
            found += [skill for skill in self.skill_db[category]
                      if re.search(rf'\b{re.escape(skill)}\b', text, re.I)]
        return ", ".join(sorted(set(found))) if found else "None Found"

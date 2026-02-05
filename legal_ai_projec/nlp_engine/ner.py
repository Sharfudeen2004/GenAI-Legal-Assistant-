import re

def extract_entities(text):
    return {
        "amounts": re.findall(r'₹\s?\d+', text),
        "dates": re.findall(r'\d{2}/\d{2}/\d{4}', text),
    }

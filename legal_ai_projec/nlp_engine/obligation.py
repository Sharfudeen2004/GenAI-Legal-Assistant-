def detect_obligation(text):
    t = text.lower()
    if "shall" in t:
        return "Obligation"
    if "may" in t:
        return "Right"
    if "shall not" in t:
        return "Prohibition"
    return "Neutral"

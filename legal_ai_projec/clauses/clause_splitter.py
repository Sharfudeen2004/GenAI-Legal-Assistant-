import re

def split_clauses(text):
    # split by ANY number + dot (works even with spaces)
    parts = re.split(r'\s+\d+\.\s+', text)

    clauses = []

    for p in parts:
        p = p.strip()
        if len(p) > 40:
            clauses.append(p)

    return clauses

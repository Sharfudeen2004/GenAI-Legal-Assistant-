def classify_contract(text):
    t = text.lower()
    if "employee" in t:
        return "Employment Contract"
    if "lease" in t:
        return "Lease Agreement"
    if "vendor" in t or "supplier" in t:
        return "Vendor Contract"
    return "General Service Contract"

def detect_risk(clause):
    risks = []
    t = clause.lower()

    if "indemnify" in t:
        risks.append(("Indemnity Clause", "HIGH"))

    if "terminate" in t and "any time" in t:
        risks.append(("Unilateral Termination", "HIGH"))

    if "confidential" in t:
        risks.append(("Confidentiality Obligation", "LOW"))

    if "governed by the laws" in t:
        risks.append(("Jurisdiction Clause", "LOW"))

    return risks

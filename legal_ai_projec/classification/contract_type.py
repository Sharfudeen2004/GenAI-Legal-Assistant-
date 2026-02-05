def classify_contract(text):

    t = text.lower()

    # Employment
    if any(word in t for word in [
        "employee", "employer", "employment", "salary",
        "probation", "termination of employment"
    ]):
        return "Employment Agreement"

    # Lease
    if any(word in t for word in [
        "rent", "lease", "tenant", "landlord", "premises"
    ]):
        return "Lease / Rental Agreement"

    # Vendor
    if any(word in t for word in [
        "service provider", "services", "invoice", "payment terms"
    ]):
        return "Service / Vendor Contract"

    # Partnership
    if any(word in t for word in [
        "partner", "partnership"
    ]):
        return "Partnership Agreement"

    return "General Contract"

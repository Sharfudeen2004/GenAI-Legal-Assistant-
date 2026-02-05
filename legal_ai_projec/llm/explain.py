import openai

def explain_clause(clause):

    prompt = f"""
    Explain this legal clause in simple business English.
    Keep it short and easy.

    Clause:
    {clause}
    """

    # Replace with GPT-4 / Claude call
    # For now simple fallback:
    return "This clause describes the responsibilities and legal conditions in simple terms."

def calculate_score(all_risks):
    score = 0

    for r, level in all_risks:
        if level == "HIGH":
            score += 3
        elif level == "MEDIUM":
            score += 2
        elif level == "LOW":
            score += 1

    return min(score, 10)

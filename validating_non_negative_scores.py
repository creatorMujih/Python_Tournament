def validate_scores(score1, score2):
    try:
        score1 = int(score1)
        score2 = int(score2)

        if score1 < 0 or score2 < 0:
            return "Error: Scores cannot be negative."

        return f"Valid scores: {score1} and {score2}"

    except ValueError:
        return "Error: Both scores must be integers."


print(validate_scores(3, 2))
print(validate_scores(0, 5))
print(validate_scores(-1, 4))
print(validate_scores("abc", 3))
print(validate_scores(2.5, 4))

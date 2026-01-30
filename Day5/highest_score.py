student_scores = [12, 13, 16, 8, 20]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score is: {highest_score}")
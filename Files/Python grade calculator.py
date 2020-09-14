def grading(grade_1, grade_2): 
    if grade_1 < 5.5:
        W = max(grade_1, grade_2) 
        if W <= 5.5:
            return W
        else:
            return 0.5 * (W - 6) + 6 
    elif grade_2 <= 5.5:
        return (grade_1 - 6) / 2 + 6
    else:
        return (grade_1 - 6) / 2 + 6 + 1/5 * grade_2

print(grading(4,9))
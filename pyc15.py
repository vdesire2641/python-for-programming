# write a nested selection using ifelse that sets the value of a variable
# gradepoint to 4 if a variable named score is greater than 90
# 3 if score is between 80 and 89, 2 if score is between 70 and 79
# 1, if score is between 60 and 69, and 0 otherwise
# 2.30
score = 77
if score > 90:
    gradepoint = 4
else:
        if 80 < score < 89:
            gradepoint = 3
        else:
                if 70 < score < 79:
                    gradepoint = 2
                else:
                        if 60 < score < 69:
                            gradepoint = 1
                        else:
                            gradepoint = 0

print(gradepoint)
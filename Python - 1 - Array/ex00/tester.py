from give_bmi import give_bmi, apply_limit

height = []
weight = []

bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

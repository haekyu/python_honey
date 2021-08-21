korean = int(input("Enter your Korean score."))
english = int(input("Enter your English score."))
avg = (korean + english) / 2
if avg >= 90 :
    grade = "A"
elif avg >=70 :
    grade = "B"
else:
    grade = "C"
print("Your grade is", grade)
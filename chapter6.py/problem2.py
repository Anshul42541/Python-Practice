#taking input marks of 3 subjects 
student = {"Maths": "", "Science": "", "English": ""}
for item in student:
    student[item] = int(input(f"Enter marks of {item} :"))

percentage = (student["Maths"]+ student["Science"]+ student["English"])/3

if percentage >40 and student["Maths"] > 33 and student["Science"] >33 and student["English"] > 33:
    print("Congratulations you have passed the exam")
else:
    print("Sorry you have failed the exam") 

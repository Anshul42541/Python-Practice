marks = []
for i in range(6):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)
marks.sort()   
print(f"The Marks in sorted order are: {marks}") 
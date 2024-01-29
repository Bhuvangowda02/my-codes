students=input('enter the heights:').split()
for i in range(0,len(students)):
  students[i]=int(students[i])

total_height=0
for height in students:
  total_height+=height

total_student=0
for student in students:
  total_student+=1


average=(total_height/total_student)
print(average)
  
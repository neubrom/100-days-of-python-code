total_height=0
student_number=0

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total_height += int(student_heights[n])
  student_number +=1

#print(student_number)
#print(total_height)

average = round((total_height/student_number), 0)
print(int(average))


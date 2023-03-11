# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_height = 0
number_count = 0
#Write your code below this row 👇
for height in student_heights:
    total_height += height
    number_count = number_count +1
#print (total_height)
#print (f"There are a total of {number_count} heights in student_height")
average_height = round (total_height / number_count)
print (average_height)



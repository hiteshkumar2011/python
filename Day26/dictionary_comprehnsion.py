## new_dict = {new_key:new_value  for item in list}

#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
name = ["Hitesh", "Trisha", "Tom", "Ryan", "Mike", "Messi", "HKT", "Nivaan", "Nivan"]

student_score = {student:random.randint(1,100) for student in name}
#print (student_score)

passed_students = {student:score for (student,score) in student_score.items() if score >= 60}

print(passed_students)
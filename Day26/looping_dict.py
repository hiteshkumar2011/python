## Looping through dictionary
student_dict = {
        "student": ["Hitesh", "Nivaan", "Trisha", "HKT", "Mike"],
        "score": [69,79,80,90,95]
}
# for (key,value) in student_dict.items():
#     print(key, value)

import  pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through Data Frame
# for (key,value) in student_data_frame.items():
#     print(value)

# Loop through rows of Data Frame
for (index,row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Hitesh":
        print(row.score)


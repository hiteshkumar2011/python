## To Find the unique value from file 1 and file2 and print as result

with open("file1.txt") as file1:
    num_data1 = file1.readlines()

with open("file2.txt") as file2:
    num_data2 = file2.readlines()

result = [int(num) for num in num_data1 if num in num_data2]
print(result)
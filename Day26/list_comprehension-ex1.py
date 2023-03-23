numbers = [1,2,3]   ## to increase list by 1 up to 10
# for i in range(4,11):
#     numbers.append(i)
# print(numbers)

## List Comprehensions

#new_list = [new_item for item in list]
# new_list = [n+1 for n in numbers]
# print(new_list)
# name = "Hitesh"
# str_list = [letters for letters in name]
# print(str_list)

## Range (1,5) new list should be [2,4,6,8]
#sqr_list = [num * 2 for num in range(1,5)]
#print(sqr_list)

## Conditional List Comprehensions
#new_list = [new_item for item in list if test]

name = ["Hitesh", "Trisha", "Tom", "Ryan", "Mike", "Messi", "HKT", "Nivaan", "Nivan"]

new_name_list = [names for names in name if len(names) < 5]
#print(new_name_list)

upper_name_list = [capital.upper() for capital in name if len(capital) < 5]
print(upper_name_list)







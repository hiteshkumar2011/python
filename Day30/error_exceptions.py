# #FileNotFound Error
#
# try:
#     file = open("a_file.txt","r")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#      file.close()
#      print("File was closed")
#      raise TypeError("This is the Error I made up")

height = float(input("Enter Height "))
weight = int(input("Enter Weight "))

if height > 3:
    raise  ValueError("Human Height should not be over 3m. ")

bmi = weight / (height ** 2)
print(bmi)


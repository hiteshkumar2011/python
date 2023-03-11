first_name=  input ("Enter your first name  ")
last_name = input("Enter your last name  ")

def name_format(f_name,l_name):
    title_fname = f_name.title()
    title_lname = l_name.title()
    return title_fname +" "+ title_lname

new_titlename=name_format(first_name,last_name)
print(new_titlename)

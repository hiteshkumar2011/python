## Use for documentation in the code  -- Docstring purpose 
'''
    Print statement is used for printing the output directly 
'''
first_name=  input ("Enter your first name  ")
last_name = input("Enter your last name  ")

#Already used functions with output 
length = len(first_name)

def name_format(f_name,l_name):
    """
    Take a first and last name and format it to return the title case version of the name
    """
    title_fname = f_name.title()
    title_lname = l_name.title()
    return title_fname +" "+ title_lname

new_titlename=name_format(first_name,last_name)
print(new_titlename)







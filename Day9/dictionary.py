## key: value   dict1 = {}
programming_dictionary = {
                          "bug":"It is an error in the program.",
                          "functon": "A piece of code we can call over again and again", "loop":"action of doing again, iteration"
                        }

## To retrieve the data from dictionary                         
#print(programming_dictionary["bug"])

# Edit an item in the dictionary 
programming_dictionary["loop"] = "There are two type of loop in python- while,for"
#print(programming_dictionary["loop"])

## To add data in the dictionary if that key does not exist 
programming_dictionary["variable"] = "To hold the data or any output"
#print(programming_dictionary)

## Create empty dictionary 
empty_dic = {}
print(programming_dictionary)   ##  It will print whole dictionary with keys & its Values 

### Loop through the dictionary
for key in programming_dictionary:    
    print(key)                            ## it will only print keys of the dictionary
    print(programming_dictionary[key])    ## It will give the value 
    





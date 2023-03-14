piano_keys = ['a','b','c','d','e','f','g','h']
print (piano_keys[:])  ## It will print the whole list : -- it use to create new list
print(piano_keys[:3])  ## It will slice the list from starting index 0 till index 1 (exluding the last)
print(piano_keys[2:5]) ## It will slice the list starting from 2 to 5 index excluding index 5
print(piano_keys[1:])  ## It will slice the list from begining index 1 till index end,  
print(piano_keys[:-1]) ## It will slice the list starting from right side , 
print(piano_keys[:-2])
print(piano_keys[2:-5])  ## It will slice from index [2] to index [-5]
print(piano_keys[2:6:2])  ## Start from index 2 and slice till 6 , at step of 2 
print(piano_keys[::2])   ## Hold of full list, but it will print alternate item. 
print(piano_keys[::-1])   ## Hold of full list, but it will print starting from -1 (reverse) item.
print(piano_keys[0:-3])
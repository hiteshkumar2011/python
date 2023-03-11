# 🚨 Don't change the code below 👇
age = input("What is your current age? ")  
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
year_remaining = 90 - int(age)          ## Considering if we are going to live till 90 
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12

# f-string 
message= f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print (message)
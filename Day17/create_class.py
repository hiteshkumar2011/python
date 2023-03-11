
#PascalCase = First Letter Of Word Will Be Capital
#camelCase  = 
#snake_case = all words are in small case but separated by underscore

class User:
    def __init__(self,userid,name):    ## Special function initialization - called constructor,passing another attribute 
        self.username = name
        self.id = userid
        self.followers =0
        self.following =0
        #print("New user will be created")

    def follow(self,user):
        user.followers +=1
        self.following +=1


user1 = User("001","Hitesh")
user2 = User("002","Trisha")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)






# user2 = User()
# user2.userid = "002"
# user2.name = "HKT"
# print(user2.userid)
# print(user2.name)

# class Car():
#     def enter_race_mode(self):
#         self.seats = 2
#         print(self.seats)

# car = Car()
# car.enter_race_mode()

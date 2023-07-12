# Create Class

# Q.1: A slug's blood is green. (True/False)?: true
# You got it right!
# The correct answer was: True.
# Your current score is: 1/1.

# Q.2: The loudest animal is the African Elephant. (True/False)?: false
# You got it right!
# The correct answer was: False.
# Your current score is: 2/2.

# Q.3. Approximately one queater of human bones are in the feet. (True/False): true

class User: # Create a blueprint
    pass # When you don't want to put anything in, using pass. 

user_1 = User()

def function():
    pass

print("hello")

# =====================================
class User:
    p

user_1 = User()
user_1.id = "001"          # attributes
user_1.username = "hailey" # attributes

print(user_1.username) # hailey

user_2 = User()
user_2.id = "002"
user_2.name = "kelly"  # user_2.username = "kelly" has yellow underline.
# =====================================

# initialize

class Car:
    def __init__(self): #initialize attributes
        print("new user being created...")

class Car:
    def __init__(self, seats):# parameter = attributes
        self.seats = seats

my_car = Car(5)

# ============================
class Car:
    def enter_race_mode(self): # method
        self.seats = 2

my_car.enter_race_mode()

# ==============================
class User:

    def __init__(self, user_id, username): # 초기화 기능
        self.id = user_id
        self.username = username 

user_1 = User("001", "hailey") # attribute
user_2 = User("002", "kelly")

print(user_1.username)
print(user_1.id)

# ========================= 
# Example Instagram

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Default value

user_1 = User("001", "angela")
user_2 = User("002", "jack")
# user_3 = User("003", "hailey", 0) # (user_id, username, followers)

print(user_1.followers)




    

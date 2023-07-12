class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Default value
        self.following = 0 

    def follow(self, user): # 메소드의 경우 함수와 달리 항상 첫 번째 매개변수로 자체 매개변수가 있어야 한다. 
        user.followers += 1 # another user
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")
# user_3 = User("003", "hailey", 0) # (user_id, username, followers)

print(user_1.followers)

# self 키워드는 우리가 클래스와 작업할 때 상당히 중요하다. 이는 사물, 객체를 참조하는 방법이다. 

user_1.follow(user_2)
print(f"user_1's followers count is {user_1.followers}")
print(user_1.following)
print(user_2.followers)
print(user_2.following)


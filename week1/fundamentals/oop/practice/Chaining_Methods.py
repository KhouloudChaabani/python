class user:
    def __init__(self, first_name, last_name, email, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("==========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            "you dont have enough points"
            return
        
        self.gold_card_points = self.gold_card_points - amount

my_user = user("Sadie", "Flick", "sflick@codingdojo.com", 39)
my_user.display_info()

user2 = user("Clifford", "Brown", "cbrown@codingdojo.com", 25)
user3 = user("Sonny", "Rollins", "srollins@codingdojo.com", 92)

my_user.spend_points(50)
user2.enroll()
user2.spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()

import getpass
import instaloader

print("=============================================================")
print("     ***    Welcome to instagram unfollow finder    ***")
print("=============================================================")

username = input("Enter your instagram username : ")
password = getpass.getpass("Enter your instagram password: ")
print("\nplease wait to login...")
load = instaloader.Instaloader()
load.login(username, password)
print("Login is succesful!")
Insta_Page = input("Enter the username of your favorite page on instagram: ")
profile = instaloader.Profile.from_username(load.context, Insta_Page)

old_followers=[]
new_followers = []

file = open("Followers.txt", "r")
for line in file:
    old_followers.append(line)
file.close()


for follower in profile.get_followers():
    new_followers.append(follower.username)

file = open("Followers.txt", "w")
for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)
        file.write(new_follower + "\n")

file.close()

import json
from userinfo_functions import UserInfo
# Welcome user
print("Press 'q' to quit.")
start = input("Welcome! To make a personal file about yourself, type 'start': ")

# Make function that will run program
def start_project():
    u = UserInfo()
    u.dump_info()
    u.compiled_info()
    u.json_pass()

while True:
    if start == 'start':
        # run script
        start_project()

        # Do another file?
        again = input("\nWould you like to try again? (y/n)")
        if again == 'n' or again == 'q':
            break
        
    elif start == 'q':
        break
    else:
        print("'start' is case sensitive! Check spelling.")
        break

print("Good day, \nYou have visited MREO website.")
from plates_No import plates_list
plates = set(plates_list)   # to count how many unique No`s in plates_list
print(f"Currently, we have {len(plates)} unique plates No`s!!!")
user = input("Please enter your desired plate No: ").upper()
print(user in plates_list)
# while True:
#     print("Oooops. This number already exists in the database.\nThe summary of all numbers inside the current plate is: ")
if user in plates_list:
    print("Oooops. This number already exists in the database."
          "The summary of all numbers inside the current plate is: ")
    user = list(user)
    del user[:2]; del user[-2:]
    print(sum([int(value) for value in user]))
    print("Please enter different No")
elif user not in plates_list:
    print("Please check your entering format!!!")
else:
    print("This plate No does not exist in date base.\nThe summary of all numbers inside the current plate is:")
    user = list(user)
    del user[:2]; del user[-2:]
    print(sum([int(value) for value in user]))


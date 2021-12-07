from plates_No import plates_list

print("Dear Customer,\nGood day,\nYou have visited MREO website.")

while True:
    user = input("Please enter your desired plate No: ").upper()
    while len(user) == 0:
        user = input("Please enter your desired plate No: ").upper()

    plates = set(plates_list)
    print(f"Currently, we have {len(plates)} unique plates No`s!!!")  # to show amount of unique plates numbers

    if user in plates_list:
        print(f"Oooops. This plates_No - '{user}' already exists in the database."
              f"\nThe summary of all numbers inside the current plate is: ")
        user = list(user)
        del user[:2]
        del user[-2:]
        print(sum([int(value) for value in user]))
        print("Please enter different No: ")
    # elif user not in plates_list:
    #     print("Please check your entering format!!!"
    #           "Example: BH1011OE")
    #   True
    else:
        print(f"This plates_No - '{user}' does not exist in the date base.\n"
              "The summary of all numbers inside the current plate is:")
        plates_list.insert(0, user)
        user = list(user)
        del user[:2]
        del user[-2:]
        print(sum([int(value) for value in user]))

    choose_again = input("Choose again? (YES/NO): ").upper()
    if choose_again != "YES":
        print("Good byeeeeeee!")
        break

    print(plates_list)

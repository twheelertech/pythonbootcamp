age = int(input("how old are you: "))


if age:
    if age >= 18 and age < 21:
        print("You can enter but need a wristband!")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("You are too young sorry...")
else:
    print("Please enter an age.")

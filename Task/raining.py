raining = input("Is it raining? (yes/no): ").lower()

if raining == "yes":
    windy = input("Is it windy? (yes/no): ").lower()

    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
mark = int(input("Enter the mark :"))

if mark >= 0 and mark <= 100:

    if (mark > 90) :
        print(f"U Scored A grade")

    elif mark > 75 and mark <= 90 :
        print(f"U Scored B graade")

    elif mark >= 60 and mark <= 75:
        print(f"U Scored C grade")
    else:
        print("U are failed")

else:
    print(f"GETOUT")

n = int(input("Enter a number :"))

if n %2 == 0 :   
    
    if n >= +2 and n <= +5 :
        print(f"Not weired")
    elif n >= +6 and n <= +20:
       print(f"Weird")
    elif n > +20:
        print(f"Not Weird")      
    else:
        print("GetOut")  
else:
    print("Weird")

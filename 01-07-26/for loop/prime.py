

# # n = int(input("Enter N :"))
# # if n > 1:
# #     for i in range(2,n):
# #         if n %i == 0:
# #             print(f"not prime")
# #             break
# #     else:
# #         print(f"Its prime")
# # else:
# #     print(f"Getout")




# n = 1
# while( n <= 1):
#     n = int(input("Enter N :"))
# for i in range(2,n):
#     if n % i == 0 :
#         print(f"{n}is not prime")
#         break
# else:
#     print(f"{n}is prime")


count = 0
for i in range(100,1001):
    for j in  range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
        if count == 10:
            break
        

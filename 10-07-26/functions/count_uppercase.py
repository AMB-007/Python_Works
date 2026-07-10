#count uppercase,lowercase,digits and specialcharacters
# text = "programMING@123"



text = "programMING@123"

upper = 0
lower = 0
digit = 0
special = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print(upper)
print(lower)
print(special)
print(special)




def count(text):
    u = l = d = s = 0
    for ch in text:
        if ch.isupper():
            u += 1
        elif ch.islower():
            l += 1
        elif ch.isdigit():
            d += 1
        else:
            s += 1
    return u, l, d, s

print(count("programMING@123"))
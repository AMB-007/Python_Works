# Question: Write a Python program for upper case.

def upper_case(text):
    for ch in text:
        if ch.isupper():
            print(ch,end=" ")
upper_case("PyTHon")

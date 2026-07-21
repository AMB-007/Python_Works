def reverse(text):
    for i in text:
        if i == "p":
            print(text[0:text.index(i)][::-1] + text[text.index(i)::])
            break
    else:
        print(text[::-1])

            

reverse("hellopython")
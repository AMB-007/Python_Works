def is_panagram(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in alpha:
        if i not in  text.lower():
            print("not panagram")
            break
    else:
        print("panagram")

is_panagram("The quick brown fox jumps over the lazy dog")
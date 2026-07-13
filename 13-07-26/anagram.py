def is_anagram(text_1,text_2):
    if len(text_1) == len(text_2):
        for i in text_1:
            if text_1.count(i) != text_2.count(i):
                print("not anagram")
                break
        else:
            print("anagram")

    else:
        print("not anagram")
is_anagram("silent","listen")
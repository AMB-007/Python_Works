def recursive(text):
    new = ""
    for i in text:
        # if text.count(i) >1:
        #     print(i)
        #     break
        if i not in new:
            if text.count(i) > 1 :
                new += i
                print(i,text.count(i))

        # if text.count(i) == 1:
        #     print(i)
        #     break


recursive("AABBCDAB")
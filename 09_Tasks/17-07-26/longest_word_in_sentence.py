# Q14. Find the longest word in a sentence
# Input: Python is a powerful programming language
# Output: programming

sentence = input("Enter a sentence: ")
words    = sentence.split()
longest  = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

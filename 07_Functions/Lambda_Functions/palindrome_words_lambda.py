# Lambda function to filter palindrome words from a list

words = ["madam", "python", "level", "code", "radar"]
get_palindromes = lambda word_list: [w for w in word_list if w == w[::-1]]

print("Words:", words)
print("Palindromes:", get_palindromes(words))

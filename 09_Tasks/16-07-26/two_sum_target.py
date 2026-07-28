# Question: Find two numbers in a list that sum to target

numbers = [3, 4, 5, 1]
target = 7

def two_number_sum(elements, target_val):
    pairs = []
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            if elements[i] + elements[j] == target_val:
                pairs.append((elements[i], elements[j]))
    return pairs

print(f"Pairs summing to {target}:", two_number_sum(numbers, target))


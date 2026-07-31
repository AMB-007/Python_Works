# Question: Input three numbers. If sum > 100, print product. If 50 <= sum <= 100, print average. If sum < 50, if any is divisible by 5, print smallest number; else print largest.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

nums = [num1, num2, num3]
total_sum = sum(nums)

print(f"\nNumbers: {nums} | Sum: {total_sum}")

if total_sum > 100:
    product = num1 * num2 * num3
    print(f"Sum > 100: Product = {product}")
elif 50 <= total_sum <= 100:
    avg = total_sum / 3
    print(f"Sum between 50 and 100: Average = {avg:.2f}")
else:
    # sum < 50
    divisible_by_5 = [n for n in nums if n % 5 == 0]
    if len(divisible_by_5) > 0:
        print(f"Sum < 50 and divisible by 5 found: Smallest Number = {min(nums)}")
    else:
        print(f"Sum < 50 and no number divisible by 5: Largest Number = {max(nums)}")

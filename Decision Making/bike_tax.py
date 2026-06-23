bike = int(input("Ente the bike price :"))

if bike > 20000:
    tax = bike * 0.12
elif bike <= 20000 and bike >= 10000:
    tax = bike * 0.10
else:
    tax = bike * 0.7
print(f"Your total tax is { bike + tax}")
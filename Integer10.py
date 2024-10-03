son = int(input("Uch xonali son kiriting: "))

birlik = son%10
son //= 10
son %= 10

print(f"Birliklar xonasi: {birlik}\nO'nliklar xonasi: {son}")
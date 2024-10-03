son = int(input("Uch xonali son kiriting: "))

yuzlik = son//100
onlik = (son//10)%10
birlik = son%10

yigindi = yuzlik+onlik+birlik

print(f"Natija: {yigindi}")
son = int(input("Uch xonali son kiriting: "))

yuzlik = son//100
onlik = (son//10)%10
birlik = son%10

natija = yuzlik*100+birlik*10+onlik

print(f"Natija: {natija}")
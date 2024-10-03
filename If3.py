son = int(input("Son kiriting: "))

if son>0:
    print(f"Natija: {son+1}")
elif son == 0:
    son = 10
    print(f"Natija: {son}")
else: print(f"Natija: {son-2}")
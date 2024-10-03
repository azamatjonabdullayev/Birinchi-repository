son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

if son1<son2 and son1<son3:
    print(f"{son1} eng kichik son.")
elif son2<son1 and son2<son3:
    print(f"{son2} eng kichik son.")
else:
    print(f"{son3} eng kichik son.")
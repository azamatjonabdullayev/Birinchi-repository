son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

if son1<son2<son3 or son1<son3<son2:
    print(f"{son1} Eng kichik son.")
elif son2<son1<son3 or son2<son3<son1:
    print(f"{son3} Eng kichik son.")
elif son3<son1<son2 or son3<son2<son1:
    print(f"{son3} eng kichik son.")

if son1>son2>son3 or son1>son3>son2:
    print(f"{son1} Eng katta son.")
elif son2>son1>son3 or son2>son3>son1:
    print(f"{son3} Eng katta son.")
elif son3>son1>son2 or son3>son2>son1:
    print(f"{son3} eng katta son.")
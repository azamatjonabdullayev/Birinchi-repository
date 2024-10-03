son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

if son1<son2<son3 or son1>son2>son3:
    print(f"{son2} o'rtancha son.")
elif son2<son1<son3 or son2>son1>son3:
    print(f"{son1} o'rtancha son.")
elif son1==son2==son3:
    print("Barchasi teng.")
else:
    print(f"{son3} o'rtancha son.")
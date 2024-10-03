son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))


if (son1>0 and (son2<=0 | son3<=0)) or (son1<=0 and (son2>0 | son3<=0)) or (son1<=0 and (son2<=0 | son3>0)):
    print("Bitta musbat son bor.")
elif ((son1>0 and son2>0) and son3<=0) or ((son1>0 and son3>0) and son2<=0) or ((son2>0 and son3>0) and son1<=0):
    print("Ikkita musbat son bor.")
elif son1>0 & son2>0 & son3>0:
    print("Uchta musbat son bor.")
else: print("Barcha son manfiy.")
sukupuoli = input("Oletko mies vain nainen: ")
hemo = float((input("Anna hemoglobiiniarvosi: ")))

if sukupuoli == str("mies") and 134 <= hemo <= 195:
    print("hemoglobiiniarvvosi on normaali")
elif sukupuoli == str("mies") and hemo < 134:
    print("hemoglobiiniarvvosi on alhainen")
elif sukupuoli == str("mies") and hemo > 195:
    print("hemoglobiiniarvvosi on ylhäinen")
elif sukupuoli == str("nainen") and 117 <= hemo <= 175:
    print("hemoglobiiniarvvosi on normaali")
elif sukupuoli == str("nainen") and hemo < 117:
    print("hemoglobiiniarvvosi on alhainen")
elif sukupuoli == str("nainen") and hemo > 175:
    print("hemoglobiiniarvosi on ylhäinen")
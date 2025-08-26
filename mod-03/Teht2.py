hytti = str(input("Onko hyttiluokkasi LUX,A,B vai C: "))
if hytti == str("LUX"):
    print("Lux on parvekkeellinen hytti yläkannella")
elif hytti == str("A"):
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti == str("B"):
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hytti == str("C"):
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")
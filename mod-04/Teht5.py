kj = "python"
salasana = "rules"
arvaukset = 0

while arvaukset <5:
 kjar = input("Anna käyttäjätunnus: ")
 salasanaar = input("Anna salasana: ")
 arvaukset = arvaukset + 1

 if kj != kjar or salasana != salasanaar:
    print("Salasana tai käyttäjätunnus on väärin")
 elif salasana == salasanaar and kj == kjar:
    print("Tervetuloa")
    break
else:
    print("Pääsey evätty")
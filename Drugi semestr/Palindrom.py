x = input("podaj nazwa: ") #Wpisz nazwe
size = len(x) #długość nazwy
p = size-1 #nsprawdzamy kolejną litere
index = 0  #od pierwszej litery
while index < p: #kiedy pierwsza cyfra indeksowa bo bo jak a jest pierwsze to ma indeks 0 taka jest numeracja w python
   if x[index] == x[p]: #porównanie liczb
       index = index + 1
       p = p-1
       print("napis jest palindromem") #jeśli jest palindromem to wyświel to co w ""
       break #przerwij
   else: #sprawdź drugą możliwość
       print("napis nie jest palindromem") #jeśli nie jest to wyświetl to co ""
       break #przerwij
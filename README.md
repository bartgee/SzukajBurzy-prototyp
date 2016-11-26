SzukajBurzy-prototyp
====================

Prototyp dla aplikacji napisanej w C++ (http://szukajburzy.tk).

Dane o zagrożeniach pogodowych dostępne są poprzez SOAP API na stronie
https://burze.dzis.net/?page=api_interfejs.

Tak wygląda w działaniu:
```
bart@tux:~/Dokumenty/python/github/SzukajBurzy-prototyp$
./szukajburzy-prototyp.py
*** SzukajBurzy 0.1 Prototyp ***

auth=True
współrzędne miasta Przywidz: 54.12, 18.19

ostrzeżenia pogodowe:
mróz=0
upał=0
wiatr=0
burza=0
mróz=0
tornado=0
<SOAPpy.Types.structType return at 139888495995216>: {'okres': 20, 'odleglosc':
0.0, 'kierunek': '', 'liczba': 0}
bart@tux:~/
```

"""Matemaatilised tehted"""
from turtledemo.chaos import f
import math
# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
a = float(input("sisesta a:"))
b = float(input("sisesta b:"))

c = (a ** 2) + (b ** 2)
if c < 0:
    print("lahendid puuduvad")
else:
    vastus = math.sqrt(c)
    print(f"hüpotenuus on: {round(vastus, 2)}")
    print(f"ümbermõõt on: {round (a+b+vastus, 2)}")
    print(f"pindala on: {round ((a*b)/2, 2)}")




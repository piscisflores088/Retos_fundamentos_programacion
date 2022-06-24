

print("Dia 1. Puntos IMECA:")
dia1 = int(input())
print("Dia 2. Puntos IMECA:")
dia2 = int(input())
print("Dia 3. Puntos IMECA:")
dia3 = int(input())
print("Dia 4. Puntos IMECA:")
dia4 = int(input())
print("Dia 5. puntos IMECA:")
dia5 = int(input())
print("Ganancias diarias")
gan_diarias = float(input())
prom_puntos = (dia1+dia2+dia3+dia4+dia5)/5
if prom_puntos>170:
	dinero_perdido = (0.5*gan_diarias*5)+(gan_diarias*5)
else:
	dinero_perdido = 0
print("Obtuviste un promedio de ",prom_puntos," puntos IMECA")
print("Dinero perdido ",dinero_perdido)
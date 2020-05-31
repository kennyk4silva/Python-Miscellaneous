# MIT License

# Copyright (c) 2020 Kenny Silva

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ======================
# PROBLEMA DE MONTY HALL
# ======================

# Importa de la biblioteca random la función randint.
from random import randint

# Variables para almacenar la cantidad de concursantes que ganan o pierden el automóvil.
ganaSinCambiar = 0
pierdeSinCambiar = 0
ganaCambiando = 0
pierdeCambiando = 0

# Puerta alterna con la cual el concursante podrá cambiar de opinión respecto a la puerta elegida en primer lugar. Inicialmente se asumirá como 0 para efectos de inicialización.
puertaAlterna = 0

# Simula la participación de 100000 concursantes en el juego.
for i in range(100000):
	
	# Ubica aleatoriamente el premio en una de las tres puertas.
	puertaPremio = randint(1, 3)

	# Selecciona aleatoriamente la puerta elegida por el concursante.
	puertaElegida = randint(1, 3)
	
	# Puerta 1 con el premio.
	if puertaPremio == 1:
		
		puertaAlterna = 1
		if puertaElegida == 2:
			puertaMonty = 3
		elif puertaElegida == 3:
			puertaMonty = 2
		else:
			puertaMonty = randint(2, 3)
			if puertaMonty == 2:
				puertaAlterna = 3
			else:
				puertaAlterna = 2
	
	# Puerta 2 con el premio.
	elif puertaPremio == 2:
		
		puertaAlterna = 2
		if puertaElegida == 1:
			puertaMonty = 3
		elif puertaElegida == 3:
			puertaMonty = 1
		else:
			puertaMonty = randint(0, 1)
			if puertaMonty == 0:
				puertaMonty = 3
			if puertaMonty == 1:
				puertaAlterna = 3
			else:
				puertaAlterna = 1
	
	# Puerta 3 con el premio.
	if puertaPremio == 3:
		
		puertaAlterna = 3	
		if puertaElegida == 1:
			puertaMonty = 2
		elif puertaElegida == 2:
			puertaMonty = 1
		else:
			puertaMonty = randint(1, 2)
			if puertaMonty == 1:
				puertaAlterna = 2
			else:
				puertaAlterna = 1
				
	# Establece aleatoriamente si el concursante decide cambiar de opinión o no con respecto a la primera puerta elegida. Un valor 0 significa que no cambia de opinión y un 1 que si cambia de opinión.
	cambio = randint(0, 1)
	
	# Si decide cambiar de opinión entonces la nueva puerta elegida será la puerta alterna y suma un concursante a cada una de las variables correspondientes según su decisión.
	if cambio == 1:
		puertaElegida = puertaAlterna
		if puertaElegida == puertaPremio:
			ganaCambiando += 1
			print(str(i+1) + ")", "Ganó cambiando")
		else:
			pierdeCambiando += 1
			print(str(i+1) + ")", "Perdió cambiando")		
	else:
		if puertaElegida == puertaPremio:
			ganaSinCambiar += 1
			print(str(i+1) + ")", "Ganó sin cambiar")
		else:
			pierdeSinCambiar += 1
			print(str(i+1) + ")", "Perdió sin cambiar")

# Porcentajes de resultados.
pGanaSinCambiar = round(ganaSinCambiar / 100000 * 100, 1)
pPierdeSinCambiar = round(pierdeSinCambiar / 100000 * 100, 1)
pGanaCambiando = round(ganaCambiando / 100000 * 100, 1)
pPierdeCambiando = 100 - (pGanaSinCambiar + pPierdeSinCambiar + pGanaCambiando)

print()
print("=" * 33)
print("R E S U L T A D O S:")
print("=" * 33)
print("SIMULACIÓN DE 100000 CONCURSANTES")
print("PREMIO: Vehículo\n")
print(ganaSinCambiar, " ({:.1f}%), ganan sin cambiar".format(pGanaSinCambiar), sep = "")
print(pierdeSinCambiar, " ({:.1f}%), pierden sin cambiar".format(pPierdeSinCambiar), sep = "")
print(ganaCambiando, " ({:.1f}%), ganan cambiando".format(pGanaCambiando), sep = "")
print(pierdeCambiando, " ({:.1f}%), pierden cambiando".format(pPierdeCambiando), sep = "")

print("\nGANARON: ", ganaSinCambiar + ganaCambiando, " ({:.1f}%)".format(pGanaSinCambiar + pGanaCambiando), sep = "")
print("PERDIERON: ", pierdeSinCambiar + pierdeCambiando, " ({:.1f}%)".format(pPierdeSinCambiar + pPierdeCambiando), sep = "")

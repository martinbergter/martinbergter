


def cambiar_x(test):
	print("Juega X")
	x=33
	repeat=0
	while x in test:
		repeat+=1
		if repeat>=2:
			print("No man, Ya ocuparon esa casilla...")
		x=int(input("ingrese valor: "))
	out=x
	return out
	
def cambiar_o(test):
	print("Juega O")
	o=33
	repeat=0
	while o in test:
		repeat+=1
		if repeat>=2:
			print("No man, Ya ocuparon esa casilla...")
		o=int(input("ingrese valor: "))
	out=o
	return out

def mostrartabla (tabla):
	
	
	a=0
	for i in range(3):
		print(tabla[a],tabla[a+1],tabla[a+2])
		a+=3
	if tabla[0]==tabla[1] and tabla[1]==tabla[2] or tabla[3]==tabla[4] and tabla[4]==tabla[5]or tabla[6]==tabla[7] and tabla[7]==tabla[8] or tabla[0]==tabla[3] and tabla[3]==tabla[6] or tabla[1]==tabla[4] and tabla[4]==tabla[7] or tabla[2]==tabla[5] and tabla[5]==tabla[8] or tabla[0]==tabla[4] and tabla[4]==tabla[8] or tabla[2]==tabla[4] and tabla[4]==tabla[6]:
		print ("el ultimo jugador ha ganado\nganador!!!")
		exit()
		
	
def main():
	print("Bienvenidos a TA TE TI")	
	print("para ingresar un valor debe:\n ingresar el numero que ocupa la la casilla que quiere ocupar en este orden\n por  ej: 1")
	tabla=[0,1,2,3,4,5,6,7,8]
	test=[33,33,33,33,33,33,33,33,33]
	mostrartabla(tabla)
	
	while("Start"):
		cambio=cambiar_x(test)
		tabla[cambio]="X"
		test[cambio]=cambio
		if test == [0,1,2,3,4,5,6,7,8]:
			print("EMPATE")
			exit()
		mostrartabla(tabla)
		cambio=cambiar_o(test)
		tabla[cambio]="O"
		test[cambio]=cambio
		mostrartabla(tabla)

if __name__ == '__main__':
    import sys
    main()

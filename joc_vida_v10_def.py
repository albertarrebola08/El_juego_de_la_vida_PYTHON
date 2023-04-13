'''
@ Author: Albert Arrebola Sans
'''
import os # import de una libreria para limpiar la consola en cada evolución
var = os.name 
import random #importo libreria random aleatorio
uno = 0
def numAleatorio(porcentaje): #creo una función donde le pasaré un porcentaje cada vez que la llame
    aleatorio = random.randint(0,100) #guardo un numero aleatorio entre el 0 i el 100
    if porcentaje == 0:
        return("·")
    elif aleatorio <= porcentaje: #en el caso de ser sobre 3, la probabilidad de que salga un 1 un 2 o un 3 era de un 33%, si se traslada al 100% la probabilidad de que salga un numero inferior a un 50% por ejemplo es del 50% por ciento, y de esta manera con el input se indica que porcentaje y sei el numero es menor cumple con la probabilidad (aunque no és exacto del todo)
        return("#")  #devuelve hastags que son vivas para rellenar en base al porcentaje calculado  
    else:
        return("·")#devuelve puntos que son muertas para rellenar en base al porcentaje calculado  

#######################   FUNCION BORRAR PANTALLA ###########  
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
   
#################################################
def crearMatriz(xx,yy,porcentaje): #le paso 3 parámetros que serán las filas y las columnoas, y por ultimo el porcentaje de casillas vivas que se requiera
    global matriz 
    global matriz2
    matriz = [] #creo una lista vacía de nombre matriz
    matriz2 = [] #creo una lista vacía de nombre matriz2
    for y in range (yy): #en base a laprimera columna que es el for general
        matriz.append([]) #añado listas vacías para poder meter cosas dentro
        matriz2.append([])
        for x in range(xx): #con el anidado voy rellenando las diferentes filas
            resultado = numAleatorio(porcentaje) 
            if x == 0 or x == xx-1 or y == 0 or y == yy-1: #contemplo los bordes y los creo con 'x' para distinguirlos y le digo que no rellene las filas y columnas de los bordes
                matriz[y].append("x")
                matriz2[y].append("x")
         
            else:
                matriz[y].append(resultado) #añado a la matriz lo que haya en resultado que en este caso serán hastags o puntos dependiendo del porcentaje que se le ha pasado
                matriz2[y].append(resultado) 
    

####################################################
def blinker(x,y): #creo la primera forma blinker pasandole dos coordenadas 'x' 'y'
    global matriz
    global pregunta_dimensions
    if (x + 2) > pregunta_dimensions[0]: #contemplo que como la coordenada empieza en el punto oeste, en su longitud no se salga del tablero y si es el caso avisar
        print("La peça es surt del tauler per tant no s'escriurà...")
    else:
        #relleno las coordenadas de la forma de la pieza blinker
        matriz[y][x] = "#" 
        matriz[y][x+1] = "#"
        matriz[y][x+2] = "#"
#IGUAL QUE EN EL CASO ANTERIOR 
def block(x,y):
    global pregunta_dimensions
    global matriz
    if (x + 1) > pregunta_dimensions[0] or (y + 1) > pregunta_dimensions[1]:
        print("La peça es surt del tauler per tant no s'escriurà...")
    else:
        matriz[y][x] = "#"
        matriz[y][x+1] = "#"
        matriz[y+1][x] = "#"
        matriz[y+1][x+1] = "#"
def glider(x,y):
    global matriz
    global pregunta_dimensions
    if (x + 2) > pregunta_dimensions[0] or (y + 2) > pregunta_dimensions[1]:
        print("La peça es surt del tauler per tant no s'escriurà...")
    else:
        matriz[y][x] = "#"
        matriz[y][x+1] = "#"
        matriz[y][x+2] = "#"
        matriz[y+1][x] = "#"
        matriz[y+2][x+1] = "#"
################################################################
def casillas_manual(x,y): #creo una funcion donde le paso las coordenadas y que escribe un hastag en las coordenadas que se le pase al llamar a la función
    global matriz
    matriz[y][x] = "#"
################################################################
def transformaciones():  #cuenta los vecinos de cada elemento de la matriz y evoluciona según las condiciones establecidas
    global matriz
    global matriz2        
    for y in range (1,len(matriz)-1): #recorro la matriz
        for x in range (1,len(matriz[0])-1): #recorro la matriz
            matriz2[y][x] = evoluciones(x,y) #voy copiando el resultado de la función evoluciones en la matriz nueva (elemento a elemento)

    for y in range (1,len(matriz2)-1): #recorro la matriz2 nueva
        for x in range (1,len(matriz2[0])-1): #recorro 
            matriz[y][x] = matriz2[y][x] #y la vuelvo a trasladar copiando los valores a la matriz 1 para así tener la 2 libre e iniciar otra vez el proceso con solo 2 matrices
################################################################   
def dibujaMatriz(): #se dibuja la matriz que se ha creado con la función creaMatriz
    global matriz
    for y in range (len(matriz)):
        for x in range (len(matriz[0])): 
            print(matriz[y][x], end = " ") #printo cada elemento y dejo una separación entre estos
        print()
#################################################################
def dibujaMatriz2():
    global matriz2
    #hago lo mismo que en la función anterior pero para dibujar la matriz 2
    for y in range (len(matriz2)): 
        for x in range (len(matriz2[0])): 
            print(matriz2[y][x], end = " ")
        print()
#################################################################
def cuentaVecinos(x,y): #creo la funcion que contará vecinos y le paso los parámetros 'x' 'y' para que sepa de que casilla debe partir aunque será desde un for i se recorrerá toda
    global matriz
    global vecinos_vivos
    vecinos_vivos = 0 #pongo el contador de vecinos vivos a 0 
    #arriba - le explico que casillas son vecinas y que tienen que hacer si están vivas
    if  matriz[y-1][x-1] == "#":
        vecinos_vivos += 1
    if  matriz[y-1][x] == "#":
        vecinos_vivos += 1
    if  matriz[y-1][x+1] == "#":
        vecinos_vivos += 1
    #izquierda
    if  matriz[y][x-1] == "#":
        vecinos_vivos += 1
    #derecha
    if  matriz[y][x+1] == "#": 
        vecinos_vivos += 1
    #abajo
    if  matriz[y+1][x-1] == "#":
        vecinos_vivos += 1
    if  matriz[y+1][x] == "#":
        vecinos_vivos += 1
    if  matriz[y+1][x+1] == "#":
        vecinos_vivos += 1
    
   
    return(vecinos_vivos) #la función devuelve el numero de vecinos vivos por cada casilla

def evoluciones(x,y): #creo la función que evolucionará dependiendo de los vecinos vivos de la función anterior
    global matriz
    global matriz2
    global vecinos_vivos
    
    if matriz[y][x] == "#": #si la casilla esta viva
        if cuentaVecinos(x,y)<2 or cuentaVecinos(x,y) >3: # y tiene menos de 2 o más de 3 vecinos vivos....
            return("·") #pon un · en la casilla (muere)
        else: #sino
            return("#")# pon un # en la casilla (vive)
    else: #si está muerta....
        if cuentaVecinos(x,y) == 3: #y tiene exactamente 3 vecinos vivos...
            return("#") #devvuelve # (vive)
        else: #sino
            return("·") #devuleve  ·  (muere)


            
### INICIEM EL JOC ###
### MENÚ ###
print ('''
        1)VERSIÓ SIMPLE
        2)VERSIÓ COMPLETA
        ''')
pregunta_version = input("Indica a quina versió del joc vols jugar: ")
if pregunta_version == "1":
    crearMatriz(22,12,33) #llamo a crear matriz pasandole las medidas incluyendo los bordes y pasandole el porcentaje de vivas en el ultimo parámetro (33 pq es la version simple)
    dibujaMatriz() #dibujo la matriz
    pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ")
    borrarPantalla() #borro la consola para mostrar mejor las evoluciones

    while pregunta_evolucion !=  "finalitzar": #doy la opción de salir del juego - mientras no se quiera salir....
        transformaciones() #evoluciona la matriz
        dibujaMatriz() #dibujalas
        pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ") 
        borrarPantalla() #y borra la consola
    else: #si se quiere finalizar salir del juego con un msg final
        print()
        print("Has decidit sortir del joc... torna a inicialitzar el programa per jugar de nou.") 
##################################    VERSIÓN COMPLEJA     ###########################3
elif pregunta_version == "2": #si se escoge la versión completa...
    pregunta_dimensions = list(map(int,input("Indica les dimensions del taulell separades per comes: ").split(","))) #pregunta las dimenciones del tablero al usuario
    while pregunta_dimensions[0]<10 or pregunta_dimensions[0]>60 or pregunta_dimensions[1]> 30 or pregunta_dimensions[1] < 10: #si las medidas son validas segun el enunciado..., sino ...
        print()
        print("ERROR --- Recorda que el tauler ha de ser mínim 10x10 i màxim 60x30...")
        print()
        pregunta_dimensions = list(map(int,input("Indica les dimensions del taulell separades per comes: ").split(","))) #si con correctas, muestra el modo de inicializar con el print siguiente:
    print()
    print('''
                1) De manera aleatòria triant el percentatge de caselles vives.
                2) Triant quines caselles estan vives.
                3) Inserint formes al taulell. ''')
    print()
    pregunta_modo_inicializar = input("Com vols inicialitzar el taulell?: ")
#######################################    MODO 1    ################################
    if pregunta_modo_inicializar == "1": 
        #en este caso se crea la matriz y se le pasa el numero de vivos con el input en el parámetro de porcentaje
        pregunta_porcentaje = int(input("Tria el percentatge (%) de caselles vives: "))
        crearMatriz(pregunta_dimensions[0]+2,pregunta_dimensions[1]+2,pregunta_porcentaje)
        dibujaMatriz()
        pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ")
        borrarPantalla()
        print()
        print()
        while pregunta_evolucion !=  "finalitzar":
            transformaciones() 
            dibujaMatriz() 
            pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ") 
            borrarPantalla()
            print()
            print()
        else:
            print()
            print("Has decidit sortir del joc... torna a inicialitzar el programa per jugar de nou.") 
#######################################    MODO 2    ################################
    if pregunta_modo_inicializar == "2":
        crearMatriz(pregunta_dimensions[0]+2,pregunta_dimensions[1]+2,0) #se crea la matriz con las dimensiones deseadas pero porcentaje 0% para ver solo las vivas escogidas manualmente
        cant_caselles = int(input("Quantes caselles vols marcar?: "))
        for i in range (0,cant_caselles):
            coordenada = list(map(int,input("Indica les coordenades (x,y) de la casella separades per comes. (Exemple: 3,2): ").split(",")))
            while coordenada[0]>pregunta_dimensions[0] or coordenada[1]>pregunta_dimensions[1] or coordenada[0] <= 0 or coordenada[1] <= 0: #tenemos en cuenta las excepciones de los bordes
                print("ERROR -- Recorda que has de marcar una casilla de dins el tauler...")
                coordenada = list(map(int,input("Indica les coordenades (x,y) de la casella separades per comes. (Exemple: 3,2): ").split(",")))
            casillas_manual(coordenada[0],coordenada[1]) #llamamos a casillas manual que escribirá en las coordenadas que le indiquemos un '#'
            dibujaMatriz()
        pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ")
        borrarPantalla()
        while pregunta_evolucion !=  "finalitzar":
            transformaciones() 
            dibujaMatriz() 
            pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ") 
            borrarPantalla()
        else:
            print()
            print("Has decidit sortir del joc... torna a inicialitzar el programa per jugar de nou.") 
########################################     MODO 3    ########################################
    if pregunta_modo_inicializar == "3":
        crearMatriz(pregunta_dimensions[0]+2,pregunta_dimensions[1]+2,0)
        print(''' FORMES A ESCOLLIR:
        
        1.Blinker      2.Block       3.Glider
                                      # # #
          # # #         # #           #
                        # #             #
         ''')   

        cant_formes = int(input("Quantes formes vols col·locar?: "))
        for i in range (0,cant_formes):
            pregunta_piezas = input("Tria la forma (1 o 2 o 3) que vols col·locar al tauler: ")
            coordenada = list(map(int,input("Indica les coordenades (x,y) de la casella separades per comes. (Exemple: 3,2): ").split(",")))
            if pregunta_piezas == "1":
                blinker(coordenada[0],coordenada[1]) #dibuja la forma blinker 
            if pregunta_piezas == "2":
                block(coordenada[0],coordenada[1])#dibuja la forma block 
            if pregunta_piezas == "3":
                glider(coordenada[0],coordenada[1])#dibuja la forma glider 
        dibujaMatriz()
        pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ")
        while pregunta_evolucion !=  "finalitzar":
            transformaciones() 
            dibujaMatriz() 
            pregunta_evolucion = input("Pressiona enter per evolucionar o 'finalitzar' per sortir del joc: ") 
            borrarPantalla()       
        else:
            print()
            print("Has decidit sortir del joc... torna a inicialitzar el programa per jugar de nou.") 
        
        


            






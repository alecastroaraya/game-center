def juego_gato():
    import random
    '''
    Entrada: Ninguna
    Salida: El juego Gato
    Restricciones: Ninguna
    Esta funcion permite jugar Gato por medio del uso de varias subfunciones
    '''
    
    tamano = input("Seleccione el tamano de tablero que desea. Debe ser un numero impar.\n") # Pide al jugador que escoja el tamano del tablero, el cual debe ser un numero impar.
    
    if tamano.isdigit() == True:                                                             # Revisa que el tamano dado sea un entero. Si es entero, revisa que sea impar.
        tamano = int(tamano)
        if tamano % 2 == 0:                                                                  # Si es par, entonces dice que debe ser un numero impar y vuelve a pedir el tamano.
            print("Por favor rescriba un numero impar.\n")
            return juego_gato()
    
    elif tamano.isdigit() != True:                                                           # Si el tamano dado no fue un entero, entonces vuelve a pedir el tamano.
        print("Por favor escriba un numero impar.\n")
        return juego_gato()
    
    def flujo_juego():
        '''
        Entrada: Ninguna
        Salida: Printea el tablero
        Restricciones: Ninguna
        Esta funcion crea el flujo del juego, es decir, prepara el tablero para ser printeado dependiendo de su tamano, y determina el ganador o el empate, ademas establece que el jugador empieza y que es X
        '''
        
        # El tablero se crea usando una list comprehension, la cantidad de casillas _ que se crean es el tamano que escogio, y puse una lista dentro de una lista
        # para hacer dos list comprehensions para que la cantidad de casillas en el tablero sea el tamano multiplicado por el tamano, porque si fuera solo una lista el tablero no estaria completo.
        
        tablero = [["_" for casilla in range(tamano)] for casilla in range(tamano)]
        
        es_x = True                                                     # Aqui establezco que al inicio de la partida, el jugador humano es X, y es el que empieza.
        
        juego_terminado = False                                         # Establezco que el juego no se ha terminado, para poder cambiarlo a True cuando haya un ganador o un empate.
        
        while juego_terminado != True:                                  # Mientas el juego no se haya terminado, que el juego siga.
            
            if es_x == True:                                            # Si el jugador actual es X, es decir es el jugador humano, entonces printea el tablero y 
                                                                        # manda la seleccion del jugador a la funcion de seleccionar una casilla para el jugador humano.
                printear_tablero(tablero)
                try:                                                    # Aqui uso try except para que, si se escribe una seleccion de casilla no vacia o una seleccion que se sale del rango del tablero,
                                                                        # nada mas pide que se escoja una casilla vacia.
                                                                        
                    seleccion = tuple_seleccion(seleccionar_casilla())  # Se convierte la seleccion en un tuple, luego se pone el simbolo que va a ser X en este caso porque es_x es True.
                    poner_simbolo(seleccion, es_x, tablero)
                except ValueError:                                      # Si el valor escogido por el jugador no es valido entonces gracias al except ValueError
                                                                        # y gracias al continue va a seguir pidiendo un valor apropiado hasta que se de uno.
                    print("Por favor escoja un espacio vacio.\n")
                    continue
                    
                juego_terminado = ganador(tablero) or empate(tablero)   # Se revisa si hubo un ganador o un empate al final del turno. 
                                                                        # Estas funciones que estan definidas abajo retornan un False si se cumple alguna de ellas.
                                                                        # Si la funcion ganador o la funcion empate retornaron False, entonces el juego se termina. Si no retornaron False, entonces el juego sigue.
                                                                        
                es_x = False                                            # Se acabo el turno del jugador huamno, entonces se cambia al jugador CPU, entonces se cambia de X a O.
            
            
            elif es_x == False:                                         # Si el jugador actual NO es el jugador humano, entonces, se printea el tablero y manda la seleccion del cpu 
                                                                        # a la funcion de seleccionar casilla del CPU.
                printear_tablero(tablero)
                seleccion = tuple_seleccion(seleccionar_casilla_cpu())
                poner_simbolo(seleccion, es_x, tablero)
                juego_terminado = ganador(tablero) or empate(tablero)
                es_x = True                                             # Aqui se vuelve a cambiar es_x para que el jugador actual pase a ser el humano de nuevo, es decir, la X.
            
            # Este ciclo del flujo de juego se repetira hasta que haya un ganador o un empate
    
    def tuple_seleccion(seleccion):
        '''
        Entrada: La seleccion de casilla
        Salida: La seleccion de casilla convertida en un tuple
        Restricciones: La seleccion debe ser int
        Esta funcion convierte la seleccion de la casilla en un tuple para meterla en la matriz
        '''
         # Con esta funcion se convierte la seleccion de casilla en un tuple para que se pueda meter en la matriz de forma [i][j].
         
        if type(seleccion) != int:                       # Valida que el tipo de la seleccion sea un entero.
            return "Error 01"
                                                         
        seleccion = seleccion - 1                        # Aqui le resto uno a la seleccion porque python cuenta desde 0, entonces si uno escoge la casilla 1 en realidad se va a poner el simbolo en la segunda casilla
                                                         # y no la primera.
                                                         
                                                         # Entonces le resto uno a la seleccion para facilitar la comprension del juego para el jugador.
        
        
        return (seleccion // tamano, seleccion % tamano) # Se retorna la seleccion de la casilla en forma [i][j] por medio de ser dada como un tuple. Note que este tuple [i][j] en realidad son indices de lista.
                                                         # Uso division entera porque si uso divison va a dar error porque los indices de lista solo aceptan float o int.
                                                         # En [i], a la seleccion se le hace division entera entre el tamano para sacar la fila. 
                                                         # Luego, en [j] se saca el residuo de dividir seleccion entre tamano para sacar la columna.
                                                         # Esto dara la seleccion en modo [i][j], que es un tuple, y es como usar una matriz.
    
    def empate(tablero):
        '''
        Entrada: El tablero
        Salida: Un empate
        Restricciones: El tablero debe ser una lista
        Esta funcion determina si hubo un empate y lo printea
        '''
        if type(tablero) != list:                       # Se valida que el tipo del tablero sea una lista.
            return "Error 02"
        
        for fila in tablero:                            # Se revisan las filas del tablero, y dentro de las filas se revisan las casillas. Si una casilla sigue vacia, no puede haber empate todavia.
            for casilla in fila:                        
                if casilla == "_":
                    return False                        # Como una casilla sigue vacia, entonces retorna False para senalar que por ahora no hay empate.
                    
        printear_tablero(tablero)                       # Si al acabarse el loop no se retorno False, entonces hubo empate, por lo que printea el tablero final para mostrar que hubo un empate.
        print("\nHubo un empate!") 
        return menu_entrada()                           # Finalmente dice que hubo empate y luego vuelve al menu de entrada.
    
    def ganador(tablero):
        '''
        Entrada: El tablero
        Salida: El ganador
        Restricciones: El tablero debe ser una lista
        Esta funcion determina si hubo un ganador y quien lo fue, y lo printea
        '''
        if type(tablero) != list:
            return "Error 03"
        
        def revisar_X(tablero):                         # Se define la funcion que revisa si el jugador X gano.
            '''
            Entrada: El tablero
            Salida: Revisa y dice si X es el ganador de la partida
            Restricciones: El tablero debe ser una lista
            Esta funcion determina si X gano la partida mediante revisar si todas las casillas de una fila, columna, o diagonal tienen X
            '''
            if type(tablero) != list:
                return "Error 04"
            
            fila = 0
            columna = 0
            
            # Revisa si alguna fila tiene todas las casillas llenas con el mismo simbolo (revisa horizontalmente).
            while fila < tamano:
                while columna < tamano:                 # Se van revisando todas las casillas de una fila mediante sumandole 1 a la columna para avanzar, si una fila no tiene todas X, se va a la siguiente.
                    if tablero[fila][columna] == "X":
                        columna = columna + 1
                        continue
                    else:
                        break                           # Si una fila no tiene todas las casillas con X, para de revisar y va a la siguiente fila mediante sumarle 1 a la variable fila.
                    
                if columna == tamano:                   # Si se llego a la ultima casilla de la columna significa que toda esa fila tiene X en todas sus casillas, entonces X gano la partida.
                    printear_tablero(tablero)
                    print("\nFelicidades! El ganador de la partida es X!")
                    print("\nVolviendo al menu de entrada...")
                    return menu_entrada()
                
                columna = 0
                fila = fila + 1
        
            fila = 0                                    # Si X no gano horizontalmente, se procede a revisar si gano verticalmente, entonces se resetean las variables.
            columna = 0
        
            # Revisa si alguna columna tiene todas las casillas llenas con el mismo simbolo (revisa verticalmente).
            while columna < tamano:
                while fila < tamano:                    # Se revisan todas las casillas de una columna mediante sumarle 1 a la fila para avanzar, si una columna no tiene todas X, se va a la siguiente.
                    if tablero[fila][columna] == "X":
                        fila = fila + 1
                        continue
                    else:
                        break                           # Si una columna no tiene todas sus casillas con X, para de revisar y va a la siguiente columna mediante break y sumarle 1 a la variable columna.
                    
                if fila == tamano:                      # Si se llego a la ultima casilla de la fila significa que X gano con esa fila, entonces X gano la partida.
                    printear_tablero(tablero)
                    print("\nFelicidades! El ganador de la partida es X!")
                    print("\nVolviendo al menu de entrada...")
                    return menu_entrada()
                
                fila = 0
                columna = columna + 1
        
            fila = 0                                    # Si la X no gano ni horizontalmente ni verticalmente, entonces revisa diagonalmente, entonces se resetean las variables fila y columna.
            columna = 0
        
            # Revisa si alguna diagonal tiene todas las casillas llenas con el mismo simbolo (revisa diagonalmente).
            # Primero revisa la diagonal que empieza en la primera casilla de la primera columna del tablero y va para abajo.
            while fila < tamano:
                if tablero[fila][columna] == "X":
                    fila = fila + 1
                    columna = columna + 1               # Revisa si la diagonal de izquierda a derecha esta llena de X mediante sumarle 1 a la fila y a la columna a la misma vez.
                    continue
                else:
                    break
            
            if fila == tamano:
                printear_tablero(tablero)
                print("\nFelicidades! El ganador de la partida es X!")
                print("\nVolviendo al menu de entrada...")
                return menu_entrada()
        
            fila = tamano - 1                           # Si aun no ha ganado X, entonces se revisa la diagonal que va de la ultima casilla de la primera columna para arriba. 
                                                        # Por lo que se define la fila como el tamano menos 1 porque se empieza a contar desde 0.
                                                        # Entonces se le resta 1 porque asi no va a dar index error en la ultima iteracion.
                                                        
            columna = 0
        
            # Luego revisa la diagonal que empieza en la ultima casilla de la primera columna y va para arriba.
            while fila+1 > 0:                           # Se usa fila+1 comparado con 0, porque si se usara solo fila, entonces no se revisaria la ultima casilla de la diagonal.
                if tablero[fila][columna] == "X":
                    fila = fila - 1                     # Se le va restando 1 a la fila porque como va desde la ultima casilla de la primera columna para arriba, entonces se ocupa retroceder la fila para ir arriba.
                    columna = columna + 1               # Se le va sumando 1 a la columna porque ocupa ir para arriba.
                    continue
                else:
                    break
            
            if fila+1 == 0:                             # Si se llego a la primera fila significa que X gano con esa diagonal, por lo que X gano la partida.
                printear_tablero(tablero)
                print("\nFelicidades! El ganador de la partida es X!")
                print("\nVolviendo al menu de entrada...")
                return menu_entrada()
        
        def revisar_O(tablero):                         # Se define la funcion para revisar si O gano, que sigue la misma logica que revisar_X solo que lo hace para O.
            '''
            Entrada: El tablero
            Salida: Revisa y dice si O es el ganador de la partida
            Restricciones: El tablero debe ser una lista
            Esta funcion determina si O gano la partida mediante revisar si todas las casillas de una fila, columna, o diagonal tienen O
            '''
            if type(tablero) != list:
                return "Error 05"
            
            fila = 0
            columna = 0
            
            # Revisa si alguna fila tiene todas las casillas llenas con el mismo simbolo (revisa horizontalmente)
            while fila < tamano:
                while columna < tamano:
                    if tablero[fila][columna] == "O":   # Hace exactamente lo mismo que revisar_X, pero el cambio es que revisa que las casillas tengan O en vez de X.
                                                        # Esto aplica para toda esta funcion asi que como los comentarios serian lo mismo que en revisar_X, para no sobresaturar, voy a evitar comentar tanto en esta funcion.
                        columna = columna + 1
                        continue
                    else:
                        break
                    
                if columna == tamano:
                    printear_tablero(tablero)
                    print("\nFelicidades! El ganador de la partida es O!")
                    print("\nVolviendo al menu de entrada...")
                    return menu_entrada()
                
                columna = 0
                fila = fila + 1
        
            fila = 0
            columna = 0
        
            # Revisa si alguna columna tiene todas las casillas llenas con el mismo simbolo (revisa verticalmente)
            while columna < tamano:
                while fila < tamano:
                    if tablero[fila][columna] == "O":
                        fila = fila + 1
                        continue
                    else:
                        break
                    
                if fila == tamano:
                    printear_tablero(tablero)
                    print("\nFelicidades! El ganador de la partida es O!")
                    print("\nVolviendo al menu de entrada...")
                    return menu_entrada()
                
                fila = 0
                columna = columna + 1
        
            fila = 0
            columna = 0
        
            # Revisa si alguna diagonal tiene todas las casillas llenas con el mismo simbolo (revisa diagonalmente)
            # Primero revisa la diagonal de izquierda a derecha
            while fila < tamano:
                if tablero[fila][columna] == "O":
                    fila = fila + 1
                    columna = columna + 1
                    continue
                else:
                    break
            
            if fila == tamano:
                printear_tablero(tablero)
                print("\nFelicidades! El ganador de la partida es O!")
                print("\nVolviendo al menu de entrada...")
                return menu_entrada()
        
            fila = tamano - 1
            columna = 0
        
            # Luego revisa la diagonal de derecha a izquierda
            while fila+1 > 0:
                if tablero[fila][columna] == "O":
                    fila = fila - 1
                    columna = columna + 1
                    continue
                else:
                    break
            
            if fila+1 == 0:
                printear_tablero(tablero)
                print("\nFelicidades! El ganador de la partida es O!")
                print("\nVolviendo al menu de entrada...")
                return menu_entrada()
    
        revisar_X(tablero)                              # Ahora que se definieron las funciones para revisar los ganadores, las llamo para que al llamar ganadores(tablero) se llamen ambas.
        revisar_O(tablero)                              # De esta manera se revisara si gano X o si gano O.
        
    def poner_simbolo(seleccion, es_x, tablero):
        '''
        Entrada: Tuple seleccion de casilla, si es X o no, y el tablero
        Salida: Pone el simbolo, ya sea X u O
        Restriccion: La seleccion debe ser un tuple, y el tablero debe ser una lista
        Esta funcion escribe ya sea una X o una O dependiendo de quien es el jugador actual
        '''
        if type(seleccion) != tuple:                            # Se valida que la seleccion sea un tuple.
            return "Error 05"
        elif type(tablero) != list:                             # Se valida que el tablero sea una list.
            return "Error 06"
        
                                                                # El tuple de la seleccion de la casilla se define como i,j para simular un elemento de una matriz y que asi se pueda entender mas facilmente.
                                                                # Si es X entonces escribe una X en la casilla elegida, si no entonces se escribe un O.
        i, j = seleccion
        if tablero[i][j] == "_":                                # Si la casilla esta vacia, entonces se pone una X si es_x es verdadero, si es_x es falso entonces se pone un O.
            tablero[i][j] = "X" if es_x == True else "O"
        
        elif tablero[i][j] != "_" and es_x == False:            # En caso de la casilla que eligio la computadora NO este vacia, vuelve a elegir una casilla al azar hasta que SI este vacia.
            seleccion = tuple_seleccion(random.randint(1,tamano*tamano))
            poner_simbolo(seleccion, es_x, tablero)
        
        else:                                                    # Si hay algun valor no valido entonces se hace raise a un ValueError para validar con try except.
            raise ValueError
    
    def printear_tablero(tablero):
        '''
        Entrada: El tablero
        Salida: Printea el tablero
        Restricciones: El tablero debe ser una lista
        Esta funcion printea el tablero mediante printear las filas
        '''
        if type(tablero) != list:                               # Si el tablero no es de tipo list, retorna error.
            return "Error 07"
        
                                                                # Se usa un for para printear las filas del tablero una por una.
        for fila in tablero:                                    # Las filas van a ser printeadas de manera que van a dar la ilusion que son un tablero, pero en realidad son solo varias listas separadas.
            print(fila)
    
    def seleccionar_casilla():
        '''
        Entrada: Ninguna
        Salida: La seleccion de casilla del jugador humano
        Restricciones: Ninguna
        Esta funcion retorna la seleccion de casilla del humano para mandarla a convertirse a tuple luego
        '''
        seleccion = int(input("\nSeleccione una casilla donde poner su simbolo: ")) # Pide al jugador que escoja en que casilla quiere escribir su simbolo.
        
        if seleccion < 1 or seleccion > tamano*tamano:                              # Se valida que la casilla sea mayor a 1 y menor o igual al numero de la ultima casilla,
                                                                                    # la cual se calcula con el tamano multiplicado con el mismo.
                                                                                    
            raise ValueError                                                        # Para validar esto, si no se cumplen esas condiciones, se hace raise a un ValueError, lo que permitira pedir la seleccion
                                                                                    # de nuevo hasta que se de una seleccion apropiada, gracias al try except de flujo_juego.
                                                                                    
        return seleccion                                                            # Se retorna la seleccion.
    
    def seleccionar_casilla_cpu():
        '''
        Entrada: Ninguna
        Salida: La seleccion de casilla del jugador computadora
        Restricciones: Ninguna
        Esta funcion retorna la seleccion de casilla de la computadora para mandarla a convertirse a tuple luego
        '''
        respuesta = input("\nEl CPU esta moviendose. Por favor presione ENTER para seguir.") # Se indica que es el turno del CPU y pide presionar una tecla para avanzar el juego.
        
        seleccion = random.randint(1,tamano*tamano)                                          # Se escoje un numero random para que este que sea la casilla elegida de la computadora.
        
        if seleccion < 1 or seleccion > tamano*tamano:                                       # Se usa un ValueError para podere validar con el try except de flujo_juego
                                                                                             # si la seleccion es menor a 1 o mayor que la ultima casilla.
            raise ValueError
        return seleccion
    
    return flujo_juego()

def juego_21():
    '''
    Entrada: Ninguna
    Salida: El juego 21
    Restricciones: Ninguna
    Esta funcion permite jugar 21 por medio de varias subfunciones, ademas tiene los perfiles de las computadoras y las prioridades de ganador
    '''
    import random                                                                           # Se importa random para poder usar randint para generar numeros random y shuffle para revolver el mazo.
    
    figuras  = [numeros for numeros in range(2,11)] + ["jota", "reina", "rey", "as"]        # En esta lista estan las figuras, es decir, los numeros del 2 al 10, y la jota, la reina, el rey y el as.
    palos = ["picas", "corazones", "rombos", "treboles"]                                    # En esta lista estan los palos, los cuales son picas, corazones, rombos, y treboles.
    
    def obtener_mazo():
        '''
        Entrada: Ninguna
        Salida: Un nuevo mazo de cartas
        Restricciones: Ninguna
        Esta funcion retorna un nuevo mazo de cartas
        '''
        return [[figura, palo] for figura in figuras for palo in palos]                    # Retorna un mazo con todas las posibles combinaciones de figuras y palos y retorna cada combinacion en forma de lista.
    
    mazo = obtener_mazo()                                                                  # Define la variable mazo como lo que retorno la funcion obtener_mazo(), o sea, todas las combinaciones de cartas.
    random.shuffle(mazo)                                                                   # Se revuelve el mazo con shuffle.
    
    humano_adentro = True                                                                  # Se define la variable humano_adentro, esta indica que el humano sigo dentro del juego y no se ha decidido quedar fuera.
    
    mano_computadora = [mazo.pop(), mazo.pop()]                                            # Saca los ultimos dos elementos del mazo revuelto y los agrega a la mano de la computadora, eso se tomara como su mano.
    mano_humano = [mazo.pop(), mazo.pop()]                                                 # Saca los ultimos dos elementos del mazo revuelto y los agrega a la mano del humano, eso sera su mano.
    
    def valor_carta(carta):
        '''
        Entrada: Una carta
        Salida: El valor de la carta
        Restricciones: La carta debe ser una lista
        Esta funcion retorna el valor int de una carta dada
        '''
        if type(carta) != list:
            return "Error 01"
        
        figura = carta[0]                                                                  # Saca el primer elemento de la lista de la carta ya que ese es su valor, y esa sera la figura de la carta.
        if figura in figuras[0:-4]:                                                        # Si el primer elemento de la carta es un numero (es decir es de 2 a 10), entonces se convierte a int y eso se retorna.
            return int(figura)
        elif figura == "as":                                                               # Si el primer elemento es un as, su valor es 11
            return 11
        else:                                                                              # El else significa que si el primer elemento es una jota, un rey, o una reina, su valor es 10
            return 10
    
    def valor_mano(mano):
        '''
        Entrada: Una mano
        Salida: El valor de la mano dada
        Restricciones: La mano debe ser una lista
        Esta funcion retorna el valor entero de una mano dada
        '''
        if type(mano) != list:                                                              # Si la mano no es de tipo list entonces da error.
            return "Error 02"
        
        suma_cartas = sum(valor_carta(carta) for carta in mano)                             # Se suman los valores de las cartas en el mazo para sacar el valor total de la mano.
        
        numero_as = len([carta for carta in mano if carta[0] == "as"])                      # Se cuentan cuantos as hay en la mano para poder calcular su valor.
                                                                                            # Esto se hace mediante sacar el length de la lista con los as de la mano.
                                                                                            
        while numero_as > 0:                                                                # Mientras se tenga al menos un as, se entra en este ciclo.
            if suma_cartas > 21:                                                            # Si la suma total de las cartas seria mayor a 21 y se tiene un as, entonces el as vale 1, para esto se le resta 10.
                suma_cartas = suma_cartas - 10
                numero_as = numero_as - 1                                                   # Se le resta 1 a la cantidad de as hasta llegar a 0 para salir del while.
            else:
                break                                                                       # Si la suma de cartas no es mayor a 21, hace break.
        
        return suma_cartas                                                                  # Se retorna el valor de la suma total de las cartas de la mano dada.
    
    def repetir():
        '''
        Entrada: Ninguna
        Salida: Pregunta si se quiere seguir a la siguiente tirada o volver al centro de entretenimiento
        Restricciones: Ninguna
        Esta funcion repite la tirada hasta que el jugador decida parar
        '''
        while True:                                                                         # Esta funcion pregunta si se desea hacer otra tirada o volver al centro de entrenimiento y lo repite hasta que se escriba S o N.
            respuesta = input("\nQuiere proceder a la siguiente tirada? Escriba S para seguir, y N para volver al centro de entretenimiento.\n")
    
            if respuesta == "S" or respuesta == "s":                                        #  Si se escribe S entonces se hace otra tirada.
                print("\nReiniciando el juego...\n")
                return juego_21()
            elif respuesta == "N" or respuesta == "n":                                      # Si se escribe N entonces se devuelve al menu de entrada.
                print("\nGracias por jugar! Devolviendose al centro de enterenimiento...\n")
                return menu_entrada()
        
    def ganador_humano():                                                                   # Esta funcion dice que el jugador humano es el que ha ganado, y luego llama la funcion repetir.
        '''
        Entrada: Ninguna
        Salida: Dice que el jugador humano ha ganado y luego  repite la tirada
        Restricciones: Ninguna
        Esta funcion dice que ha ganado el humano y luego retorna la funcion de repeticion
        '''
        print("\nEl ganador es el jugador humano!\n")
        return repetir()
        
    def ganador_computadora():                                                              # Esta funcion dice que el jugador CPU es el que ha ganado y luego llama la funcion repetir.
        '''
        Entrada: Ninguna
        Salida: Dice que el jugador computadora ha ganado y luego repite la tirada
        Restricciones: Ninguna
        Esta funcion dice que ha ganado la computadora y luego retorna la funcion de repeticion
        '''
        print("\nEl ganador es la computadora!\n")
        return repetir()
        
    def empate():                                                                           # Esta funcion dice que hubo un empate entre ambos jugadores y luego llama la funcion repetir.
        '''
        Entrada: Ninguna
        Salida: Dice que la tirada fue un empate y luego repite la tirada
        Restricciones: Ninguna
        Esta funcion dice que la tirada fue un empate, luego retorna la funcion de repetir tiradas
        '''
        print("\nHay un empate entre ambos!\n")
        return repetir()
    
    def ambos_perdieron():                                                                  # Esta funcion dice que ambos jugadores perdieron ya que tuvieron un puntaje mayor a 21 y luego llama la funcion repetir.
        '''
        Entrada: Ninguna
        Salida: Dice que ambos jugadores perdieron y luego repite la tirada
        Restriccione: Ninguna
        Esta funcion dice que ambos jugadores perdieron la tirada, luego retorna la funcion de repetir tiradas
        '''
        print("\nNadie gano porque ambos tienen mas de 21!\n")
        return repetir()
        
    def decir_puntajes():                                                                   # Esta funcion dice los puntajes de ambos jugadores y sus manos al final mediante convertirlos en strings.
        '''
        Entrada: Ninguna
        Salida: Dice los puntajes de ambos jugadores
        Restricciones: Ninguna
        Esta funcion printea los puntajes al convertirlos en string y luego printea las manos completas de ambos jugadores
        '''
        print("\nEl puntaje total sumado de las cartas de la computadora es: " + str(puntaje_computadora))                  # Convierte el puntaje del CPU en un string y lo printea junto con su mano.
        print("Ya que su mano completa incluyendo la carta boca abajo era: ")
        print((mano_computadora))                                                                                           # Aqui hay un print en vez de un return porque no quiero que se retorne todavia.
    
        print("\nEl puntaje total sumado de las cartas del jugador humano es: " + str(puntaje_humano))                      # Convierte el puntaje del humano en un string y lo printea junto con su mano.
        print("Ya que su mano completa incluyendo la carta boca abajo era: ")
        return(mano_humano)                                                                                                 # Aca hay un return para que ya se retorne luego de decir el puntaje y mano del humano.
    
    # Aqui se definen todas las variables que se usaran luego para determinar las prioridades de ganador.
    indice = 0
    largo_computadora = len(mano_computadora)
    largo_humano = len(mano_humano)
    
    print("\nIniciando la tirada!\n")                                                                                 # Se inicia la tirada.
    
    input("\nPresione ENTER para continuar.\n")
    
    
    perfil_escogido = random.randint(1,4)                                                                             # Se escoge el numero de perfil que usara la computadora al azar por medio de randint, y se printea.
    print("\nEl perfil escogido fue el perfil: " + str(perfil_escogido))
    print("\n")
    input("\nPresione ENTER para continuar.\n")
    
    input("\nSe le repartió una carta boca abajo a la computadora. Presione ENTER para continuar el juego.\n")        # Se reparten las cartas boca abajo al CPU y al humano.
    
    input("\nSe le repartió una carta boca abajo al jugador humano. Presione ENTER para continuar el juego.\n")
    
    input("\nLa carta boca arriba dada al jugador computadora es: " + str((mano_computadora)[1]) + ". Presione ENTER para continuar el juego.\n")   # Se reparte la carta boca arriba al CPU y se printea cual es.
    
    input("\nLa carta boca arriba dada al jugador humano es: " + str((mano_humano)[1]) + ". Presione ENTER para continuar el juego.\n")             # Se reparte la carta boca arriba al humano y se printea cual es.
    
    input("\nEs el turno de la computadora. Presione ENTER para continuar el juego.\n")
    
    puntaje_humano = valor_mano(mano_humano)                                                            # Para facilitar la comprension, se define la variable puntaje_jugador como el valor de la mano del jugador.
    
    puntaje_computadora = valor_mano(mano_computadora)                                                  # Para facilitar la comprension se define la variable puntaje_computadora como el valor de la mano de la computadora.
    
    
    # Se printea la mano de la computadora aparte de la carta boca abajo. Para no mostrar la carta boca abajo, se empieza desde el segundo elemento, ya que el primer elemento es la carta boca abajo.
    print("La computadora tiene, sin contar la carta boca abajo, la mano: " + str(mano_computadora[1:]))
    
    
    # Dependiendo del numero al azar que se escogio con perfil_escogido, el jugador computadora escoge uno de cuatro perfiles que determinan su manera de jugar dependiendo del rango inferior y superior.
    
    if perfil_escogido == 1:                                                    # Perfil 1.
        if puntaje_humano >= 0 and puntaje_humano <= 18:                        # Solicitud obligatoria de carta.
            print("\nPerfil 1 siendo usado.\n")
            nueva_carta_computadora = mazo.pop()                                # Saca una carta nueva mediante hacerle pop al mazo para sacar el ultimo elemento de este y lo agrega a la mano con append.
            mano_computadora.append(nueva_carta_computadora)
            print ("La computadora saca " + str(nueva_carta_computadora))
    
        elif puntaje_humano >= 19 and puntaje_humano <= 20:                     # Solicitud condicional de carta.
            print("\nPerfil 1 siendo usado.\n")
            num_aleatorio = random.randint(0,1)
            if num_aleatorio == 1:                                              # Solicita una carta adicional si al generar un numero aleatorio entre 0 y 1, sale un 1. Si sale 0, pasa el turno.
                nueva_carta_computadora = mazo.pop()
                mano_computadora.append(nueva_carta_computadora)
                print ("La computadora saca " + str(nueva_carta_computadora))
            else:
                print("\nLa computadora pasa el turno.\n")
    
        elif puntaje_humano == 21:                                              # No solicitar carta y pasar el turno.
            print("\nPerfil 1 siendo usado.\n")
            print("\nLa computadora pasa el turno.\n")
    
    
    elif perfil_escogido == 2:                                                  # Pefil 2.
        if puntaje_humano >= 0 and puntaje_humano <= 15:                        # Solicitud obligatoria de carta.
            print("\nPerfil 2 siendo usado.\n")
            nueva_carta_computadora = mazo.pop()
            mano_computadora.append(nueva_carta_computadora)
            print ("La computadora saca " + str(nueva_carta_computadora))
    
        elif puntaje_humano >= 16 and puntaje_humano <= 21:                     # No solicitar carta y pasar el turno.
            print("\nPerfil 2 siendo usado.\n")
            print("\nLa computadora pasa el turno.\n")
    
    
    elif perfil_escogido == 3:                                                  # Perfil 3.
        if puntaje_humano >= 0 and puntaje_humano <= 15:                        # Solicitud obligatoria de carta.
            print("\nPerfil 3 siendo usado.\n")
            nueva_carta_computadora = mazo.pop()                                # Se saca una carta del mazo, y la que se saca se le da a la mano de la computadora.
            mano_computadora.append(nueva_carta_computadora)
            print ("La computadora saca " + str(nueva_carta_computadora))
    
        elif puntaje_humano >= 16 and puntaje_humano <= 19:                     # Solicitud condicional de carta.
            print("\nPerfil 3 siendo usado.\n")
            num_aleatorio = random.randint(0,1)
            if num_aleatorio == 1:
                nueva_carta_computadora = mazo.pop()
                mano_computadora.append(nueva_carta_computadora)
                print ("La computadora saca " + str(nueva_carta_computadora))
            else:
                print("\nLa computadora pasa el turno.\n")
    
        elif puntaje_humano >= 20 and puntaje_humano <= 21:                     # No solicitar carta y pasar el turno.
            print("\nPerfil 3 siendo usado.\n")
            print("\nLa computadora pasa el turno.\n")
    
    
    
    elif perfil_escogido == 4:                                                  # Perfil 4.
        if puntaje_humano >= 0 and puntaje_humano <= 21:                        # No solicitar carta y pasar el turno.
            print("\nPerfil 4 siendo usado.\n")
            print("\nLa computadora pasa el turno.\n")
    
    puntaje_computadora = valor_mano(mano_computadora)                          # Se actualiza el puntaje de la computadora.
    
    humano_adentro = True                                                      # El jugador ahora esta adentro ya que se acabo el turno de la computadora.
    
    input("\nEs el turno del jugador humano. Presione ENTER para continuar el juego.\n")
    
    while humano_adentro:                                                      # Aqui ocurre el turno del jugador humano, donde puede sacar cartas o pasar el turno.
        
        # Se printea la mano del jugador humano aparte de la carta boca abajo. Para no mostrar la carta boca abajo, se empieza desde el segundo elemento, ya que el primer elemento es la carta boca abajo.
        print("El jugador humano tiene, sin contar la carta boca abajo, la mano: " + str(mano_humano[1:]))
        
        if valor_mano(mano_humano) > 21:                                       # Si la mano del jugador humano es mas de 21 no se le pregunta si quiere jugar o quedarse.
            break
        
        if humano_adentro:
            respuesta = input("\nDesea sacar una carta o pasar el turno? Escriba su opcion deseada:\n1. Sacar carta.\n2. Pasar el turno.\n\n") # Se le pregunta al jugador humano si desea sacar una carta o pasar el turno.
            
            if respuesta == "1":                                                                                                               # Si el jugador humano decide jugar se le da otra carta.
                humano_adentro = True
                nueva_carta_humano = mazo.pop()
                mano_humano.append(nueva_carta_humano)
                print ("Ha sacado: " + str(nueva_carta_humano))
                
            elif respuesta == "2":                                                                 # Si decide pasar el turno entonces se acaba el turno del jugador humano.
                humano_adentro = False                                                             # Se hace False a jugador_adentro para salir del while.

    puntaje_humano = valor_mano(mano_humano)                                                       # Se actualizan los puntajes del humano y de la computadora.
    puntaje_computadora = valor_mano(mano_computadora)
    
    print(decir_puntajes())                                                                        # Printea los puntajes y luego los compara con las prioridades para determinar quien gano.
    
    if puntaje_humano == puntaje_computadora:                                                      # Si el humano y la computadora tienen el mismo puntaje, hubo un empate.
        return empate()
    
    elif puntaje_humano > 21 and puntaje_computadora > 21:                                         # Si el puntaje del humano y el de la computadora se pasó de 21, entonces ambos perdieron.
        return ambos_perdieron()
    
    
    if puntaje_humano == 21 and mano_humano[indice][0] == 7:                                       # Prioridad 6 Humano: Revisa si hay Triple 7, es decir 21 con tres sietes del mismo palo, para el humano.
        while indice < largo_humano:
            if mano_humano[indice][0] == 7:                                                        # Si detecta 21 puntos y un siete en la mano, y toda la mano es igual, entonces se saco 21 con tres sietes.
                if mano_humano[0] == mano_humano[1] == mano_humano[2]:
                    print("\nEl jugador humano tiene Triple 7!\n")
                    return ganador_humano()
            indice = indice + 1
        indice = 0
        largo_humano = len(mano_humano)
    
    
    if puntaje_computadora == 21 and mano_computadora[indice][0] == 7:                             # Prioridad 6 Computadora: Revisa si hay Triple 7, es decir 21 con tres sietes del mismo palo, para la computadora.
        while indice < largo_computadora:
            if mano_computadora[indice][0] == 7:
                if mano_computadora[0] == mano_computadora[1] == mano_computadora[2]:
                    print("\nEl jugador computadora tiene Triple 7!\n")
                    return ganador_computadora()
            indice = indice + 1
        indice = 0
        largo_computadora = len(mano_computadora)
    
    
    if mano_humano[0][0] == "as" and mano_humano[1][0] == "as":                                   # Prioridad 5 Humano: Revisa si hay doble as, es decir dos ases de cualquier palo, en la mano del humano.
        print("\nEl jugador humano tiene Doble As!\n")
        return ganador_humano()
    
    
    if mano_computadora[0][0] == "as" and mano_computadora[1][0] == "as":                         # Prioridad 5 Computadora: Revisa si hay doble as, es decir dos ases de cualquier palo, en la mano de la computadora.
        print("\nEl jugador computadora tiene Doble As!\n")
        return ganador_computadora()
    
    
    if mano_humano[0] == [5,"rombos"]:                                                            # Prioridad 4 Humano: Revisa si el humano recibio un 5 de rombos como primera carta de su mano.
        print("\nEl jugador humano tiene 5 de rombos como primera carta de su mano!\n")
        return ganador_humano()
    
    
    if mano_computadora[0] == [5,"rombos"]:                                                       # Prioridad 4 Computadora: Revisa si la computadora recibio un 5 de rombos como primera carta de su mano.
        print("\nEl jugador computadora tiene 5 de rombos como primera carta de su mano!\n")
        return ganador_computadora()
    
    
    # Prioridad 3 Humano: Revisa si el jugador tiene 5 menores, es decir, 5 cartas todas de valor inferior a 10.
    if len(mano_humano) == 5 and type(mano_humano[0][0]) == type(mano_humano[1][0]) == type(mano_humano[2][0]) == type(mano_humano[3][0]) == type(mano_humano[4][0]) and type(mano_humano[0][0]) == int:
        if mano_humano[0][0] < 10 and mano_humano[1][0] < 10 and mano_humano[2][0] < 10 and mano_humano[3][0] < 10 and mano_humano[4][0] < 10:
            print("\nEl jugador humano tiene 5 menores con valor inferior a 10!\n")
            return ganador_humano()
    
    # Prioridad 3 Computadora: Revisa si la computadora tiene 5 menores, es decir, 5 cartas todas de valor inferior a 10.
    if len(mano_computadora) == 5 and type(mano_computadora[0][0]) == type(mano_computadora[1][0]) == type(mano_computadora[2][0]) == type(mano_computadora[3][0]) == type(mano_computadora[4][0]) and type(mano_computadora[0][0]) == int:
        if mano_computadora[0][0] < 10 and mano_computadora[1][0] < 10 and mano_computadora[2][0] < 10 and mano_computadora[3][0] < 10 and mano_computadora[4][0] < 10:
            print("\nEl jugador computadora tiene 5 menores con valor inferior a 10!\n")
            return ganador_computadora()
            
            
    # Prioridad 2 Humano: Revisa si el jugador humano tiene 21 Duro, es decir, si tiene 21 puntos con una figura y un as.
    if puntaje_humano == 21 and mano_humano[0][0] == "jota" or mano_humano[0][0] == "rey" or mano_humano[0][0] == "reina":          # Si detecta una figura como primera carta y un as de segunda, saco 21 Duro.
        if mano_humano[1][0] == "as":
            print("\nEl jugador humano tiene 21 Duro!\n")
            return ganador_humano()
    if puntaje_humano == 21 and mano_humano[0][0] == "as":
        if mano_humano[1][0] == "jota" or mano_humano[1][0] == "rey" or mano_humano[1][0] == "reina":                               # Si detecta un as como primera carta y una figura de segunda, saco 21 Duro.
            print("\nEl jugador humano tiene 21 Duro!\n")
            return ganador_humano()
    
    # Prioridad 2 Computadora: Revisa si la computadora tiene 21 Duro, es decir, si tiene 21 puntos con una figura y un as.
    if puntaje_computadora == 21 and mano_computadora[0][0] == "jota" or mano_computadora[0][0] == "rey" or mano_computadora[0][0] == "reina":
        if mano_computadora[1][0] == "as":
            print("\nEl jugador computadora tiene 21 Duro!\n")
            return ganador_computadora()
    if puntaje_computadora == 21 and mano_computadora[0][0] == "as":
        if mano_computadora[1][0] == "jota" or mano_computadora[0][0] == "rey" or mano_computadora[0][0] == "reina":
            print("\nEl jugador computadora tiene 21 Duro!\n")
            return ganador_computadora()
    
    
    if puntaje_humano == 21:                                                     # Prioridad 1 Humano: Revisa si el humano tiene 21 Suave, es decir, si tiene 21 puntos con cualquier combinacion de cartas.
        print("\nEl jugador tiene un 21 Suave!\n")
        return ganador_humano()
        
    
    if puntaje_computadora == 21:                                                 # Prioridad 1 Computadora: Revisa si la computadora tiene 21 Suave, es decir, si tiene 21 puntos con cualquier combinacion de cartas.
        print("\nEl jugador computadora tiene 21 Suave!\n")
        return ganador_computadora()
    
    
    # Estas ultimas ya no son parte de las prioridades de ganador establecidas en las especificaciones del proyecto.
    
    if puntaje_humano > 21:                                                      # Estas dos condiciones establecen que si un jugador se pasa de los 21 puntos, el otro jugador gana la partida.
        print("\nEl jugador humano se pasó de los 21 puntos...\n")
        return ganador_computadora()
        
    if puntaje_computadora > 21:
        print("\nEl jugador computadora se pasó de los 21 puntos...\n")
        return ganador_humano()
    
    
    
    if puntaje_humano > puntaje_computadora and puntaje_humano < 21:           # Estas ultimas dos condiciones establecen que si nadie llega a 21 puntos, el que tuvo mas puntos gana la partida.
        print("\nNo se llegó a 21, pero gana el jugador humano ya que tuvo un valor de mano mas alto que la computadora.\n")
        return ganador_humano()
        
    if puntaje_humano < puntaje_computadora and puntaje_computadora < 21:
        print("\nNo se llegó a 21, pero gana la computadora ya que tuvo un valor de mano mas alto que el jugador humano.\n")
        return ganador_computadora()
    
def menu_entrada():
    '''
    Entrada: Ninguna
    Salida: El menu de entrada del centro de entretenimiento
    Restricciones: Ninguna
    Esta funcion hace display al menu de entrada del centro de entretinimiento y permite ver las instrucciones y acceder a los dos juegos
    '''
    
    # Se  le hace display al arte ASCII y se muestra el menu de entrada con las opciones que el jugador puede escoger
    print('''
   _____           _                   _                   _            _             _           _            _        
  / ____|         | |                 | |                 | |          | |           (_)         (_)          | |       
 | |     ___ _ __ | |_ _ __ ___     __| | ___    ___ _ __ | |_ _ __ ___| |_ ___ _ __  _ _ __ ___  _  ___ _ __ | |_ ___  
 | |    / _ \ '_ \| __| '__/ _ \   / _` |/ _ \  / _ \ '_ \| __| '__/ _ \ __/ _ \ '_ \| | '_ ` _ \| |/ _ \ '_ \| __/ _ \ 
 | |___|  __/ | | | |_| | | (_) | | (_| |  __/ |  __/ | | | |_| | |  __/ ||  __/ | | | | | | | | | |  __/ | | | || (_) |
  \_____\___|_| |_|\__|_|  \___/   \__,_|\___|  \___|_| |_|\__|_|  \___|\__\___|_| |_|_|_| |_| |_|_|\___|_| |_|\__\___/ 
''')
    respuesta=input('''\nBienvenido al centro de entretinimiento! \n\nPor favor digite el numero de la opcion que desea:
\n1. Instrucciones de Gato\n2. Instrucciones de 21\n3. Jugar Gato\n4. Jugar 21\n5. Salir del juego\n''')

    if respuesta == "1":                                                                                                  # Se dan las instrucciones de Gato al escoger la opcion 1
        print('''\n-Este juego de Gato será un 1v1 contra el computador.
-El tablero será representado por el número que debe digitar para escribir su símbolo en esa posición.
-El primer jugador en tener una línea en diagonal o recta de sus símbolos, ya sean X o O, gana.
-Si hace trampa mediante poner su símbolo sobre el símbolo del otro jugador, usted perderá automáticamente.
-Al inicio del juego se le pedirá que escoja el tamaño del tablero.
\nVolviendo al menu de entrada...''')
        return menu_entrada()

    elif respuesta == "2":                                                                                               # Se dan las instrucciones de 21 al escoger la opcion  2
        print('''\n-21 es un juego de cartas que consiste en obtener 21 puntos mediante la suma de los valores de las cartas.
-Las cartas numéricas representan su valor, las figuras valen 10 y el As es un 11 o un 1 según como convenga al jugador.
-Este juego también será un 1v1 contra la computadora. 
-Se gana una partida cuando se alcanza 21 puntos de diferentes maneras, se recibe un 5 de rombos como primera carta de su mano, u obtiene dos ases de cualquier palo, o cuando se tiene más puntos sumados que su rival.
\nVolviendo al menu de entrada...''')
        return menu_entrada()

    elif respuesta == "3":                                                                                               # Llama la funcion que carga el juego Gato al escoger la opcion 3
        return juego_gato()

    elif respuesta == "4":                                                                                               # Llama la funcion que carga el juego 21 al escoger la opcion 4
        return juego_21()
    
    elif respuesta == "5":                                                                                               # Se sale del menu de entrada al escoger la opcion 5
        print("\nSaliendo del menu de entrada...")
        raise SystemExit
    
    elif respuesta != "1" or respuesta != "2" or respuesta != "3" or respuesta != "4" or respuesta != "5":               # Si la respuesta dada por el jugador no esta dentro de las opciones, pide otra respuesta
        print("\nPor favor digite un numero que esté en las opciones posibles.")
        menu_entrada()
        
menu_entrada()


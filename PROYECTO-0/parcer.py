"""
Reglas:
DEFINICIONES

1) Una definición variable empieza con defVar, seguido de un nombre y un valor inicial
defVar nombre 1
2) Una definicion procedimental empieza con defProc, seguido de un nombre, seguida de una lista de parametros
entre parentesis separado por comas, seguido de un bloque de comandos
defProc [x,y,z]
    .
    .
    .
BLOQUE DE COMANDOS
3)es una secuencia de comandos separados por semicolons ";", entremedio de y corchetes {}
VALORES
4) un valor es un numero (int/float) o una variable previamente definida
COMANDOS
5) Puede ser un comando simple/una estructura de control/una llamada de procedimiento
    COMANDO SIMPLE
    6) Una asignación de la forma variable = valor. El resultado de esta instruccion es asignar un valor 
    a la variable
    7) jump(x,y) ---> x,y son valores (el robot salta a x,y)
    8) walk(v) ----> v es un valor (el robo se debe mover v pasos al frente)
    9) walk(v,D)---> v es un valor, D es una direccion (alfrente,derecha,izquierda,atras)
    10) walk(v, 0) ----> v es un valor. 0 es norte, sur, oeste ó este. (El robot mira hacia la coordenada O
    y se mueve v pasos)
    11) leap(v) --> v es un valor, (robot debe saltar v pasos)
    12) leap(v, D)
    13) leap(v, O)
    14)turn(D) – where D can be left, right, or around. The robot should turn 90
    degrees in the direction of the parameter.
    15)turnto(O) – where O can be north, south, east or west. The robot should
    turn so that it ends up facing direction O.
    16)drop(v) – where v is a value. The robot should drop v chips.
    17)get(v) – where v is a value. The robot should pickup v chips.
    18)grab(v) – where v is a value. The robot should pick v balloons.
    19)letGo(v) – where v is a value. The robot put v balloons.
    20)nop() The robot does not do anything.
21) un procedimiento es invocado usando el nombre del procedimiento, seguido de su argumento 
entre parentesis separado por commas
22)
    ESTRUCTURA DE CONTROL
    22)Conditional: if condition Block1 else Block2 – Executes Block1 if condition
    is true and Block2 if condition is false.
    23)Loop: while condition Block – Executes Block while condition is true.
    24)RepeatTimes: repeat v times Block – Executes Block n times, where v is

A condition can be:
24)facing(O) – where O is one of: north, south, east, or west
26) can(C) – where C is a simple command. This condition is true when the
simple command can be executed without error.
27)not: cond – where cond is a condition

"""
import lexer

cadena_lexer, diccionario_completo = lexer.leer_archivo()

def comandos():
    dicc = {
    "JUMP":"JUMP",
       "WALK": "WALK",
       "LEAP": "LEAP",
       "TURN": "TURN",
       "TURNTO": "TURNTO",
       "DROP": "DROP",
       "GET": "GET",
       "GRAB" : "GRAB",
       "LETGO":"LETGO",
       "NOP": "NOP"}
    return dicc

valores_iniciales = ["0","1","2","3","4","5","6","7","8"]
def recorrerArchivo(archivo):
    doc_completo = []
    variables_definidas = []
    with open(archivo, 'r') as archivo:
    # Itera a través de las líneas del archivo
        for linea in archivo:
            linea.lower()
            if linea != "":
                doc_completo.append(linea)
            correcto = True
            valores = linea.split(" ")
            cant_partes = len(valores)
            if valores[0] == "defvar":
                variables_definidas.append(valores[1])
                if cant_partes > 4 or cant_partes <3:
                    correcto == False
                else:
                    if valores[2] not in valores_iniciales:
                        correcto == False
                
            if valores[0] == "defproc":
                if cant_partes < 3:
                    correcto==False
                else:
                    if ("(" not in valores[1] or "(" not in valores[2]):
                        correcto == False
                    if ")" not in valores[cant_partes-1]:
                        correcto == False
                    if ")" not in (valores[cant_partes-1])[len(valores[cant_partes-1])-1]:
                        correcto==False


    for i in range(0,len(doc_completo)):
        una_linea = doc_completo[i]
        valores = una_linea.split(" ")
        comandos = comandos()
        if "{" in una_linea:
            nueva_linea = doc_completo[i+1]
            for comando in comandos():
                if comando in nueva_linea:
                    largo_comando = len(comando)
            

def isValue(caracter:str, variables_def):
    centinela = True
    try:
        if ("." in caracter) or ("," in caracter):
            float(caracter)
        else:
            int(caracter)
    except:
        centinela = False
        if caracter in variables_def:
            centinela = True
        
    return centinela

print(isValue("a", ["b","si","a"]))


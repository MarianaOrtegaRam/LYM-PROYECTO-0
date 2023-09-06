
# -*- coding: utf-8 -*-
def crear_diccionario()-> dict:
    diccionario={
       "(": "PARENTESISABIERTO",
       ")": "PARENTESISCERRADO",
       ";": "SEMICOLON",
       ",": "COMMA",
       ":":"dospuntos",
       "{": "LLAVECURVAABIERTA",
       "}": "LLAVECURVACERRADA",
       #PALABRAS RESERVADAS
       "defvar" : "DECLVAR",
       "defproc": "PROCEDIMIENTOS",
       'if'       : 'IF',
       'else'     : 'ELSE',
       'while'    : 'WHILE',
       "repeat"   : "REPEAT",
       "times"    :"TIMES",
       #COMANDO SIMPLE
       "jump":"JUMP",
       "walk": "WALK",
       "leap": "LEAP",
       "turn": "TURN",
       "turnto": "TURNTO",
       "drop": "DROP",
       "get": "GET",
       "grab" : "GRAB",
       "letgo":"LETGO",
       "nop": "NOP",
       "left": "IZQUIERDA",
       "right": "DERECHA",
       "front": "ADELANTE",
       "back": "ATRAS",
       "west": "OESTE",
       "south": "SUR",
       "north": "NORTE",
       "south": "SUR",
       "east": "ESTE",
       "around":"AROUND",
       #CONDICIONES
       "facing": "FACING",
       "can": "CAN",
       "not":"NOT"        
        }    
    return diccionario
def otroDic()-> dict:
    diccionario={

    }
    return diccionario

def crear_lista():
    lista = [
        "{","","(",")",";",", "," ", ",","\n"]
    return lista

def listanumeros():
    lista = [
        "1","2","3","4","5","6","7","8","9","0"]
    return lista

def leer_archivo(ruta)->None:
    archivo = open(ruta)
    lexer =""
    palabracreada = ""
    lista = crear_lista()
    listanum = listanumeros()
    diccionario = crear_diccionario()
    diccionario2 = otroDic()
    lastword =""
    diccionariofunciones = {}
    temporal = "."
    for linea in archivo :
        linea = " " + linea + " " 
    
    
        for letra in linea :
                    
            if(letra in lista) or (letra in listanum):
                palabracreada = palabracreada.lower()
                if ((letra == "{") and((lastword == "PROCEDIMIENTOS") or (lastword == "LLAVECURVACERRADA"))) or (palabracreada in diccionariofunciones):
                        
                    if palabracreada != "":
                        lexer = lexer + " " + palabracreada
                        diccionario2[palabracreada] = palabracreada
                        diccionario[palabracreada] = palabracreada
                        palabracreada = ""
                    if letra == "{":
                        lexer = lexer + " " + diccionario[letra]
                        lastword = diccionario[letra]
                    
                    
                    
                elif (palabracreada in diccionario) or (letra in diccionario) or (letra in listanum):
                    
                    if(palabracreada in diccionario):   
                        if (palabracreada == "defvar") or (palabracreada == "defproc"):
                            temporal = "variable"
                        


                        


                        lexer = lexer + " " + diccionario[palabracreada] 
                        lastword = diccionario[palabracreada]
                    elif(palabracreada != ""):
                            if(palabracreada in listanum):
                                lexer = lexer + " " + "INT"
                                lastword = "INT"
                            else:   
                                if(temporal == "variable"):
                                    if letra == "(" and palabracreada not in diccionario and lastword == "PROCEDIMIENTOS":
                                        diccionario[palabracreada] = palabracreada 
                                        lexer = lexer + " " + palabracreada
                                    else:
                                        diccionario["var-" + palabracreada] = "var-" + palabracreada
                                        lexer = lexer + " " + "var"
                                        lastword = "var"
                                elif("var-"+palabracreada) in diccionario :
                                    lexer = lexer + " " + "var"
                                    lastword = "var"
                                else:
                                    lexer = lexer + " " + "ERROR"
                                    lastword = "var"


                    if letra in listanum:
                        lexer = lexer + " " + "INT"
                        lastword = "INT"
                    
                    if letra in diccionario:
                        if letra == ";":
                            temporal =""
                        lexer = lexer + " " + diccionario[letra] 
                        lastword = diccionario[letra]
                        # hacer que escriba en un archivo lo que dice el lexer
                    
                    palabracreada = ""
            else:
            
                palabracreada = palabracreada + letra

    return lexer, diccionario
               

#prueba de lexer
#print(leer_archivo("programa.txt"))
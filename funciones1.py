import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
import random
def pausa():
    input("\tPresione una tecla para continuar")
def ya_hechos():
    pass
    limpiar();
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                                                             ║
    ║    ╔═══════╗            ╦                                                   ║
    ║    ║                    ║                                                   ║
    ║    ║                    ║                                                   ║
    ║    ║                    ║                                                   ║
    ║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗                         ║
    ║    ║            ║       ║    ║       ║    ║                                 ║
    ║    ║            ║       ║    ║       ║    ║          ╔╗                     ║
    ║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝                     ║
    ║                                                                             ║
    ║                                                                             ║
    ║                                                                             ║
    ║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
    ║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
    ║              ║    ║                ║       ║            ║       ║           ║
    ║              ║    ╚╗               ║       ║            ║       ║           ║
    ║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
    ║              ║           ╚╗        ║       ║            ║       ║           ║
    ║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
    ║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
    ║                                                                             ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    ║                                                                             ║
    ║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
    ║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
    ║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
    ║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
    ║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
    ║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
    ║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
    ║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    ''')
    pausa()
    limpiar()
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                                                             ║
    ║    ╔╗      ╔╗   ╔═════╗    ╔══════╗    ╦       ╦   ╦           ╔═════╗      ║
    ║    ║╚╗    ╔╝║  ╔╝     ╚╗   ║      ╚╗   ║       ║   ║          ╔╝     ╚╗     ║
    ║    ║ ╚╗  ╔╝ ║  ║       ║   ║       ║   ║       ║   ║          ║       ║     ║
    ║    ║  ╚╗╔╝  ║  ║       ║   ║       ║   ║       ║   ║          ║       ║     ║
    ║    ║   ╚╝   ║  ║       ║   ║       ║   ║       ║   ║          ║       ║     ║
    ║    ║        ║  ║       ║   ║       ║   ║       ║   ║          ║       ║     ║
    ║    ║        ║  ╚╗     ╔╝   ║      ╔╝   ╚╗     ╔╝   ║          ╚╗     ╔╝     ║
    ║    ╩        ╩   ╚═════╝    ╚══════╝     ╚═════╝    ╚═══════╝   ╚═════╝      ║
    ║                                                                             ║
    ║                                                                             ║
    ║                                                                             ║
    ║       ╔════╗                ╦                      ╔═╗       ╔═══╗          ║
    ║      ╔╝    ╚╗               ║                     ╔╝ ║      ╔╝   ╚╗         ║
    ║      ╚╗    ╔╝               ║     ╔═════╗            ║           ╔╝         ║
    ║       ╠════╣         ╔══════╣    ╔╝     ╚╗           ║          ╔╝          ║
    ║      ╔╝    ╚╗       ╔╝      ║    ║       ║           ║        ╔═╝           ║
    ║      ║      ║       ║       ║    ╠═══════╝           ║       ╔╝             ║
    ║      ╚╗    ╔╝       ╚╗      ║    ╚╗                  ║      ╔╝              ║
    ║       ╚════╝         ╚══════╝     ╚══════╝        ╚══╩══╝   ╚═════╝         ║
    ║                                                                             ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

    pausa()
    limpiar()
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║ ╔══════╗ ╦      ╦ ╔╗      ╦  ╔════╗  ╦  ╔════╗  ╔╗      ╦ ╔══════╗  ╔════╗  ║
    ║ ║        ║      ║ ║╚╗     ║ ╔╝    ╚╗ ║ ╔╝    ╚╗ ║╚╗     ║ ║        ╔╝    ╚╗ ║
    ║ ║        ║      ║ ║ ╚╗    ║ ║        ║ ║      ║ ║ ╚╗    ║ ║        ║        ║
    ║ ║        ║      ║ ║  ╚╗   ║ ║        ║ ║      ║ ║  ╚╗   ║ ║        ╚╗       ║
    ║ ╠════╗   ║      ║ ║   ╚╗  ║ ║        ║ ║      ║ ║   ╚╗  ║ ╠═════╝   ╚════╗  ║
    ║ ║        ║      ║ ║    ╚╗ ║ ║        ║ ║      ║ ║    ╚╗ ║ ║              ╚╗ ║
    ║ ║        ╚╗    ╔╝ ║     ╚╗║ ╚╗    ╔╝ ║ ╚╗    ╔╝ ║     ╚╗║ ║        ╚╗    ╔╝ ║
    ║ ╩         ╚════╝  ╩      ╚╝  ╚════╝  ╩  ╚════╝  ╩      ╚╝ ╚══════╝  ╚════╝  ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                              Funciones y Metodos                            ║
    ║                              -------------------                            ║
    ║          Funciones    Description                                           ║
    ║                   lambda                                                    ║
    ║                                                                             ║
    ║          Metodos son funciones dentro de clases donde se deberia instanciar ║
    ║                   a la clase con self nombre_objeto                         ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                                                             ║
    ║                              Funciones,  Metodos                            ║
    ║                                  y Generadores                              ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m\033[0;m
    """)




def ya_hechos2():
    pass
    def funcion_numero(info):
        if info.isdigit():
            info = int (info)
        else:
            print ("son caracteres")
        return (info)


    def suma_SIMPLE():
        DATO1 = input ("INGRESE EL PRIMER DATO:")
        DATO2 = input ("INGRESE EL SEGUNDO DATO:")
        DATO1 =  funcion_numero (DATO1)
        DATO2 =  funcion_numero (DATO2)
        RESULTADO = DATO1+DATO2
        print ( RESULTADO)
    suma_SIMPLE()


    pausa();limpiar();


    def suma_RETURN(DATO1,DATO2):
        RESULTADO = DATO1+DATO2
        return RESULTADO

    DATO1 = input ("INGRESE EL PRIMER DATO:")
    DATO2 = input ("INGRESE EL SEGUNDO DATO:")
    DATO1 =  funcion_numero (DATO1)
    DATO2 =  funcion_numero (DATO2)



    RESULTADO= suma_RETURN(DATO1,DATO2)
    print (RESULTADO)

    pausa();limpiar();







    def sumar(x,y):
       return x+y

    def restar(x,y):
       return x-y

    def operar(operacion,x,y):
       return operacion(x,y)
    x=9
    y=10
    print(operar(sumar,x,y))
    print(operar(restar,x,y))

def ya_hechos3():



    def funcion_0():
        # ~ objeto = 1
        print (f"objeto dentro de la funcion = {objeto}")
        # ~ objeto += 1# como no pasa como parámetro y no es global no se puede escribir, solo leer
        print (f"objeto dentro de la funcion = {objeto}")

    objeto = 123456789
    funcion_0()
    """
    #--------------------------------------------------------------
    """
    def funcion_parametro_entrada(objeto):
        # ~ objeto = 1
        print (f"objeto dentro de la funcion 1= {objeto}")
        objeto += 1
        print (f"objeto dentro de la funcion 2= {objeto}")

    objeto = 9
    print (f"objeto en el main antes de ir a la funcion= {objeto}")
    funcion_parametro_entrada(objeto)

    print (f"objeto en el main luego de ir a la funcion= {objeto}")

    #--------------------------------------------------------------


    def funcion_parametro_entrada_y_salida(objeto):
        # ~ objeto = 1
        print (f"objeto dentro de la funcion 1= {objeto}")
        objeto += 1
        print (f"objeto dentro de la funcion 2= {objeto}")
        return objeto
    objeto = 9
    print (f"objeto en el main antes de ir a la funcion= {objeto}")
    objeto = funcion_parametro_entrada_y_salida(objeto)

    print (f"objeto en el main luego de ir a la funcion= {objeto}")


    #--------------------------------------------------------------
    import random

    def calcular_promedios(nota_1, nota_2):
        resultado = (nota_1 + nota_2)/2
        return resultado


    nota_a= random.randint(0,10)
    nota_b= random.randint(0,10)
    regreso = calcular_promedios(nota_a,nota_b)
    print (f"el promedio de la nota {nota_a} y {nota_b} es {regreso} con parametros")


    #--------------------------------------------------------------
    import random

    def calcular_promedios():

        global nota_a
        global nota_b
        global regreso
        regreso = (nota_a + nota_b)/2

    regreso =0
    nota_a= random.randint(0,10)
    nota_b= random.randint(0,10)

    calcular_promedios()
    print (f"el promedio de la nota {nota_a} y {nota_b} es {regreso} como globales")

    #--------------------------------------------------------------

def ya_hecho4():#listas y tuplas
    pass
    import random

    def calcular_promedios(*notas):#argumento con index
        suma = 0
        lista_notas= []
        #lista_notas.extend(notas)
        for contador,cada_nota in enumerate (notas):
            lista_notas.appned(cada_nota)
            suma = suma + cada_nota

        resultado = (suma)/(contador+1)
        return resultado

    def calcular_promedios2(*notas):
        notas=list(notas)#busco los 0 y los cambio por 1
        suma = sum(notas)
        contador = len (notas)
        resultado = (suma)/contador
        #return resultado
        return sum(notas)/ len (notas)



    notas = [random.randint(0,10)  for cont in range (0,random.randint (2,7))]

    print (f"{notas=}")

    #😊

    print (f"el promedio de la notas {notas}  es {calcular_promedios(*notas)} con parametros")

    print (f"el promedio de la notas {notas}  es {calcular_promedios2(*notas)} con parametros")





def ya_hechos5():#diccionarios
    pass


    def calcular_promedios3(**notas):
        lista_notas=list(notas.values())
        suma = sum(lista_notas)
        contador = len (notas)
        resultado = (suma)/contador
        #return resultado
        return sum(lista_notas)/ len (notas)

    nombres = ("Alberto", "Bea","Carlos", "Daniela", "Ester")
    """
    solo_notas = [random.randint(0,10)  for nombre in nombres]
    notas = {}
    for cada_nombre, cada_nota in zip(nombres, solo_notas):
        notas [cada_nombre]=cada_nota
    """
    #-------------------------------------
    nombres = ("Alberto", "Bea","Carlos", "Daniela", "Ester")
    solo_notas = [random.randint(0,10)  for nombre in nombres]
    notas = {cada_nombre: cada_nota   for cada_nombre, cada_nota in zip(nombres, solo_notas)}
    #-------------------------------------
    notas = {cada_nombre: cada_nota   for cada_nombre, cada_nota in zip(("Alberto", "Bea","Carlos", "Daniela", "Ester"),  [random.randint(0,10)  for nombre in nombres])}
    #-------------------------------------
    cant = random.randint(0,1000)
    notas = {cada_nombre: cada_nota   for cada_nombre, cada_nota in zip([ f"alumno-{str(legajo).zfill(3)}"  for legajo in range (0,cant)],  [random.randint(1,10)  for cont in  range (0,cant)])}

    print (f"{notas=}")
    #😊
    for clave, valor in notas.items():
        print (f"clave {clave}   nota:{valor}")

    print (f"el promedio de la notas ({len(notas)}) es {round(calcular_promedios3(**notas),2)} con parametros")

def ya_hechos6():#argumento por default
    pass
    """
    parametros es el objeto por donde pasan datos (y su tipo)

    argumentos son los datos (y su tipo)


    hay perametros de entrada y de salida
    hay parametos de objetos estandar, de tuplas y diccionarios
    """


    def funcion_gracia (nombres,apellidos, titulo):
        gracia = titulo+". "+nombres+" "+apellidos
        print (f"{gracia=}")

    funcion_gracia ("Juan","Garcia", "Dr")

    funcion_gracia (apellidos="Serrat", titulo="Canta Autor", nombres="Juan Manuel")

    funcion_gracia (apellidos="Sabina", nombres="Joaquin" , titulo="Canta Autor")

    ################################################################

    def funcion_gracia (nombres,apellidos, titulo=""):
        gracia = titulo+". "+nombres+" "+apellidos
        print (f"{gracia=}")

    funcion_gracia ("Juan","Garcia", "Dr")

    funcion_gracia ("Juan","Garcia")

    funcion_gracia (apellidos="Serrat", nombres="Juan Manuel")

    funcion_gracia (apellidos="Sabina", nombres="Joaquin" , titulo="Canta Autor")



    ################################################################

    #desempaquetado

    def funcion_gracia (nombres,apellidos="xx", titulo=123):
        gracia = f"{titulo}. {nombres} {apellidos}"
        print (f"{gracia=}")

    funcion_gracia ("Juan","Garcia", "Dr")

    funcion_gracia ("Juan","Garcia")

    funcion_gracia (apellidos="Serrat", nombres="Juan Manuel")

    funcion_gracia (apellidos="Sabina", nombres="Joaquin" , titulo="Canta Autor")

    funcion_gracia ( nombres="Joaquin" , titulo="Canta Autor")

    funcion_gracia ( nombres="Joaquin" )

    funcion_gracia ( "Joaquin" )

def ya_hechos7(notas):
    pass
    def funcion_empaquetados(**notas):#desempaquetado argumento
        cant_a=0
        cant_d=0
        aprobados=[]
        desaprobados=[]
        for clave,valor in notas.items():
            if valor >= 6:
                cant_a+=1
                aprobados.append(clave)
            else:
                cant_d+=1
                desaprobados.append(clave)
        return cant_a, aprobados,cant_d, desaprobados

    nombres = ("Alberto", "Bea","Carlos", "Daniela", "Ester")
    solo_notas = [random.randint(0,10)  for nombre in nombres]
    notas = {cada_nombre: cada_nota   for cada_nombre, cada_nota in zip(nombres, solo_notas)}
    print (f"{notas=}")
    #paquete ==>>  cant_a, aprobados,cant_d, desaprobados
    """
    paquete = funcion_empaquetados(**notas)
    print (f"{paquete=}")

    #paquete=(4, ['Alberto', 'Bea', 'Carlos', 'Ester'], 1, ['Daniela'])

    aprobados_cantidad, aprobados_nombres, desaprobados_cantidad, desaprobados_nombres = paquete
    """
    aprobados_cantidad, aprobados_nombres, desaprobados_cantidad, desaprobados_nombres = funcion_empaquetados(**notas)
    print (f"los aprobados fueron {aprobados_nombres} cant ({aprobados_cantidad})")
    print (f"los desaprobados fueron {desaprobados_nombres} cant ({desaprobados_cantidad})")



    #desempaquetado

def ya_hechos8(pagos):
    pass

def funcion_pagos(**ingresos):
    dic={"elect":{"cantidad":0,
                "total":0
                },
         "tar":{"cantidad":0,
               "total":0
                },
        "efec":{"cantidad":0,
                "total":0
                }
        }
    for ticket ,valores in ingresos.items():
        for clave, valor in valores.items():
            print (clave, valor)
            if clave =="tipo":
                tipo_de_pago= valor
                continue
            if clave =="valor":
                monto= valor
            """
            tipo tar
            valor 382
            tipo efec
            valor 340
            tipo tar
            """



            """

            if tipo_de_pago=="elect":
                dic [tipo_de_pago]["cantidad"]+=1
                dic [tipo_de_pago]["total"]+=monto
            elif tipo_de_pago=="tar":
                dic [tipo_de_pago]["cantidad"]+=1
                dic [tipo_de_pago]["total"]+=monto
            elif tipo_de_pago=="efec":
                dic [tipo_de_pago]["cantidad"]+=1
                dic [tipo_de_pago]["total"]+=monto
            """
            dic [tipo_de_pago]["cantidad"]+=1
            dic [tipo_de_pago]["total"]+=monto
    return dic

cant = random.randint(0,100)
lista_tipos_pagos = ["tar","efec","elect"]

cada_pago_tipo = random.choice(lista_tipos_pagos)
cada_pago_gasto = random.randint(10,500)

dic_salida = { f"ticket_nro_{str(contador).zfill(4)}": {"tipo":random.choice(lista_tipos_pagos),"valor":random.randint(10,500)} for contador in range (1,cant ) }
dic_regreso = funcion_pagos(**dic_salida)
print (f"{dic_regreso=}")

exit()

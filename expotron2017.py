#!/usr/bin/env python
#-*- coding: utf-8 -*-
import  os
import sys
import sqlite3

print("\t\t\t\t--------")
print("\t\t\t\tEXPOTRON")
print("\t\t\t\t--------\n")

def menu():
    def nosotros():
        print("-----------------------")
        print("Que es el Expotron ?")
        print("-----------------------\n")
        print("El EXPOTRON es uno de los eventos de robótica más grandes a nivel nacional, que se encarga de fomentar la investigación y el desarrollo tecnológico en nuestro país. Este evento año tras año reúne a decenas de estudiantes de distintas parte del Perú y, para que en 3 días demuestren sus habilidades y destrezas en temas de robótica y automatización en los concursos.")
        input("Presione 'Enter'\\\\\\\\\\\\\\\\\\")
        print("-----------------------")
        print("Quienes somos ?")
        print("-----------------------\n")
        print("Este evento está organizado por la Rama Estudiantil IEEE-UNSA, y la Escuela Profesional de Ingeniería Electrónica (EPIE) de la Universidad Nacional de San Agustín.")
        input("Presione 'Enter'\\\\\\\\\\\\\\\\\\")
        print("-----------------------")
        print("Donde se realizara ?")
        print("-----------------------\n")
        print("Loza Deportiva de la Escuela Profesional de Ingeniería Electrónica")
        input("Presione 'Enter' para regresar al MENU \\\\\\\\\\\\\\\\\\")
        menu()
    def inscripcion():
        def feria():
            print("Llene los siguientes datos ...Para reservar su stand...")
            print("==================================")
            nempresa=input("Nombre de la empresa : ")
            nombref=input("Nombre :")
            apellidosf=input("Apellidos :")
            dnif=input("DNI : ")
            telefonof=input("Telefono :")
            correof=input("Correo electronico : ")
            descripcionf=input("Descripcion breve de que dara a conocer : ")

            # para llamar a base de datos de psqlite admin
            con=sqlite3.connect("expotrom.s3db")
            cursor=con.cursor()
            cursor.execute("insert into Feria (nempresa,nombref,apellidosf,dnif,telefonof,correof,descripcionf) values ('"+nempresa+"','"+nombref+"','"+apellidosf+"','"+dnif+"','"+telefonof+"','"+correof+"','"+descripcionf+"')")
            con.commit()
            con.close()

            input("UD. se registro con exito...")
            inscripcion()

        def taller():
            print("Llene los siguientes datos ...Para reservar su stand...")
            print("==================================")
            ntaller=input("Nombre del taller : ")
            nombreta=input("Nombre : ")
            apellidosta=input("Apellidos :")
            dnita=input("DNI : ")
            telefonota=input("Telefono :")
            correota=input("Correo electronico : ")
            descripcionta=input("Descripcion breve del taller : ")

            #llamando a base de datos

            con=sqlite3.connect("expotrom.s3db")
            cursor=con.cursor()
            cursor.execute("insert into Taller (ntaller,nombreta,apellidosta,dnita,telefonota,correota,descripcionta) values ('"+ntaller+"','"+nombreta+"','"+apellidosta+"','"+dnita+"','"+telefonota+"','"+correota+"','"+descripcionta+"')")
            con.commit()
            con.close()

            input("UD. se registro con exito...")
            inscripcion()

        def proyectos():
            print("Llene los siguientes datos ...Para exponer su proyecto...")
            print("==================================")
            nproyecto=input("Nombre del proyecto : ")
            nombrep=input("Nombre : ")
            apellidosp=input("Apellidos :")
            dnip=input("DNI : ")
            telefonop=input("Telefono :")
            correop=input("Correo electronico : ")
            descripcionp=input("Descripcion breve del proyecto : ")

            #llebando a base de datos
            con=sqlite3.connect("expotrom.s3db")
            cursor=con.cursor()
            cursor.execute("insert into Proyecto (nproyecto,nombrep,apellidosp,dnip,telefonop,correop,descripcionp) values ('"+nproyecto+"','"+nombrep+"','"+apellidosp+"','"+dnip+"','"+telefonop+"','"+correop+"','"+descripcionp+"')")
            con.commit()
            con.close()

            input("UD. se registro con exito...")
            inscripcion()

        def competencias():
            def segvel():
                print("Llene los siguientes datos ...Para inscribir su seguidor/velocista...")
                print("==================================")
                print("/t/tDatos del Participante ")
                print("==================================")
                nombres=input("Nombre : ")
                apellidoss=input("Apellidos :")
                dnis=input("DNI : ")
                telefonos=input("Telefono :")
                correos=input("Correo electronico : ")
                print("==================================")
                print("/t/tDatos del Seguidor/Velocista  ")
                print("==================================")
                nomsegvel=input("Nombre del S/V :")
                colorsegvel=input("Color del S/V :")
                materialsegvel=input("Material del S/V :")
                pesosegvel=input("Peso del S/V :")

                #agregando a base de datos
                con=sqlite3.connect("expotrom.s3db")
                cursor=con.cursor()
                cursor.execute("insert into segvel (nombres,apellidoss,dnis,telefonos,correos,nomsegvel,colorsegvel,materialsegvel,pesosegvel) values ('"+nombres+"','"+apellidoss+"','"+dnis+"','"+telefonos+"','"+correos+"','"+nomsegvel+"','"+colorsegvel+"','"+materialsegvel+"','"+pesosegvel+"')")
                con.commit()
                con.close()

                input("UD. se registro con exito ...")
                competencias()
            def minisumos():
                def medio():
                    print("Llene los siguientes datos ...Para exponer su minisumo...")
                    print("==================================")
                    print("/t/tDatos del Participante ")
                    print("==================================")
                    nombreme=input("Nombre : ")
                    apellidosme=input("Apellidos :")
                    dnime=input("DNI : ")
                    telefonome=input("Telefono :")
                    correome=input("Correo electronico : ")
                    print("==================================")
                    print("/t/tDatos del Seguidor/Velocista  ")
                    print("==================================")
                    nomsumo=input("Nombre del minisumo:")
                    colorsumo=input("Color del minisumo :")
                    matsumo=input("Material del minisumo :")
                    pesosumo=input("Peso del minisumo :")
                    #agregando a base de datos
                    con=sqlite3.connect("expotrom.s3db")
                    cursor=con.cursor()
                    cursor.execute("insert into medio (nombreme,apellidosme,dnime,telefonome,correome,nomsumo,colorsumo,matsumo,pesosumo) values ('"+nombreme+"','"+apellidosme+"','"+dnime+"','"+telefonome+"','"+correome+"','"+nomsumo+"','"+colorsumo+"','"+matsumo+"','"+pesosumo+"')")
                    con.commit()
                    con.close()

                    input("UD. se registro con exito ...")
                    minisumos()
                def tres():
                    print("Llene los siguientes datos ...Para inscribir su minisumo ...")
                    print("==================================")
                    print("/t/tDatos del Participante ")
                    print("==================================")
                    nomt=input("Nombre : ")
                    apellidost=input("Apellidos :")
                    dnit=input("DNI : ")
                    telefonot=input("Telefono :")
                    correot=input("Correo electronico : ")
                    print("==================================")
                    print("/t/tDatos del Seguidor/Velocista  ")
                    print("==================================")
                    nomsumot=input("Nombre del minisumo :")
                    colorsumot=input("Color del S/V :")
                    matsumot=input("Material del minisumo :")
                    pesosumot=input("Peso del minisumo :")

                    #llamando base de datos
                    con=sqlite3.connect("expotrom.s3db")
                    cursor=con.cursor()
                    cursor.execute("insert into tres (nomt,apellidost,dnit,telefonot,correot,nomsumot,colorsumot,matsumot,pesosumot) values ('"+nomt+"','"+apellidost+"','"+dnit+"','"+telefonot+"','"+correot+"','"+nomsumot+"','"+colorsumot+"','"+matsumot+"','"+pesosumot+"')")
                    con.commit()
                    con.close()

                    input("UD. se registro con exito ...")
                    minisumos()

                print("\n//////////CATEGORIAS///////////\n")
                print("-------------------------------")
                print("\t (1) 500 gr. ")
                print("-------------------------------")
                print("\t (2) 3 kgr. ")
                print("-------------------------------")
                print("\t (3) Volver al menu de competencias ")
                print("-------------------------------")
                deci=int(input("Digite una opcion del MENU DE COMPETENCIAS "))
                if deci==1:
                    medio()
                elif deci==2:
                    tres()
                elif deci==3:
                    input("Presione 'Enter' para regresar al menu")
                    competencias()
                else:
                    input("Digite una opcion valida ...")
                    minisumos()
            def mirosoft():
                print("Llene los siguientes datos ...Para inscribir su robot(misoft)...")
                print("==================================")
                print("/t/tDatos del Participante ")
                print("==================================")
                nombrem=input("Nombre : ")
                apellidosm=input("Apellidos :")
                dnim=input("DNI : ")
                telefonom=input("Telefono :")
                correom=input("Correo electronico : ")
                print("==================================")
                print("/t/tDatos del Mirosoft  ")
                print("==================================")
                nomsoft1=input("Nombre del mirosoft 1 :")
                nomsoft2=input("Nombre del mirosoft 2 :")
                colsoft=input("Color de los mirosofts  :")
                materialsoft=input("Material de los mirosofts :")
                pesosoft1=input("Peso del mirosoft 1 :")
                pesosoft2=input("Peso del mirosoft 2 :")

                #agregando a base de datos
                con=sqlite3.connect("expotrom.s3db")
                cursor=con.cursor()
                cursor.execute("inser into mirosoft (nombrem,apellidosm,dnim,telefonom,correom,nomsoft1,nomsoft2,colsoft,materialsoft,pesosoft1,pesosoft2) values ('"+nombrem+"','"+apellidosm+"','"+dnim+"','"+telefonom+"','"+correom+"','"+nomsoft1+"','"+nomsoft2+"','"+colsoft+"','"+materialsoft+"','"+pesosoft1+"','"+pesosoft2+"')")
                con.commit()
                con.close()

                input("UD. se registro con exito ...")
                competencias()
            print("\n//////////COMPETENCIAS///////////\n")
            print("-------------------------------")
            print("\t (1) Seguidores y Velocistas ")
            print("-------------------------------")
            print("\t (2) Minisumos ")
            print("-------------------------------")
            print("\t (3) Mirosoft ")
            print("-------------------------------")
            print("\t (4) Volver al MENU DE INSCRIPCIONES ")
            print("-------------------------------")
            opci=int(input("Digite una opcion del MENU DE COMPETENCIAS "))
            if opci==1:
                segvel()
            elif opci==2:
                minisumos()
            elif opci==3:
                mirosoft()
            elif opci==4:
                input("Presione 'Enter' para regresar al MENU DE INSCRIPCIONES")
                inscripcion()
            else:
                input("Digite una opcion valida ...")
                competencias()

        def warbots():
            print("Llene los siguientes datos ...Para inscribir su warbot...")
            print("==================================")
            print("/t/tDatos del Participante ")
            print("==================================")
            nombrew=input("Nombre : ")
            apellidosw=input("Apellidos :")
            dniw=input("DNI : ")
            telefonow=input("Telefono :")
            correow=input("Correo electronico : ")
            print("==================================")
            print("/t/tDatos del Warbot  ")
            print("==================================")
            nomw=input("Nombre del Warbot  :")
            matw=input("Material Warbot :")
            pesow=input("Peso del Warbot :")
            asistentes=input("Numero de Asistentes :")
            #agregando a base de datos
            con=sqlite3.connect("expotrom.s3db")
            cursor=con.cursor()
            cursor.execute("insert into Warbots (nombrew,apellidosw,dniw,telefonosw,correow,nomw,matw,pesow,asistentes) values ('"+nombrew+"','"+apellidosw+"','"+dniw+"','"+telefonow+"','"+correow+"','"+nomw+"','"+matw+"','"+pesow+"','"+asistentes+"')")
            con.commit()
            con.close()

            input("UD. se registro con exito ...")
            competencias()

        print("\n//////////INSCRIPCIONES ///////////\n")
        print("-------------------------------")
        print("\t (1) Feria de Tecnologia ")
        print("-------------------------------")
        print("\t (2) Talleres ")
        print("-------------------------------")
        print("\t (3) Proyectos ")
        print("-------------------------------")
        print("\t (4) Competencias ")
        print("-------------------------------")
        print("\t (5) WARBOTS ")
        print("-------------------------------")
        print("\t (6) Volver al MENU PRINCIPAL ")
        print("-------------------------------")
        opci=int(input("Digite una opcion del MENU DE INSCRIPCIONES... : "))
        if opci==1:
            feria()
        elif opci==2:
            taller()
        elif opci==3:
            proyectos()
        elif opci==4:
            competencias()
        elif opci==5:
            warbots()
        elif opci==6:
            input("Presione 'Enter' para regresar al MENU PRINCIPAL ")
            menu()
        else:
            input("Digite una opcion valida ...")
            inscripcion()
    def cronograma():

        def primero():
            print("--------------------------------------------------------------------------")
            print("(9:00-10:00)  |                      Inaguracion                         |")
            print("--------------------------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia |                 |                  |")
            print("--------------------------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia |  Larvic -UCSP   |  CARRERAS KIDS   |")
            print("--------------------------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |      YURA       | SEGUIDOR JUNIOR  |")
            print("--------------------------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |                 |   SCRATCH        |")
            print("--------------------------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |                 |   RECICLAJE      |")
            print("--------------------------------------------------------------------------")
            print("(15:00-16:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(16:00-17:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(17:00-18:00) |   Taller Arduino    |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("(18:00-19:00) |                     |                 |    Proyectos     |")
            print("--------------------------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def segundo():

            print("---------------------------------------------------------------------------------")
            print("(9:00-10:00)  |                                                                 |")
            print("---------------------------------------------------------------------------------")
            print("(10:00-11:00) | Taller de PLC  | Feria de Tecnologia |              | LEGO      |")
            print("---------------------------------------------------------------------------------")
            print("(11:00-12:00) | Taller de PLC  | Feria de Tecnologia | Tec Hunter   | LEGO      |")
            print("---------------------------------------------------------------------------------")
            print("(12:00-13:00) | Taller de PLC  | Feria de Tecnologia | Larvic UCSP  | SOCCER    |")
            print("---------------------------------------------------------------------------------")
            print("(13:00-14:00) | Taller de PLC  | Feria de Tecnologia |              | LIBRE     |")
            print("---------------------------------------------------------------------------------")
            print("(14:00-15:00) |                | Feria de Tecnologia | Eagle Diseño |           |")
            print("---------------------------------------------------------------------------------")
            print("(15:00-16:00) | Taller Arduino |        Taller       |   diseño     | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(16:00-17:00) | Taller Arduino |         de          |  de PCBs     | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(17:00-18:00) | Taller Arduino |      creacion de    |              | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("(18:00-19:00) |                |      videojuegos    |              | Proyectos |")
            print("---------------------------------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def tercero():
            print("--------------------------------------------------------------------")
            print("(9:00-10:00)  |                                                    |")
            print("--------------------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia |                | SEGUIDORES  |")
            print("--------------------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia | Fablab TECSUP  | SEGUIDORES  |")
            print("--------------------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |    MECANOS     | VELOCISTAS  |")
            print("--------------------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |                | VELOCISTAS  |")
            print("--------------------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |                |             |")
            print("--------------------------------------------------------------------")
            print("(15:00-16:00) |                     |  Proyectos     | MINI SUMOS  |")
            print("--------------------------------------------------------------------")
            print("(16:00-17:00) |                     |  Proyectos     | MINU SUMOS  |")
            print("------------------------------------------------------------------- ")
            print("(17:00-18:00) |                     |  Proyectos     |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print("(18:00-19:00) |                     |                |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print("(19:00-20:00) |                     |                |  WAR BOTS   |")
            print("--------------------------------------------------------------------")
            print()
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()
        def cuarto():

            print("---------------------------------------------------------")
            print("(9:00-10:00)  |                                         |")
            print("---------------------------------------------------------")
            print("(10:00-11:00) | Feria de Tecnologia | FINAL SEGUIDORES  |")
            print("---------------------------------------------------------")
            print("(11:00-12:00) | Feria de Tecnologia | FINAL VELOCISTA   |")
            print("---------------------------------------------------------")
            print("(12:00-13:00) | Feria de Tecnologia |    SUMOBOTS       |")
            print("---------------------------------------------------------")
            print("(13:00-14:00) | Feria de Tecnologia |      MIROSOFT     |")
            print("---------------------------------------------------------")
            print("(14:00-15:00) | Feria de Tecnologia |      MIROSOFT     |")
            print("---------------------------------------------------------")
            print("(15:00-16:00) |                                         |")
            print("---------------------------------------------------------")
            print("(16:00-17:00) |               CLAUSURA                  |")
            print("---------------------------------------------------------")
            print("(17:00-18:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("(18:00-19:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("(19:00-20:00) |                     |       WAR BOTS    |")
            print("---------------------------------------------------------")
            print("")
            input("Precione 'Enter' para regresar al CRONOGRAMA ")
            cronograma()

        print("\n/////////////CRONOGRAMA//////////////\n")
        print("-------------------------------")
        print("\t (1) Primer dia")
        print("-------------------------------")
        print("\t (2) Segundo dia ")
        print("-------------------------------")
        print("\t (3) Tercer dia ")
        print("-------------------------------")
        print("\t (4) Cuarto dia ")
        print("-------------------------------")
        print("\t (5) Regresar al menu  ")
        print("-------------------------------")

        op=int(input("Digite una opcion : "))
        if op==1:
            primero()
        elif op==2:
            segundo()
        elif op==3:
            tercero()
        elif op==4:
            cuarto()
        elif op==5:
            salirmenu()
        else:
            input("Digite una opcion valida ...")
            cronograma()
    def contactenos():
        print("FACEBOOK : ")
        print("https://www.facebook.com/IEEEUNSA/?fref=ts# ")
        input("Presione 'Enter' para regresar al MENU PRINCIPAL ")
        menu()

    print("\n//////////MENU PRINCIPAL///////////\n")
    print("-------------------------------")
    print("\t (1) Sobre EXPOTRON")
    print("-------------------------------")
    print("\t (2) Inscripciones ")
    print("-------------------------------")
    print("\t (3) Ver cronograma ")
    print("-------------------------------")
    print("\t (4) contactenos ")
    print("-------------------------------")
    print("\t (5) Salir ")
    print("-------------------------------")

    opcion=int(input("Digite una opcion del Menú :"))

    if opcion==1:
        nosotros()
    elif opcion==2:
        inscripcion()
    elif opcion==3:
        cronograma()
    elif opcion==4:
        contactenos()
    elif opcion==5:
        sys.exit()
    else:
        input("Digite una opcion valida  ")
        menu()
menu()






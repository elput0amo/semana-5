from libreria import BankAccount
cuenta= [
    BankAccount(0,500),
    BankAccount(1,236),
    BankAccount(2,6969),
    BankAccount(3,420),
    BankAccount(4,555),
    BankAccount(5,350),
    BankAccount(6,1200),
    BankAccount(7,58),
    BankAccount(8,3556),
    BankAccount(9,69),

]


divisas = {
    "euros" :1 ,
   "dolares":1.06,
    "yenes":150.91,
    "pesos":19.32,
    "dinares" :3.35,
    "coronas":11.62,
    "francos":0.95


}
#cuentas

numero=int( input(f"Introduzca su numero de cuenta (0-9): "))
cunt = cuenta[numero]

#cuentas2

print (f"Su cuenta numero {numero} tiene {cunt.cuanto_tienes()} euros actualmente")

#aqui se viene lo complicado
#pides la accion 
bucle=True
while (bucle):
    print (f"Porfavor escribe la accion que quieras realizar:")
    accion= input  (f"(depositar, extraer, comprobar dinero, cambiar divisa,cambiar de cuenta, cometer suicidio economico, cerrar sesion): ")

    if accion == "depositar":
        deposito= float(input("¿Cuanta pasta quieres meter? (euros): ") )
        cunt.deposit(deposito)
        print (f"Has añadido {deposito} euros a tu cuenta, llevando el total de esta a {cunt.cuanto_tienes()} euros, enhorabuena, sigues siendo pobre")

#depositar
    elif accion== "extraer":
        extraccion = float(input("¿Cuanta pasta quieres sacar? (euros): ")  )
        if (cunt.cuanto_tienes() - extraccion) < 0 :
            print(f"No te lo puedes permitir, das pena")
        else :
            cunt.extraer(extraccion)
            print (f"Eres {extraccion} euros mas pobre, te quedan en la cuenta {cunt.cuanto_tienes()} euros, ser rico te persigue, pero tu eres mas rapido")

#sacar pasta

    elif  accion == "comprobar dinero":
        print(f"Te lo digo cada vez que haces algo, no necesitas un comando ara esto, esta opcion solo esta para hacer parecer que el chatbot tiene varias opciones")
        print(f"Unpopular opinion, la gente de marketing y politica son seres humanos solo por el mas pequeño de los vacios legales")

    elif accion == "cambiar divisa": 
        print(f"Tu cuenta tiene {cunt.cuanto_tienes} euros")
        divisa = input(f"¿A que moneda quieres hacer el cambio? (euros, dolares,  yenes, pesos, dinares, francos, coronas): ")
        divisas= divisa
        cambio= cunt.cuanto_tienes*divisas 
        print(f"Tu cuenta consta de {cambio} {divisa}")
        if divisa=="euros":
            print (f"Porfavor, no te reproduzcas, eres gilipollas")

#cambiar divisa

    elif accion == "cambiar de cuenta":
        numero=int( input(f"Introduzca su numero de cuenta (0-9): "))
        cunt = cuenta[numero]
        print (f"Su cuenta numero {numero} tiene {cunt.cuanto_tienes()} euros actualmente")

#cambiar de cuenta

    elif  accion =="cometer suicidio economico":
        print(f"Inviertes todo tu dinero en la criptomoneda del momento, eres feliz unos dias hasta que esta baja a cero inevitablemente, tus amigos que solo te querian por tu dinero dejan de hablarte, intentas volver a ponerte en pie hasta que te das cuenta de que esta sociedad rota no va hacer mas que exprimirte mediante un sistema corrupto, ante la absurdidad que es la vida, tortura mandada por la decision de dios de darnos consciencia comienzas a abrir tus ojos a lo que la historia nos ha enseñado, que esta no ha sido mas que una serie de horrores creados por la humanidad mas alla de tu compresion, el unico resguardo que permite a tu mente seguir aferrandose al barranco que s presenta antes de la locura es el falso sentimiento de que tu pareja y tus hijos te aman, este breve escape mental dura poco, tus hijos fallecen debido a una sobredosis de droga causada por la presion que suponia sobre ellos una vida sin las comodidades que la sociedad ha establecido como necesarias en nuestra mente, tu pareja revela que su a mor hacia ti o hacia vuestros hijos nunca existio y no era mas que una manera de poder seguir junto a lo unico para lo que habia espacio en su corazon, la divisa por la que el mundo sangra y se pelea, tu dinero, te pide la separacion y la unica razon por la que no te deja mas vacio por dentro es porque no hay nada dentro de ti que te pueda quitar, la unica pertenecia con la que cuentas es tu vida, hasta que la pierdes dos dias despues en un puente mirando lo que era tu antigua casa boca suspendido boca abajo con lagrimas camuflandose con las estrellas que tambien observas, preguntandote si te convertiras en alguna de ellas pero en verdad deseando que este sea tu final, pues has descubierto que cualquier existencia se basa en el dolor, y que no hay diferencia entre una supernova y tu cabeza aplastada por el nuevo modelo de tesla. ")
    
    elif accion== "cerrar sesion":
        print(f"Gracias por utilizar nuestros servicios, para su informacion hemos vendido toda su informacion y privacidad al pujante mas rentable. ")
        bucle = False
    
    else :
        print(f"Ese no es un comando valido, vuelve a intentarlo dislexico.")

#estas ultimas son cerrar sesion y una gilipollez
    

 
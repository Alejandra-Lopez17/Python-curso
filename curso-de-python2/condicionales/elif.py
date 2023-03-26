ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en dificil")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien bro, estas bien")
    else:
        print("bro, estas gastando mcuho dinero, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamèrica")
    
elif ingreso_mensual > 500:
    print("estas bien en colombia")
    
elif ingreso_mensual > 200:
    print("estas bien en argentina")
    
else: 
    print("eres pobre")
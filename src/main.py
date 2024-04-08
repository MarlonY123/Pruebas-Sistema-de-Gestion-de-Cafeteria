def registroBebidas(entrada):
    # Separar la entrada por comas y eliminar espacios en blanco al principio y al final de cada elemento
    entrada = entrada.split(',')
    entrada = [e.strip() for e in entrada]

    # Verificar que el nombre del artículo solo contenga caracteres alfabéticos
    if not entrada[0].isalpha():
        raise Exception("El nombre solo debe contener caracteres alfabéticos")

    # Verificar que la longitud del nombre esté dentro del rango permitido (2 a 15 caracteres)
    if len(entrada[0]) > 15 or len(entrada[0]) < 2:
        raise Exception("Longitud incorrecta del nombre del artículo")
    
    # Seleccionar todos los elementos después del primero
    nueva_entrada = entrada[1:]
    
    if len(nueva_entrada) > 5 or len(nueva_entrada) < 1:
        raise Exception("Cantidad de tamaños incorrecta")

    # Inicializar variable para comparación de tamaños
    anterior = 0

    # Procesar cada tamaño de la bebida
    for i in nueva_entrada:
        try:
            # Intentar convertir el tamaño a flotante
            numero = float(i)

            # Verificar si el número es realmente un entero
            if not numero.is_integer():
                raise Exception("Se esperaba un número entero, se obtuvo un decimal")
        except ValueError:
            # Capturar el error si el valor no es un número
            raise Exception("Entrada no válida, se esperaba un número")

        # Convertir a entero después de verificar que es un entero
        numero = int(numero)

        # Verificar si el tamaño está dentro del rango permitido (1 a 48)
        if 1 <= numero <= 48:
            # Verificar si los tamaños están en orden ascendente
            if anterior < numero:
                anterior = numero
            else:
                raise Exception("Orden de los tamaños incorrectos")
        else:
            raise Exception("Tamaño fuera de rango")

    # Retornar mensaje de éxito si todas las validaciones pasaron
    return "Registro de nueva bebida exitoso"


print(registroBebidas("expresso,1,2,3,4,5"))

import pytest
from src.main import registroBebidas

#Pruebas para Nombre de la Bebida

#Válido: El nombre de la bebida es alfabético.
def test_registroArticuloAlfabetico():
    assert registroBebidas("chocolate,1") == "Registro de nueva bebida exitoso"

#Inválido: El nombre de la bebida no es alfabético.
def test_registroArticuloNoAlfabetico():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("chocol32*ate,1") 
    assert str(excinfo.value) == "El nombre solo debe contener caracteres alfabéticos"
    
#Inválido: El nombre de la bebida tiene menos de 2 caracteres de longitud.
def test_registroLongitudMenorA2():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas(",1,2")  
    assert str(excinfo.value) == "El nombre solo debe contener caracteres alfabéticos"

#Válido: El nombre de la bebida tiene de 2 a 15 caracteres de longitud.
def test_registroLongitudEntre2y15():
    assert registroBebidas("expresso,1,2,3,4,5") == "Registro de nueva bebida exitoso"
    
#Válido: El nombre de la bebida tiene exactamente 2 caracteres de longitud.
def test_registroLongitud2Letras():
    assert registroBebidas("ok,1,2") == "Registro de nueva bebida exitoso"

#Válido: El nombre de la bebida tiene exactamente 15 caracteres de longitud.
def test_registroLongitud15Letras():
    assert registroBebidas("aballestariamos,1,2") == "Registro de nueva bebida exitoso"
    
#Inválido: El nombre de la bebida tiene solo 1 carácter de longitud.
def test_registroLongitud1Letra():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("o,1,2")  
    assert str(excinfo.value) == "Longitud incorrecta del nombre del artículo"
    
#Inválido: El nombre de la bebida tiene más de 15 caracteres de longitud.
def test_registroLongitudMasde15Letras():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("aballestariamoso,1,2")  
    assert str(excinfo.value) == "Longitud incorrecta del nombre del artículo"
    
#Pruebas para Tamaño de la Bebida
    
#Inválido: El valor del tamaño es menor que 1.
def test_registroTamanoMenorQue1():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("aba,-1,2") 
    assert str(excinfo.value) == "Tamaño fuera de rango"
    
#Válido: El valor del tamaño está en el rango de 1 a 48.
def test_registroTamanoEnElRango1A48():
    assert registroBebidas("frappe,1,22,33,45,48") == "Registro de nueva bebida exitoso"
    
#Inválido: El valor del tamaño es mayor que 48.
def test_registroTamanoMayorQue48():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("aba,49")  
    assert str(excinfo.value) == "Tamaño fuera de rango"
    
#Válido: El valor del tamaño es un número entero.
def test_registroTamanoNumeroEntero():
    assert registroBebidas("mocha,14") == "Registro de nueva bebida exitoso"
    
#Inválido: El valor del tamaño es un decimal.
def test_registroTamanoNumeroDecimal():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("latte,4.9")  
    assert str(excinfo.value) == "Se esperaba un número entero, se obtuvo un decimal"

#Inválido: El valor del tamaño incluye caracteres no numéricos.
def test_registroTamanoNoNumerico():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("latte,a")  
    assert str(excinfo.value) == "Entrada no válida, se esperaba un número"

#Válido: Los valores del tamaño se ingresan en orden ascendente.
def test_registroTamanoNumerosAscendentes():
    assert registroBebidas("expresso,1,2,3,4,5") == "Registro de nueva bebida exitoso"
    
#Inválido: Los valores del tamaño no están en orden ascendente.
def test_registroTamanoNoAscendente():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("latte,5,4,3,2,1")  
    assert str(excinfo.value) == "Orden de los tamaños incorrectos"
    
#Inválido: No se ingresan valores de tamaño.
def test_registroNoTamanos():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("caramelo")  
    assert str(excinfo.value) == "Cantidad de tamaños incorrecta"

    
#Válido: Se ingresan un valor de tamaño
def test_registroUnTamano():
    assert registroBebidas("naranja,32") == "Registro de nueva bebida exitoso"

#Válido: Se ingresan cinco valores de tamaño   
def test_registroCincoTamanos():
    assert registroBebidas("naranja,32,33,34,39,42") == "Registro de nueva bebida exitoso"
    
#Inválido: Se ingresan más de cinco tamaños.
def test_registroMasDe5Tamanos():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("caramelo,1,2,3,4,5,6")  
    assert str(excinfo.value) == "Cantidad de tamaños incorrecta"    

    
#Pruebas para Formato de Entrada

#Inválido: El nombre del artículo no es el primero en la entrada.
def test_registroLongitudMenorA2():
    with pytest.raises(Exception) as excinfo:  
        registroBebidas("1,ok,43")  
    assert str(excinfo.value) == "El nombre solo debe contener caracteres alfabéticos"

#Valido: La entrada no contiene espacios en blanco.
def test_registroNoContieneEspacios():
    assert registroBebidas("macchiato,32,33") == "Registro de nueva bebida exitoso"

#Valido: La entrada contiene espacios en blanco.
def test_registroContieneEspacios():
    assert registroBebidas("macchiato     ,     3         , 6,        9") == "Registro de nueva bebida exitoso"


class User():
    #Podemos usar la cedula como contraseña
    def __init__(self, cedula="",nombre="",cargo="",salarioMensual=0 ):
        self.cedula= cedula
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salarioMensual
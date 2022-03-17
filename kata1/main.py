# Autor: Jose
# version: 0.0.1
# data: 15/03/2022

# description: kata I - sesión de clase

from kata1.Alumno import Alumno

if __name__ == '__main__':
    # Instancias de clase
    al1 = Alumno('Jose', 'Marín', '123456789A', 35)

    # Uso de metodos de clase
    al1.addNota(9)
    al1.addNota(5)
    al1.addNota(7)
    al1.addAge()

    print(al1)
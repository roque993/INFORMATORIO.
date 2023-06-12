#Desafío 8: Principios de programación orientada a objetos

#   -----Crear las siguientes clases con sus atributos y métodos.

#-----------Clase Usuario--------------
#1----atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
# -----métodos: login(), registrar()-------

class persona:

    def __init__(self,id,nombre,apellido,telefono,username, email, contraseña, fecha_de_registro, avatar, estado, online):
            self.id = id
            self.nombre=nombre
            self.apellido = apellido
            self.telefono = telefono
            self.username= username
            self.email=email
            self.contraseña=contraseña
            self.fecha_de_registro=fecha_de_registro
            self.avatar=avatar
            self.estado=estado
            self.online=online
    # Metodo registrar
    def __str__(self):
        return f"{self.id } {self.nombre} {self.apellido} {self.telefono} {self.username} {self.email} {self.contraseña} {self.fecha_de_registro} {self.avatar} {self.estado} {self.online}"
# lista

lista_personas_registradas = []    

# funcion login  
def  login():
      for i in range(len(lista_personas_registradas)):
             if lista_personas_registradas[i].username == usuario and lista_personas_registradas[i].contraseña == pasword:
              print (lista_personas_registradas[i].nombre,"Bienvenido. ")
    
           
# Pide datos y retorna el registro de una nueva  persona a la lista.
def registrar_persona():
    id = input("Ingrese un Id:")
    nombre= input("Ingrese nombre:")
    apellido= input("Ingrese apellido:")
    telefono= input("Ingresetelefono:")
    username= input("Ingrese username:")
    email= input("Ingrese email:")
    contraseña= input("Ingrese contraseña:")
    fecha_de_registro= input("Ingrese fecha de registro:")
    avatar= input("Ingrese avatar:")
    estado= input("Ingrese  estado:")
    online= input("Ingrese si esta en linea si/no")
    return persona(id,nombre,apellido,telefono,username, email, contraseña, fecha_de_registro, avatar, estado, online)
    




print("----------------------------------------------")
print("MENU ")
print("1- Registrarce")
print("2- Login")
print("0- Salir")

while True:

        opc = int(input("Ingrese su opcion: "))
        if opc == 0:
            break
        elif opc == 1:
            nueva_persona = registrar_persona()
            lista_personas_registradas.append(nueva_persona)
        elif opc == 2:
         #VARIABLES PARA LOGIN
         usuario = input("Ingrese su usuario:")
         pasword = input("Ingrese su contraseña:")
         login()
      
             
        
       
            
            
            
  






                  
            


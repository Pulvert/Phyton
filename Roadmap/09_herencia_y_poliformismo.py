"""
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y alma
"""

# Ejemplos Animales

class Animal:

  def __init__(self,name):
    self.name = name
    self.legs = 4
    self.tail = 1
    self.typ = "Domestic"

class Dog(Animal):

  def __init__(self, name, race):
    super().__init__(name)
    self.race = race

  def sound (self):
    print("Guau Guau")

class Cat(Animal):

  def __init__(self, name, race):
    super().__init__(name)
    self.race = race

  def sound (self):
    print("Miau Miau")


my_dog = Dog("Juanchi","Labrador")
print(f"{my_dog.name} es {my_dog.typ}")
print(f"{my_dog.name} tiene {my_dog.legs} patas")
my_dog.sound()

my_cat = Cat("Lauri","Persa")
print(f"{my_cat.name} tiene {my_cat.legs} patas")
my_cat.sound()

# Extra

class Employee:
  def __init__ (self, id, name):
    self.id = id
    self.name = name
    self.employees = []

  def add (self, employee):
    self.employees.append(employee)

  def print_employees(self):
    for employee in self.employees:
      print(employee.name)

class Manager(Employee):
  def __init__ (self, id, name, salary):
    super().__init__(id, name)
    self.salary = salary

  def functions (self):
    print(f"{self.name} se encarga de dirigir el departamento")

class Project_manager(Employee):
  def __init__ (self, id, name, salary, team):
    super().__init__(id, name)
    self.salary = salary
    self.team = team

  def functions (self):
    print(f"{self.name} se encarga de dirigir el proyecto")

class Programmer(Employee):
  def __init__ (self, id, name, language):
    super().__init__(id, name)
    self.language = language

_01 = Programmer (1, "Diego", "Python")
_02 = Manager (2, "Carlos", 50000)
_03 = Project_manager (3, "Juan", 40000, 15)


print(_01.id)
print(_01.name)
print(_01.language)

print(_02.id)
print(_02.name)
print(_02.salary)

print(_03.functions())


# Solución

"""
Ejercicio
"""

# Superclase

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# Subclases

class Dog(Animal):

    def sound(self):
        print("Guau!")


class Cat(Animal):

    def sound(self):
        print("Miau!")

def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)


"""
Extra
"""

class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")


class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")


my_manager = Manager(1, "MoureDev")
my_project_manager = ProjectManager(2, "Brais", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Moure", "Proyecto 2")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "Cobol")
my_programmer3 = Programmer(6, "Bushi", "Dart")
my_programmer4 = Programmer(7, "Nasos", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()
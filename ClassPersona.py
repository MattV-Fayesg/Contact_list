
class Persona:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def height(self):
        return self.__height

    # Sets
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @height.setter
    def height(self, height):
        self.__height = height

    def returns_data(self):
        return f'Person Info|--------------------\n' \
               f' name: {self.name}\n' \
               f' Age: {self.age}\n' \
               f' Height: {self.height}\n '

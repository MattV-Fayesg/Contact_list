
class Persona:

    def __init__(self, phone_number, name, age, height, address):
        self.__phone_number = phone_number
        self.__name = name
        self.__age = age
        self.__height = height
        self.__address = address

    # Getters
    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def height(self):
        return self.__height

    @property
    def address(self):
        return self.__address

    # Sets
    @phone_number.setter
    def phone_number(self, phone_num):
        self.__phone_number = phone_num

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @height.setter
    def height(self, height):
        self.__height = height

    @address.setter
    def address(self, address):
        self.__address = address

    def returns_data(self):
        return f'Person Info|--------------------\n' \
               f' Phone Number: {self.phone_number}\n' \
               f' name: {self.name}\n' \
               f' Age: {self.age}\n' \
               f' Height: {self.height}\n '

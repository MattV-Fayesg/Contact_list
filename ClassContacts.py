from s16Exercises.ClassPersona import Persona


class Contacts(Persona):
    contact_list = []

    def __init__(self, name='', age=0, height=0.0):
        super().__init__(name, age, height)
        self.__contact_list = Contacts.contact_list
        self.__contact = Persona(self.name, self.age, self.height)

    def register_contact(self):
        while len(self.__contact_list) < 6:
            if self.__contact not in self.__contact_list:
                self.__contact_list.append(self.__contact)
                return f'\n"{self.name}" was Added on your contact list\n'
            else:
                break
        else:
            return f'\nContact list is full\n'

    def clear_duplicity(self):
        for person in self.__contact_list:
            position = (self.__contact_list.index(person))
            if person.name == self.__contact_list[position - 1].name and\
                    person.age == self.__contact_list[position - 1].age and\
                    person.height == self.__contact_list[position - 1].height:
                print(f"\nWe found a duplicity in your contact list\n"
                      f" \n{person.returns_data()}\n {self.__contact_list[position - 1].returns_data()}")
                confirmation = input(f"Are they the same person?(y/n)\n>>> ").upper()
                if confirmation == 'Y':
                    self.__contact_list.pop(position)
                    print(f'\nContact "{person.name}" duplicity was deleted!')
                else:
                    person.name = input('Enter a new name for your contact:\n >>> ')
                    print(f"\nContact name changed:\n {person.returns_data()}")

    def remove_contact(self):
        for person in self.__contact_list:
            position = (self.__contact_list.index(person))
            if person.name == self.name:
                self.__contact_list.pop(position)
                return f"\nContact found!\n name: {person.name}\n Deleted!"
        else:
            return f"Contact not found!"

    def search(self):
        for person in self.__contact_list:
            if person.name == self.name:
                return f"\nContact found!\n name: {person.name}\n id: {(self.__contact_list.index(person)) + 1}"
        else:
            return f"Contact not found!"

    def all_contacts(self):
        for i in range(len(self.__contact_list)):
            person = self.__contact_list[i]
            position = (self.__contact_list.index(person)) + 1
            print(f'{position} {person.name}')


# Contatos para registrar
jp = Contacts('João Pedro', 18, 1.80)
marcos = Contacts('Marcos', 21, 1.83)
joao = Contacts('João', 35, 1.80)
nick = Contacts('nicolas', 24, 1.75)
jp_2 = Contacts('João Pedro', 18, 1.80)
nick2 = Contacts('nicolas', 24, 1.75)

# Registrando
jp.register_contact()
marcos.register_contact()
joao.register_contact()
nick.register_contact()
nick2.register_contact()
jp_2.register_contact()

# Exibindo contatos
Contacts().all_contacts()

# Procurando por contato X
print(nick.search())
#  Ou
print(Contacts('zezé', 21, 1.83).search())

# Removendo Contato
print(marcos.remove_contact())

# Exibindo contatos
print()
Contacts().all_contacts()

# Limpando duplicidades da lista
Contacts().clear_duplicity()

# Exibindo contatos
print()
Contacts().all_contacts()

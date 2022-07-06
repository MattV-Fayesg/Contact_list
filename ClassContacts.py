from ClassPersona import Persona


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
        duplicity = []
        old_contact = []
        # Getting all the duplicities
        for person in self.__contact_list:
            position = (self.__contact_list.index(person))
            if person.name == self.__contact_list[position - 1].name and\
                    person.age == self.__contact_list[position - 1].age and\
                    person.height == self.__contact_list[position - 1].height:

                duplicity.append(person)
                old_contact.append(self.__contact_list[position - 1])

        # Showing all duplicities
        print(f"\nWe found a duplicity in your contact list\n")
        for i in range(len(old_contact)):
            print(f" {duplicity[i].returns_data()}\n {old_contact[i].returns_data()}")
            confirmation = input(f"Are they the same person?[Y/N]\n>>> ").upper()
            while confirmation:  # Confirming if person one == person two
                if confirmation == 'Y':
                    self.__contact_list.pop(self.__contact_list.index(duplicity[i]))
                    print(f'\nContact "{duplicity[i].name}" duplicity was deleted!')
                    break
                elif confirmation == 'N':
                    new_name = input('Enter a new name for your contact:\n >>> ')  # Setting a new name for person two
                    while new_name == old_contact[i].name:
                        new_name = input('\nYou already got a contact with that name\n'
                                         'Please, Enter a new name for your contact:\n >>> ')
                    else:
                        duplicity[i].name = new_name
                        print(f"\nContact name changed:\n {duplicity[i].returns_data()}")
                        break
                else:
                    print('Invalid command!')
                    confirmation = input(f"Are they the same person?[Y/N]\n>>> ").upper()

    def remove_contact(self):
        for person in self.__contact_list:
            position = (self.__contact_list.index(person))
            if person.name == self.name:
                self.__contact_list.pop(position)
                return f"\nContact found!\n name: {person.name}\n Deleted!"
        else:
            return f"\nContact not found!\n"

    def search(self):
        for person in self.__contact_list:
            if person.name == self.name:
                return f"\nContact found!\n name: {person.name}\n id: {(self.__contact_list.index(person)) + 1}"
        else:
            return f"\nContact not found!\n"

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

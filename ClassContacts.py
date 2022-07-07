from ClassPersona import Persona


class Contacts(Persona):
    contact_list = []

    def __init__(self, phone_number=0, name='', age=0, height=0.0, address=''):
        super().__init__(phone_number, name, age, height, address)
        self.__contact_list = Contacts.contact_list
        self.__contact = Persona(self.phone_number, self.name, self.age, self.height, self.address)

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
            if person.phone_number == self.__contact_list[position - 1].phone_number:
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
                    print(f'\nContact "{duplicity[i].name}" duplicity was deleted!\n')
                    break
                elif confirmation == 'N':
                    # Setting a new phone number for person two
                    try:
                        new_num = int(input('Enter a new phone number for your contact:\n >>> '))
                    except ValueError:
                        new_num = int(input("it's not a number!"
                                            "\nPlease enter a new phone number for your contact:"
                                            "\n >>> "))

                    while new_num == old_contact[i].phone_number:
                        try:
                            new_num = int(input('\nYou already got a contact with that phone number\n'
                                                'Please, Enter a new phone number for your contact:\n >>> '))
                        except ValueError:
                            new_num = int(input("it's not a number!"
                                                "\nPlease enter a new phone number for your contact:"
                                                "\n >>> "))
                    else:
                        duplicity[i].phone_number = new_num
                        print(f"\nContact phone number has changed:\n {duplicity[i].returns_data()}")
                        break
                else:
                    print('Invalid command!')
                    confirmation = input(f"Are they the same person?[Y/N]\n>>> ").upper()

    def remove_contact(self):
        for person in self.__contact_list:
            position = (self.__contact_list.index(person))
            if person.name == self.name:
                self.__contact_list.pop(position)
                return f"\nContact found!\n name: {person.name} phone_number: {person.phone_number}\n Deleted!"
        else:
            return f"\nContact not found!\n"

    def search(self):
        for person in self.__contact_list:
            if person.name == self.name:
                return f"\nContact found!\n |id: {(self.__contact_list.index(person)) + 1}, |name: {person.name}\n" \
                       f" phone number: {person.phone_number} "
        else:
            return f"\nContact not found!\n"

    def all_contacts(self):
        print('Contact list |-----------------')
        for i in range(len(self.__contact_list)):
            person = self.__contact_list[i]
            position = (self.__contact_list.index(person)) + 1
            print(f' |id: {position}| name: {person.name}|\n'
                  f' |Phone Number: {person.phone_number}')
            print(' -' * 10)


# Running Examples
# Contatos para registrar
jp = Contacts(12_99856_4556, 'João Pedro', 18, 1.80)
marcos = Contacts(11_96954_7854, 'Marcos', 21, 1.83)
joao = Contacts(13_99456_5412, 'João', 35, 1.80)
nick = Contacts(11_99717_7177, 'nicolas', 24, 1.75)
jp_2 = Contacts(12_99856_4556, 'João Pedro', 18, 1.80)
nick2 = Contacts(11_99717_7177, 'nicolas', 24, 1.75)

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
print(Contacts(name='zezé').search())

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

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self,name, newName, newPhone, newEmail):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                contact.name = newName
                contact.phone = newPhone
                contact.email = newEmail
                self._save()
                break
        else:
            self._not_found()

    def _not_found(self):
        print('****************************')
        print('¡No se encontro el contacto!')
        print('****************************')

    def _save(self):
        with open('contacts.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            else:
                contact_book.add(row[0],row[1],row[2])

    while True:
        command = input('''
    B I E N V E N I D O  A  L A  A G E N D A
    
            ¿Que necesitas hoy?
            
            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir
            
            Selecciona tu opcion: ''')

        if command == 'a':
            print('añadir contacto')
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escribe el número del contacto: ')
            email = input('Escribe el email del contacto: ')

            contact_book.add(name,phone,email)

        elif command == 'ac':
            print('actualizar contacto')
            contact_book.show_all()
            name = input('Escribe el nombre del contacto: ')
            nName = input('Escribe el nuevo nombre del contacto: ')
            nPhone = input('Escribe el nuevo numero: ')
            nEmail = input('Escribe el nuevo Email: ')
            contact_book.update(name,nName,nPhone,nEmail)
            contact_book.search(nName)


        elif command == 'b':
            print('buscar contacto')
            name = input('Escribe el nombre del contacto: ')
            contact_book.search(name)

        elif command == 'e':
            print('eliminar contacto')
            contact_book.show_all()
            name = input('Escribe el nombre del contacto: ')
            contact_book.delete(name)

        elif command == 'l':
            print('listar contacto')
            contact_book.show_all()


        elif command == 's':
            break

if __name__ == '__main__':
    run()

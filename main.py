

class Contact:
    def __init__(self, first_name, last_name, phone, favourite=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.favourite = favourite
        self.additional = kwargs
    
    
    def __str__(self):
        result = ''
        result += f'Имя: {self.first_name}\n'
        result += f'Фамилия: {self.last_name}\n'
        result += f'Телефон: {self.phone}\n'
        if self.favourite:
            result += 'В избранных: да\n'
        else: 
            result += 'В избранных: нет\n'
        
        if len(self.additional) > 0:
            result += 'Дополнительная информация: \n'
            for i in self.additional:
                result += f'\t{i}: {self.additional[i]}\n'
        
        return result
    
    
class Phonebook:
    def __init__(self, name, *args):
        self.name = name
        self.contacts = [i for i in args if isinstance(i, Contact)]
        
    def show_contacts(self):
        for i, contact in enumerate(self.contacts):
            print(f'{i+1})', contact, sep='\n')
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def delete_contact(self, phone):
        for i, contact in enumerate(self.contacts):
            if contact.phone == phone:
                self.contacts.pop(i)
                return 
            
    def find_favourites(self):
        for contact in self.contacts:
            if contact.favourite:
                print(contact.phone)
                
    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                print(contact)
        
    
def main():            
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    petya = Contact('Petya', 'Ivanov', '+78005553535', True, vk='petyawashere')
    vova = Contact('Vova', 'Petrov', '+74952001020', facebook='2233322')
    
    book = Phonebook('Васины записки', jhon, petya, vova)
    
    book.show_contacts()
    
    igor = Contact('Igor', 'Petrushkin', '+79008007060', True, telegram='@igoresha')
    
    book.add_contact(igor)
    
    book.find_contact('Petya', 'Ivanov')
    
    book.show_contacts()
    
    book.find_favourites()
    
    book.delete_contact('+7123')
    
    book.show_contacts()
    
if __name__ == '__main__':
    main()

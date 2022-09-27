from sysconfig import get_path_names


class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone

    def print_person(self):
        print(self.__name, self.__address, self.__phone)

class Customer(Person):
    def __init__(self,name,address,phone, number, mail_list):
        Person.__init__(self,name,address,phone)

        self.__number = number
        self.__mail_list = mail_list

    def get_number(self):
        return self.__number
        
    def get_mail_list(self):
        return self.__mail_list

    def print_person(self):
        print('Method 1')
        print(Person.get_name(self))
        print(Person.get_address(self))
        print(Person.get_phone(self))
        print()
        print('Method 2')
        print()
        Person.print_person(self)

        print('Customer Number: ', self.__number)
        if self.__mail_list:
            print('yes on list')
        else:
            print('not on list')




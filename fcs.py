class Driver:
    last_id = 0

    def __init__(self, name, start_city):
        Driver.last_id += 1
        tuple = ()
        self.name = input(name)
        self.start_city = input(start_city)
        self.id = 'ID%03d' % Driver.last_id
        if i in self.id:
            tuple.append(i)

        return self.id, self.name, self.start_city


class WeDeliver:

    def __init__(self): 
        self.drivers = []
        self.cities = []

    def add_driver(self, name, start_city):
        new_driver = Driver(name, start_city)
        if start_city not in self.cities:
            print(start_city, ("is not in the database."))
            new_city = input("Do you want to add it? yes/no")
            if new_city.lower() == 'yes':
                self.cities.append(start_city)
            else:
                print("Driver cannot added. ")
            return
        self.drivers.append(new_driver)

    def similar_drivers():
        print("Hello world")
        

def main_menu():
    while True:
        choice = input("Welcome to We Deliver! Please enter: ")
        print("1. To go to the drivers’ menu ")
        print("2. To go to the cities’ menu")
        print("3. To exit the system")
        if choice == '1':
            drivers_menu()
        elif choice == '2':
            cities_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice,Please try again")
            return


def drivers_menu():
    choice = str(input("Enter :"))
    print("1. To view all the drivers")
    print("2. To add a driver")
    print("3. Check similar drivers")
    print("4. To go back to the main menu")
    if choice == '1':
        all_drivers()
    elif choice == '2':
        name = input("Enter driver's name: ") 
        start_city = input("Enter driver's start city: ")
        WeDeliver.add_driver(name, start_city)
    elif choice == '3':
        WeDeliver.similar_drivers()
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice,Please try again")
        return


def all_drivers(self):
# a list of all the drivers and their details are printed to the users.
    self.drivers()


def cities_menu():
    choice = input("Enter :")
    print("1.	Show cities  ")
    print("2.	Search city ")
    print("3.	Print neighboring cities  ")
    print("4.	Print Drivers delivering to city ")
    if choice == '1':
        print("Hello world")
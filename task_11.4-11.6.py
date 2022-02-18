
class Warehouse:

    def __init__(self, equipments=None):
        if not equipments:
            equipments = []
        self.equipments = equipments
        self.records = {}

    def issue_equipment(self, equipment, department, date):
        if equipment in self.equipments:
            equipment.in_warehouse = False
            department.count_equipment_on_hand += 1
            record = Record(department=department, equipment=equipment, date_of_issue=date)
            key = equipment.get_equipment_info()
            self.records[key] = record
        else:
            print("There is not such equipment. ")

    def return_equipment(self, equipment, department):
        if equipment in self.equipments:
            equipment.in_warehouse = True
            department.count_equipment_on_hand -= 1
            self.records[equipment.get_equipment_info()].returned = True
        else:
            print("There is not such equipment. ")


class Equipment:

    __count = 0

    def __init__(self, title, serial_number, unit_value, in_warehouse=True):
        self.title = title
        self.serial_number = serial_number
        self.unit_value = unit_value
        self.in_warehouse = in_warehouse
        Equipment.__count += 1

    def get_equipment_info(self):
        return f"{self.title} - {self.serial_number}"

    def __str__(self):
        return f'{self.title} - {self.serial_number}'

    @staticmethod
    def type_of_equipment():
        print("This is an office equipment.")


class Printer(Equipment):

    def __init__(self, title, serial_number, unit_value, print_speed, in_warehouse=True):
        super(Printer, self).__init__(title, serial_number, unit_value, in_warehouse)
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, title, serial_number, unit_value, scanner_type, in_warehouse=True):
        super(Scanner, self).__init__(title, serial_number, unit_value, in_warehouse)
        self.scanner_type = scanner_type


class Copier(Equipment):
    def __init__(self, title, serial_number, unit_value, resolution, in_warehouse=True):
        super(Copier, self).__init__(title, serial_number, unit_value, in_warehouse)
        self.resolution = resolution


class Department:
    def __init__(self, name, count_equipment_on_hand=0):
        self.name = name
        self.count_equipment_on_hand = count_equipment_on_hand

    def __str__(self):
        return f'{self.name}'


class Record:
    def __init__(self, department, equipment, date_of_issue, returned=False):
        self.department = department
        self.equipment = equipment
        self.date_of_issue = date_of_issue
        self.returned = returned

    def __repr__(self):
        return f'{self.department}:{self.equipment}:{self.date_of_issue}:{self.returned}'


printer = Printer('HP', 123, 25000, 20)
scanner = Scanner('Epson', 456, 12000, 'laser')
copier = Copier('Canon', 789, 36000, '64000*96000')

department = Department('Commercial')
warehouse = Warehouse([printer, scanner, copier])

print(department.count_equipment_on_hand)
print(warehouse.records)
print(printer.in_warehouse)
print('****issuing equipment****')
warehouse.issue_equipment(printer, department, '21-11-2021')
print(department.count_equipment_on_hand)
print(warehouse.records)
print(printer.in_warehouse)
print('****receiving equipment****')
warehouse.return_equipment(printer, department)
print(department.count_equipment_on_hand)
print(warehouse.records)
print(printer.in_warehouse)

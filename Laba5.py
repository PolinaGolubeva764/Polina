import self

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def get_info(self):
        return f'{self.name}, {self.id}'
Sotrudnik = Employee("Иван","123")
print(Sotrudnik.get_info())

class Manager(Employee):
    def __init__(self, name, id, dept):
        Employee.__init__(self, name,id)
        self.name=name
        self.id=id
        self.dept = dept

    def get_info(self):
        return super().get_info() + f" Department: {self.dept}"

    def manage_project(self):
        print(self.get_info(), f"Managing project")

#Создание  менеджера и вызов метода управления проектами
Manager1 = Manager(name="Павел", id="345", dept="Офис проектов")
Manager1.manage_project()




class Technician(Employee):
    def __init__(self,name,id,specialization):
        Employee.__init__(self,name, id)
        self.specialization = specialization

    def get_info(self):
        return super().get_info() + f" Department: {self.specialization}"

    def perform_maintenance(self):
        print(self.get_info(), f"Выполнил техническое задание")


# Создание технолога и вызов метода  технического обслуживания
Technician1 = Technician(name="Олег", id="009", specialization="Технолог")
Technician1.perform_maintenance()


class TechManager(Manager,Technician):
    def __init__(self,name,id,dept,specialization,empllist):
         Employee.__init__(self,name, id)
         Manager.__init__(self,name,id, dept)
         Technician.__init__(self,name,id,specialization)
         self.empllist = []

    def add_employee(self,empl):
        if isinstance(empl, Employee):
            self.empllist.append(empl)
            return f"{empl.name} добавлен в команду "

    def get_team_info(self):

        for empl in self.empllist:
            print("|" + empl.get_info())

# Создание технического менеджера
tech1 = TechManager(name="Павел", id="345", dept="Офис проектов", specialization="ИБ специалист",empllist=[])
print(tech1.get_info())
# Добавление менеджера в команду
print(tech1.add_employee(Manager1))
print(tech1.add_employee(Technician1))
tech1.get_team_info()
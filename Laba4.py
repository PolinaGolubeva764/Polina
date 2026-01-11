import self

class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self,new_password):
        self.password = new_password
    def check_password(self,passwordnew):
        if self.password==passwordnew:
            return True
        else: return False
Myaccount = UserAccount('polina','polina@ru','Rtjgu')


print(Myaccount.password)
Myaccount.check_password('Rtjgu')
print(Myaccount.check_password('Rtjgu'))

#class Vehicle:
#    def __init__(self,make,model):
#        self.make = make
#        self.model = model
#    def get_info(self):
#        return f'{self.make}, {self.model}'

#Mycar = Vehicle("Москвич","244")


#class Car(Vehicle):
#    def __init__(self, make, model, fuel_type):
#        super().__init__(make, model)
#        self.fuel_type = fuel_type
#    def get_info(self):
#        return f'{self.fuel_type}, {self.model}, {self.make}'

#car1 = Car("Волга","Модель1","Бензин")
#print(car1.get_info())
from html.parser import tagfind_tolerant

import self


#class Book:
#    def __init__(self, title, author, year):
#        self.title = title
#        self.author = author
#        self.year = year
#    def get_info(self):
#        return f'{self.title}, {self.author}, {self.year}'

#kniga1 = Book("'Война и мир'", "Толстой",1885)
#print("Хорошая книга:",kniga1.title)
#print(kniga1.get_info())

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return f'{self.radius}'
    def set_radius(self,new_radius):
        self.radius=new_radius

krug1 = Circle(30)
print(krug1.get_radius())
krug1.set_radius(80)
print(krug1.get_radius())
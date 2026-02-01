class school:
    def __init__(self,rollno,name,standard):
        self.rollno = rollno
        self.name = name
        self.standard = standard

    def teaching(self):
        return "its teaching"

class home(school):
    def __init__(self,rollno,name,standard,doornum,street,food):
        super().__init__(rollno, name, standard)  # 👈 important
        self.doornum = doornum
        self.street = street
        self.food = food

    def eating(self):
        return "i am eating"    

sri_chaitanya = school(1,"vamsi",10)

ff1 = home(1,'vamsi',10,'ff1','lakshminarayana nagar','noodles')

print(ff1.food)

# print(sri_chaitanya.name)


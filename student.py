class Student:
    def __init__(self,name,age,adress,dep):
        self.name=name
        self.age=age
        self.adress=adress
        self.dep=dep
        
    def student_details(self):
        print(f"student name is {self.name} AGE {self.age} from {self.adress} student depeartment is {self.dep}")
        
        
Studenta=Student("rahul",22,"delhi,agra","cse")
Studentb=Student("akhil",23,"andra pradesh","mech")

Studenta.student_details()
Studentb.student_details()
        
class Teacher:
    def setid(self,id):
        self.id=id

    def getid(self):
        return self.id

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setaddress(self,address):
        self.address=address

    def getaddress(self):
        return self.address

    def setsalary(self,sal):
        self.sal=sal

    def getsalary(self):
        return self.sal

class Student(Teacher):  #created student subclass from teacher super class
    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks

#setting all the values for student
s=Student()
s.setid(1008887)
s.setname("siddu")
s.setaddress("vijaynagar")
s.setsalary(150000)
s.setmarks(1000)

#getting all the values from student
print("My id is",s.getid())
print("My name is ",s.getname())
print("My address is ",s.getaddress())
print("My salary is ",s.getsalary())
print("My marks is",s.getmarks())


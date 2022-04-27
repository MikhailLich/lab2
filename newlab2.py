class Person:
    def __init__(self, name, role, ball1, ball2, ball3):
        self.name = name
        self.role = role
        self.ball1 = ball1
        self.ball2 = ball2
        self.ball3 = ball3

    def showInfo(self):
        print("Name: ", self.name)
        print("Role: ", self.role)
        print("IT ball", self.ball1)
        print("Math ball", self.ball2)
        print("Russkiy ball", self.ball3)
        print("average ball: ", (self.ball1 + self.ball2 + self.ball3) / 3)

    def printinfo(self):
        f.write(f"Name: {self.name}\n")
        f.write(f"Role: {self.role}\n")
        f.write(f"IT ball {self.ball1}\n")
        f.write(f"Math ball {self.ball2}\n")
        f.write(f"Russkiy ball {self.ball3}\n")
        f.write(f"average ball: {(self.ball1 + self.ball2 + self.ball3) / 3}\n")
        f.write("--------------------------\n")

    def InfoPrep(self):
        print("Name: ", self.name)
        print("Role: ", self.role)
        print("Aimee ball", self.ball1)
        print("Alice ball", self.ball2)
        print("Tran ball", self.ball3)
        print("average ball: ", (self.ball1 + self.ball2 + self.ball3) / 3)

    def InfoPrepPrint(self):
        f.write(f"Name: {self.name}\n")
        f.write(f"Role: {self.role}\n")
        f.write(f"Aimee ball {self.ball1}\n")
        f.write(f"Alice ball {self.ball2}\n")
        f.write(f"Tran ball {self.ball3}\n")
        f.write(f"average ball: {(self.ball1 + self.ball2 + self.ball3) / 3}\n")
        f.write("--------------------------\n")


f = open('xyz.txt','w')
aimee = Person("Aimee", "Student", 21, 66, 78)
aimee.showInfo()
aimee.printinfo()
print(" --------------- ")

alice = Person("Alice", "Student", 18, 88, 96)
alice.showInfo()
alice.printinfo()
print(" --------------- ")
tran = Person("Tran", "Student", 37, 34, 95)
tran.showInfo()
tran.printinfo()
print(" --------------- ")

ITprep = Person("Masscot", "IT prep", aimee.ball1, alice.ball1, tran.ball1)
ITprep.InfoPrep()
ITprep.InfoPrepPrint()

print(" --------------- ")

Mathprep = Person("Hendors", "Math prep", aimee.ball2, alice.ball2, tran.ball2)
Mathprep.InfoPrep()
Mathprep.InfoPrepPrint()
print(" --------------- ")

Ruprep = Person("Ivanov", "Ru prep", aimee.ball3, alice.ball3, tran.ball3)
Ruprep.InfoPrep()
Ruprep.InfoPrepPrint()
f.close()

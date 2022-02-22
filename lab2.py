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


aimee = Person("Aimee", "Student", 21, 66, 78)
aimee.showInfo()
print(" --------------- ")

alice = Person("Alice", "Student", 18, 88, 96)
alice.showInfo()

print(" --------------- ")
tran = Person("Tran", "Student", 37, 34, 95)
tran.showInfo()

print(" --------------- ")

ITprep = Person("Masscot", "IT prep", aimee.ball1, alice.ball1, tran.ball1)
print("Name: ", ITprep.name)
print("Role: ", ITprep.role)
print("IT ball aimee", ITprep.ball1)
print("IT ball alice", ITprep.ball2)
print("IT ball tran", ITprep.ball3)
print("average ball: ", (ITprep.ball1 + ITprep.ball2 + ITprep.ball3) / 3)



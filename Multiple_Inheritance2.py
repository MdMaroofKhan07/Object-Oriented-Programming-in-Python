class Mother:
    motherName = ""
    def mother(self):
        print(self.motherName)

class Father:
    fatherName = ""
    def father(self):
        print(self.fatherName)

class Son(Mother,Father):
    sonName = ""
    def name(self):
        print("Name :", self.sonName)

    def parents(self):
        print("Father :", self.fatherName)
        print("Mother :", self.motherName)

s1 = Son()
s1.sonName = "Haabeel"
s1.fatherName = "Adam"
s1.motherName = "Hawwa"
s1.name()
s1.parents()
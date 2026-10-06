# Class: Student
class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"


# Class: Faculty
class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"


# Class: PhDStudent (Multiple Inheritance)
class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        # Call constructors of both parent classes
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self):
        return f"StudentID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}"


# Creating objects
student = Student(101,42)
faculty = Faculty(555,42)
phd = PhDStudent(101, 555, 42)

# Output
print(student.get_info())
print(faculty.get_info())
print(phd.get_info())
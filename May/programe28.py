#Setter and property decorater 
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email =f"{fname}.{lname}@shivamtamboli23@gmail.com"

    def explain(self):
        return f"This is an employee: {self.fname} {self.lname}"

    def printemail(self):
        pass

Shivam_tamboli = Employee("Shivam", "tamboli")
Satyam_tamboli = Employee("Satyam", "tamboli")

print(Shivam_tamboli.explain())





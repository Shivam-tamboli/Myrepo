 # Created a class. 
class Student:
        # Numbers 0f subjects for every students.
    no_of_subject = 5
    

# Two instance of class name Students.
# first instance name is Shivam.
Shivam = Student()
# Second instance name is satyam.
Satyam = Student()

# Shivam's name.
Shivam.name = "Shivam"
# Shivam's age
Shivam.age = 20
# Shivam's id.
Shivam.id_no_ = 211015035
# Shivam's subject
Shivam.no_of_subject = 5
# Shivam's cource.
Shivam.Cource = "BCA"
# Shivam's branch.
Shivam.branch = "Computer scince"

# Satyam's name.
Satyam.name = "Satyam"
# Satyam age.
Satyam.age = 19
# Satyam's id_no.
Satyam.id_no_ = 211015674
# Sataym's subjects
Satyam.no_of_subject = 5
# Satyam cource.
Satyam.cource = "B.tech "
# Satyam branch
Satyam.branch ="AI(Airtificial intelligance)"

# Printing shivam's details in a dictionary form.
print(Shivam.__dict__)
# Printing satyam's details in a dictionary form.
print(Satyam.__dict__)

# Expected output.
# {'name': 'Shivam', 'age': 20, 'id_no_': 211015035, 'no_of_subject': 5, 'Cource': 'BCA', 'branch': 'Computer scince'}
# {'name': 'Satyam', 'age': 19, 'id_no_': 211015674, 'no_of_subject': 5, 'cource': 'B.tech ', 'branch': 'AI(Airtificial intelligance)'}

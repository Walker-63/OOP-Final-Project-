# patient class

class Patient:

    def __init__(self, id, name, age, gender, diagnosis):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Diagnosis: {self.diagnosis}")

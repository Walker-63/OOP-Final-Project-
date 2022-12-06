# Hospital Assignment
# Elijah Buchanan
import patient as p


def displayPatientsList():

    with open("patients.txt", "r",) as file:
        for line in file:
            patientListFile = line.strip().split(",")
            print(str(patientListFile).replace("['", "").replace("']", "").replace("_", " "))


def searchPatientById(x):
    y = str(x)
    with open("patients.txt", "r",) as file:
        for line in file:
            if line[0] == y[0] and line[1] == y[1]:
                print(line.replace("_", ", "))
                break


def patient_menu():
    x = -1
    while x != 0:
        print("Patient Menu\n"
              "0 - Return to Main Menu\n"
              "1 - Display patient's list\n"
              "2 - Search for patient by ID")

        x = int(input("Enter option: "))

        if x == 1:
            displayPatientsList()
        elif x == 2:
            patient_id = int(input("Enter patient ID: "))
            searchPatientById(patient_id)


patient_menu()

from _datetime import datetime
from enum import Enum

class Admin:
    def __init__(self):
        self.__doctors = list()
        self.__patients = list()

    def get_doctors_list(self):
        return len(self.__doctors)

    def add_doctor_to_list(self, id_number: int, first_name: str, last_name: str, speciality: str) -> None:
        self.__doctors.append(Doctor(id_number, first_name, last_name, speciality))

    def delete_doctor_from_list(self, id_number: int, name: str) -> none:
        for doctor in self.__doctors:
            if doctor.id == id_number and doctor.first_name == name:
                self.__doctors.remove(doctor)

    def view_doctors_detail_in_list(self, id_number: int, name: str) -> str:
        for doctor in self.__doctors:
            if doctor.id == id_number and doctor.first_name == name:
                return f"{doctor.id} {doctor.first_name} {doctor.last_name}"
        return "Detail not found"

    def register_a_patient(self, patient_id: int,first_name: str, last_name: str, gender, dob, phone: str) -> None:
        self.__patients.append(Patient(patient_id, first_name, last_name, gender, dob, phone))

    def delete_patient_from_list(self, id_number: int, first_name: str) -> None:
        for patient in self.__patients:
            if patient.id == id_number and patient.first_name == first_name:
                self.__patients.remove(patient)


    def get_patient_list(self) -> int:
        return len(self.__patients)

class Contact:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, full_name: str, last_name: str) -> None:
        if full_name.isalpha and last_name.isalpha():
            self.first_name = full_name
            self.last_name = last_name
        else:
            raise ValueError("name must contain only alphabets")

    @full_name.getter
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Doctor(Contact):
    def __init__(self, id: int, first_name: str, last_name: str, speciality: str):
        super().__init__(id, first_name, last_name)
        self.speciality = speciality

        def __str__(self):
            return f'{self.doctors_id} {self.first_name} {self.last_name} {self.speciality}'

class Patient(Contact):
    def __init__(self, id: int, first_name: str, last_name: str, gender: str, dob: str, phone_number: str):
        super().__init__(id, first_name, last_name)
        self.gender = Gender
        self.date_of_birth = dob
        self.phone_number = phone_number

    @property
    def patients_gender(self):
        return gender

    @patients_gender.setter
    def patients_gender(self, gender):
        if gender == "M".lower() or gender == "MALE".lower():
            self.gender = Gender.MALE
        elif gender == "F".lower() or gender == "FEMALE".lower():
            self.gender = Gender.MALE
        else:
            raise ValueError("gender must be MALE or FEMALE")




    def __str__(self):
        return f'{self.patient_id} {self.first_name} {self.last_name} {self.phone_number} {self.email}'

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class MedicalHistory:
    def __init__(self, past_illness: str, current_illness: str, allergies: str, medication: str):
        self.past_illness = past_illness
        self.present_illness = current_illness
        self.allergies = allergies
        self.medications = medication

class Appointment:
    def __init__(self):
        self.date_time = datetime.now()
        self.status = status
        self.reason = reason
        self.location = location
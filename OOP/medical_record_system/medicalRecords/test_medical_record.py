from medicalRecords import medical_record
from unittest import TestCase

class Test(TestCase):

    def test_that_doctors_list_is_empty(self):
        records = medical_record.Admin()
        self.assertEqual(records.get_doctors_list(), 0)

    def test_that_doctors_list_is_not_empty(self):
        records = medical_record.Admin()
        records.add_doctor_to_list(17, "Emma", "Adah", "Neuro-surgeon")
        self.assertEqual(records.get_doctors_list(), 1)

    def test_that_doctor_can_be_deleted_from_list(self):
        records = medical_record.Admin()
        records.add_doctor_to_list(17, "Emma", "Adah", "Neuro-surgeon")
        records.delete_doctor_from_list(17, "Emma")
        self.assertEqual(records.get_doctors_list(), 0)

    def test_that_admin_can_view_doctors_details(self):
        records = medical_record.Admin()
        records.add_doctor_to_list(17, "Emma", "Adah", "Neuro-surgeon")
        records.view_doctors_detail_in_list(17, "Emma")
        self.assertEqual(records.view_doctors_detail_in_list(17, "Emma"), "17 Emma Adah")

    def test_that_patients_list_is_empty(self):
        records = medical_record.Admin()
        self.assertEqual(records.get_patient_list(), 0)

    def test_that_admin_can_add_patients_to_list(self):
        records = medical_record.Admin()
        records.register_a_patient(17, "Emma", "Adah", "M", "12, 05, 1998","08160509785")
        self.assertEqual(records.get_patient_list(), 1)

    def test_that_admin_can_delete_patients_from_list(self):
        records = medical_record.Admin()
        records.register_a_patient(17, "Emma", "Adah", "M", "12, 05, 1998","08160509785")
        records.delete_patient_from_list(17, "Emma")
        self.assertEqual(records.get_patient_list(), 0)

        records.register_a_patient(17, "Emma", "Adah", "M", "12, 05, 1998", "08160509785")
        records.register_a_patient(18, "James", "Tauri", "M", "13, 08, 1997","09056885545")
        records.register_a_patient(19, "John", "Sleeps", "M", "04, 10, 1994","08160507485")
        records.delete_patient_from_list(18, "James")
        self.assertEqual(records.get_patient_list(), 2)


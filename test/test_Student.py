import unittest

from class_definitions import Student as t


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.student = t.Student('Alvarado', 'Alex', 'English', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "Alex")
        self.assertEqual(self.student.last_name, "Alvarado")
        self.assertEqual(self.student.major, "English")
        self.assertEqual(self.student.gpa, 4.0)

    def test_object_created_all_attributes(self):
        student = t.Student("McDonald", "Ronald", "Chem", 4.0)
        assert student.last_name == "McDonald"
        assert student.first_name == "Ronald"
        assert student.major == "Chem"
        assert student.gpa ==4.0

    def test_student_st(self):
        self.assertEqual(str(self.student), "Alvarado, Alex has major English with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student("1234sfd", "Alex", "English", 4.0)


    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Alvarado", "Alex1234", "English", 4.0)


    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Jackson", "Percy", "Spell", 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Jackson", "Percy", "CompSci", 4.5)

if __name__ == '__main__':
    unittest.main()

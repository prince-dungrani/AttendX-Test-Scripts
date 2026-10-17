
import unittest

# Sample attendance logic for demonstration.
# A real app would save attendance through its backend.

def mark_attendance(student_id, attendance_records):
    if not student_id:
        return "Student ID is required"
    if student_id in attendance_records:
        return "Attendance already marked"

    attendance_records.add(student_id)
    return "Attendance marked successfully"


class AttendanceTest(unittest.TestCase):

    def setUp(self):
        self.records = set()

    def test_mark_attendance(self):
        self.assertEqual(
            mark_attendance("STU101", self.records),
            "Attendance marked successfully"
        )

    def test_duplicate_attendance(self):
        self.records.add("STU101")
        self.assertEqual(
            mark_attendance("STU101", self.records),
            "Attendance already marked"
        )

    def test_empty_student_id(self):
        self.assertEqual(
            mark_attendance("", self.records),
            "Student ID is required"
        )


if __name__ == "__main__":
    unittest.main()

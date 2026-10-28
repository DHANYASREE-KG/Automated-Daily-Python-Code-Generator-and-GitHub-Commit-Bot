"""
Student Grading System.

Tracks grades across courses and computes overall GPA.
"""


class Student:
    """Represents a student with grades in multiple courses."""

    GRADE_POINTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses: dict[str, str] = {}  # course_code -> letter_grade

    def add_grade(self, course: str, grade: str) -> None:
        grade = grade.upper()
        if grade not in self.GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")
        self.courses[course] = grade

    def calculate_gpa(self) -> float:
        if not self.courses:
            return 0.0
        total_pts = sum(self.GRADE_POINTS[g] for g in self.courses.values())
        return total_pts / len(self.courses)


if __name__ == "__main__":
    print("=== Student GPA Tracker ===")
    s = Student("STU101", "Alex")
    s.add_grade("CS101", "A")
    s.add_grade("MATH201", "B")
    s.add_grade("ENG102", "A")

    print(f"Student: {s.name}")
    print(f"Courses: {s.courses}")
    print(f"GPA    : {s.calculate_gpa():.2f}")

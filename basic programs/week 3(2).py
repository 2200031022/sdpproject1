class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student_obj = Student(1, "John Doe")
student_obj.student_class = "Grade 10"

print("Attributes and Values Before Removal:")
print(vars(student_obj))

del student_obj.student_name

print("\nAttributes and Values After Removal:")
print(vars(student_obj))

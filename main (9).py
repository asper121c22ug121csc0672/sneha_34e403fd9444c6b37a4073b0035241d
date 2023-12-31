class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(Student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(Student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  # syntax - lambda arg:exp
  return sorted_students


# Example usage:
students =[
    Student("Har", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saunya", "A125", 9.1),
    Student("Mahindhar", "A126", 9.9),
]

Sorted_students = sort_students(students)

# Print the sorted list of students
for student in Sorted_students:
  print("Name: {},Roll Number: {}, CGPA: {}".format(student.name,
                                                                          student.roll_number,
                                                    student.cgpa))
  




# declare and fill out function here
def youngest_student(students):
  youngest = None
  age = float('inf')
  for key in students:
    if students[key] < age:
        age = students[key]
        youngest = key
  return youngest


# test case
students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student2(students))  # Expected output: "Alice"

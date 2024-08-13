# declare and fill out function here
def youngest_student(students):
  youngest = float('inf')
  for key, val in students.items():
      if val < youngest:
          youngest = val
      return key


# test case
students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student2(students))  # Expected output: "Alice"

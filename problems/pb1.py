# declare and fill out function here

def replace_spaces(s, c):
  return s.replace(" ", c)

# test case
sentence = "Test  This is a test   Testing "
sentence2 = replace_spaces(sentence, "_")
print(sentence2) # -> Test__This_is_a_test__Testing_

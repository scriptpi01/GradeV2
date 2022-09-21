#Input
student_id = str(input("Enter student's ID : "))
student_name = str(input("Enter student's name : "))
student_faculty = str(input("Enter student's faculty : "))
subject_amount = int(input("Enter subjects Amount : "))

#Declare Variable
subject_list = []
credit_list = []
grade_list = []
GPA = 0
sum_credit = 0

#Loop_input
for i in range(subject_amount):
  subject = str(input("Enter Subject #%d : "%(i+1)))
  credit = eval(input("Enter Credit : "))
  grade = str(input("Enter Grade : "))
  

  #Grade_Table
  if grade.upper() == 'A':
    grade_point = 4
  elif grade.upper() == 'B+':
    grade_point = 3.5
  elif grade.upper() == 'B':
    grade_point = 3
  elif grade.upper() == 'C+':
    grade_point = 2.5
  elif grade.upper() == 'C':
    grade_point = 2
  elif grade.upper() == 'D+':
    grade_point = 1.5
  elif grade.upper() == 'D':
    grade_point = 1
  elif grade.upper() == 'F':
    grade_point = 0
  elif grade.upper() == 'W':
    grade_point = 0
  else:
    grade = 'Error'

  #Append_to_list
  subject_list.append(subject)
  credit_list.append(credit)
  grade_list.append(grade)


  #GPA_Compute
  GPA += credit*grade_point
  if i <= subject_amount-1:
    if grade.upper() == 'W':
      sum_credit += 0
    else:
      sum_credit += credit
GPA = GPA/sum_credit


#Output
print('='*63)
print('%s%39s%23s'%('|', 'Grade Calculator', '|'))
print('='*63)
print('Student ID. : %s'%(student_id))
print('Name : %s'%(student_name))
print('School : %s'%(student_faculty))
print('='*63)
print('%s%22s%14s%11s%3s%8s%4s'%('|', 'Subject', '|', 'Credit(s)', '|', 'Grade', '|'))
print('='*63)
for i in range(subject_amount):
  if grade_list[i] == 'Error':
    print('%-37s%7s%10s%s%-8s'%(subject_list[i], credit_list[i], ' ', grade_list[i].upper(), ' '))
    GPA = 'Error'
  else:
    print('%-37s%7s%12s%s%-8s'%(subject_list[i], credit_list[i], ' ', grade_list[i].upper(), ' '))
print('='*63)
if GPA == 'Error' :  
  print('%s%30s %-6s %24s'%('|', 'GPA', GPA, '|'))
else:
  print('%s%30s %4.2f %26s'%('|', 'GPA', GPA, '|'))
print('='*63)
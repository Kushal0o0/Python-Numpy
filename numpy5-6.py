import numpy
from numpy import random

# manipulating numpy array
array = numpy.array([1,2,3,4])
print(array)

array[0] = 10   # access the zeroth index and replace it with "10"
print(array)

array = numpy.arange(2, 50)
array1 = array.reshape(6, 8)
print(array1)

array1[3][3] = 0
print(array1)

array1[:, 0] = [1, 2, 3, 4, 5, 6]
print(array1)

array1[:, -3:] = [1]
print(array1)
########################################################################################################################
########################################################################################################################

# operations with numpy array
students_array = numpy.array([['Student_1', 59, 64, 94, 87, 81],

                              ['Student_2', 8, 56, 18, 58, 69],

                              ['Student_3', 7, 20, 60, 63, 42],

                              ['Student_4', 71, 94, 71, 68, 13],

                              ['Student_5', 89, 1, 16, 33, 40],

                              ['Student_6', 4, 25, 48, 41, 84],

                              ['Student_7', 3, 79, 46, 9, 71],

                              ['Student_8', 87, 77, 75, 15, 69],

                              ['Student_9', 61, 1, 48, 98, 23],

                              ['Student_10', 98, 60, 24, 66, 56],

                              ['Student_11', 58, 12, 75, 7, 98],

                              ['Student_12', 23, 62, 6, 35, 37],

                              ['Student_13', 14, 25, 87, 56, 8],

                              ['Student_14', 68, 1, 81, 11, 61],

                              ['Student_15', 11, 69, 35, 17, 66]], dtype=object)

# number of students who have scored higher in subjectA than in subjectB
a = students_array[:, 1]
print("A", a)
b = students_array[:, 2]
print("B", b)
greater = a > b

print(len(students_array[greater]), "Students have scored higher in A than in B")
print(students_array[greater, :3])

# what is the average marks scored in subject "A" and "C"
a = students_array[:,1]
print(a)
print(a.mean())
c = students_array[:, 2]
print(c)
print(c.mean())

# number of students who have scored higher than student 15 in both subjects "A" and "B"
stu15a = students_array[14][1]   # marks of student 15 subject "A" stored
print(stu15a)
stu15b = students_array[14][2]   # marks of student 15 subject "B" stored
print(stu15b)

suba = students_array[:, 1]      # column containing subject a marks of all students
print(suba)
subb = students_array[:, 2]      # column containing subject b marks of all students
print(subb)

greater = (suba > stu15a) & (subb > stu15b)    # compare
print(students_array[greater])
print(len(students_array[greater]), "students have  scored higher than student 15 in both subjects 'A' and 'B'")

# average marks scored by students 4-10
students = students_array[3:10]
marks = students[:, 1:]
print(marks)

average = marks.mean(axis=1)    # axis 1 = column wise (average marks of each student)
print(average)

# number of people who scored more than 20 in subject "A"
marks = students_array[:, 1]
print(marks)
greater = marks > 20
print(sum(greater), "students have subject A marks greater than 20")
print(students_array[greater][:, 0:2])

# total score of subject A
suba = students_array[:, 1]
print(sum(suba))

# unique
arr = numpy.array(["a", "b", "b", "c", "a", "c", "d", "c"])
print(numpy.unique(arr))
print(numpy.unique(arr, return_index=True))
########################################################################################################################

# broadcasting array
a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([10, 11, 12, 13, 14])
c = a * b
print(c)









########################################################################################################################
# LMS problems
banking_array = numpy.array([[30.0, 'unemployed', 'married', 1787.0, 'no', 'no', 'cellular','oct'],

       [33.0, 'services', 'married', 4789.0, 'yes', 'yes', 'cellular','may'],

       [35.0, 'management', 'single', 1350.0, 'yes', 'no', 'cellular','apr'],

       [30.0, 'management', 'married', 1476.0, 'yes', 'yes', 'unknown','jun'],

       [59.0, 'blue-collar', 'married', 0.0, 'yes', 'no', 'unknown','may'],

       [35.0, 'management', 'single', 747.0, 'no', 'no', 'cellular','feb'],

       [36.0, 'self-employed', 'married', 307.0, 'yes', 'no', 'cellular','may'],

       [39.0, 'technician', 'married', 147.0, 'yes', 'no', 'cellular','may'],

       [41.0, 'entrepreneur', 'married', 221.0, 'yes', 'no', 'unknown','may'],

       [43.0, 'services', 'married', -88.0, 'yes', 'yes', 'cellular','apr'],

       [39.0, 'services', 'married', 9374.0, 'yes', 'no', 'unknown','may'],

       [43.0, 'admin.', 'married', 264.0, 'yes', 'no', 'cellular', 'apr'],

       [36.0, 'technician', 'married', 1109.0, 'no', 'no', 'cellular','aug'],

       [20.0, 'student', 'single', 502.0, 'no', 'no', 'cellular', 'apr'],

       [31.0, 'blue-collar', 'married', 360.0, 'yes', 'yes', 'cellular','jan'],

       [40.0, 'management', 'married', 194.0, 'no', 'yes', 'cellular','aug'],

       [56.0, 'technician', 'married', 4073.0, 'no', 'no', 'cellular','aug'],

       [37.0, 'admin.', 'single', 2317.0, 'yes', 'no', 'cellular', 'apr'],

       [25.0, 'blue-collar', 'single', -221.0, 'yes', 'no', 'unknown','may'],

       [31.0, 'services', 'married', 132.0, 'no', 'no', 'cellular','jul']], dtype=object)

# What is the total bank balance of the first 5 records from the data?
"""bank = banking_array[0:5][:, 3]
print(sum(bank))"""

# What is the average bank balance?
"""bank = banking_array[:, 3]
print(bank.mean())"""

# Count the number of people who has a housing?
housing = banking_array[:, 4] == "yes"
print(len(banking_array[housing]))

# Count the number of people who has a loan?
"""loan = banking_array[:, 5]
yes = loan == "yes"
print(len(loan[yes]))"""

# No of people who have a "cellular" contact and also "married" and hold a "management" job?
"""cell = banking_array[:, 6]
marriage = banking_array[:, 2]
job = banking_array[:, 1]

cond = (cell == "cellular") & (marriage == "married") & (job == "management")
print(len(banking_array[cond]))"""

# Find the total balance of the customers aged between 25 and 40(both inclusive).
"""age = banking_array[:, 0]
age1 = (age >= 25) & (age <= 40)

salary = banking_array[age1][:, 3]
print(salary.sum())"""

# No of people who are single but have more than average bank balance?
"""bank = banking_array[:, 3]
av_bank = bank.mean()
print(av_bank)

single = banking_array[:, 2]
single1 = single == "single"
single_people = banking_array[single1][:, 2:4]
salarie = single_people[:, 1]

print(sum(salarie > av_bank))"""

# Company has decided to give a bonus of 5% of their account balance to those account holders whose age is
# more than or equal to 55 years and whose account balance is more than 2000.
# Calculate the sum of the total bank balance to the account holders(mentioned above) after crediting their bonus amount.

"""age_balance = (banking_array[:, 3] > 2000) & (banking_array[:, 0] >= 55)
more_than_2k = banking_array[age_balance]

sal = more_than_2k[:, 3]
bonus = (0.05 * sal) + sal
print(more_than_2k)
print("bonus", bonus)"""

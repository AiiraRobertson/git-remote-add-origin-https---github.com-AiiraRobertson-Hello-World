import math
student_count = 1000
ratings = 4.88
is_published = True
course_name = "Python Programming"
print(student_count)
print(ratings)
print(is_published)
print(course_name)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0::2])
print(course_name[:])
print(course_name[::3])
print(course_name.upper())
print(course_name.lower())
print(course_name[-2:6])

# adding escape sequence \n and \t
course_description = "Learn Python Programming.\nStart your journey today!\tIt's fun and exciting."
print(course_description)

# adding \"
quote = "He said, \"Learning Python is awesome!\""
print(quote)

# i want to print my full name by concatenating first and last name
first = "Ifiok"
last = "Akpan"
full_name = first + " " + last
print(full_name)

# using f-string to format
full_name_fstring = f"{first} {last} {2 + 3}"
print(full_name_fstring)

# using string methods
course = "   Python for Beginners   "
print(course.strip())
print(course.find("for"))
print(len(course))

# numbers
# we have three types of numbers in python
# integer, float, complex

print(round(2.9))
print(abs(-2.9))
print(pow(3, 4))  # 3 to the power of 4
print(3 ** 4)    # 3 to the power of 4
print(10 // 3)   # floor division
print(10 % 3)    # modulus
print(math.ceil(2.1))
print(math.floor(2.9))
print(math.sqrt(16))
print(math.gcd(48, 18))
print(math.pi)

x = input("x: ")
print(type(x))

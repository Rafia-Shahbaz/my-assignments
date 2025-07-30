#Define a class Student with attributes name, age, score. Create an instance and print its attributes.Override the _str_() method in Student class to return a custom string.
class Student:
    school = "GUJAR AI School"
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def display_info(self):
        print(f"{self.name} is {self.age} years old and scored {self.score}.")
    def has_passed(self):
        return self.score >= 50
    def __str__(self):
        return(f"{self.name}, ({self.age} years), Score: {self.score}")
student = Student("Ahmad", 17, 89)
print(student)
print(student.name)
print(student.age)
#Add a method display_info() to Student to print a sentence about the student.
student.display_info()
#Define a method has_passed() that returns True if score >= 50, else False.
print(student.has_passed())
#Create a second class Teacher with name, subject, and a method teach(). Instantiate and call its method.
class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
teacher = Teacher("Mr. Faizan", "Python")
teacher.teach()
#Modify Student class to include a class variable school = "GUJAR AI School" and print it from instances.
print(student.school)
#Create two student objects and compare if they are instances of Student using isinstance().
s = Student("Noor", 16, 97)
print(isinstance(s, Student))
print(isinstance(student, Student))
#Create a Course class with attributes title and students (a list). Add a method to add students.Write a method in Course to compute the average score of enrolled students.
class Course:
    def __init__(self,title):
        self.title = title
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def average_score(self):
        if not self.students:
            return 0
        total = sum(student.score for student in self.students)
        return total / len(self.students)
course = Course("Python Programming")
course.add_student(student)
course.add_student(s)
print("Average Score:", course.average_score())
#Use the dir() function to list attributes & methods of an instance of any class.
print(dir(student))
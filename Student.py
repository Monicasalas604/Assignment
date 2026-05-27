class Student:
    def __init__(self, student_id, student_name, credits_max):
        self.student_id = student_id
        self.student_name = student_name
        self.credits_max = credits_max
        self.credits_current = 0
        self.enroll_courses = []

    def credits_left(self):
        return self.credits_max - self.credits_current

    def add_courses(self, course):
        if self.credits_max  <= 0:
            raise ValueError("The total amount of credits can only be positive") 
            
        if self.credits_max > self.credits_current:
            self.enroll_courses.append(course)
            self.credits_current =+ self.credits_current
        else:
            print ("Total amount of credits fulfeel, you can´t add more classes")

    def delete_course(self, courses):
        if self.credits_max > self.credits_current:
            self.enroll_courses.remove(course)
            self.credits_current =- self.credits_current

    def visualize_course_info(self):
        for course in self.enroll_courses:
            print(f"Course {course.course_name} ({course.course_id}): ({course.course_credits} credits)")
            
class Course:
    def __init__(self, course_id, course_name, course_capacity, course_credits):
        self.course_id = course_id
        self.course_name = course_name
        self.course_capacity = course_capacity
        self.course_credits = course_credits
        self.enroll_students = []

    def is_full(self):
        if self.course_capacity  <= 0:
            raise ValueError("The total course capacity can only be positive")
            
        if len(self.enroll_students) >= self.course_capacity:
            return ("Course full, accepting no more students")

    def add_student(self, student):
        if not self.is_full() and student not in self.enroll_students:
            self.enroll_students.append(student)

    def delete_student(self, student):
        if student in self.enroll_students:
            self.enroll_students.remove(student)

class RegistrationSystem:
    def __init__(self):
        self.all_courses = []
        self.all_students = []

    def enrolled_students_in_course(self, course):
        return course.enroll_students
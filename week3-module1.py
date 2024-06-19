import torch, math

#Exercise 1
class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def __call__(self, tensor: torch.Any):
        self.tensor = tensor
        denominator = sum([math.exp(self.tensor[i]) for i in range(len(self.tensor)])
        for _ in range(len(self.tensor)):
            self.tensor[_] = math.exp(self.tensor[_]) / denominator
        return self.tensor
    
    
class Softmaxstable(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def __call__(self, tensor: torch.Any):
        self.tensor = tensor
        c = max(self.tensor)
        denominator = sum([math.exp(self.tensor[i] - c) for i in range(len(self.tensor))])
        for _ in range(len(self.tensor)):
            self.tensor[_] = math.exp(self.tensor[_] - c) / denominator
        return self.tensor
        
#Exercise 2

class Ward:
    def __init__(self, name) -> None:
        self.people = []
        self.name = name
    
    def add_person(self, person):
        self.people.append(person)
    
    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.people:
            person.describe()
    
    def count_doctor(self):
        total = 0
        for person in self.people:
            if person.profession == "doctor":
                total += 1
        return total

    def sort_age(self):
        yobs = [person.yob for person in self.people]
        yobs.sort(reverse=True)
        for i in range(len(yobs)):
            for person in self.people:
                if person.yob == yobs[i]:
                    yobs[i] = person
        self.people = yobs
    
    def compute_average(self):
        yobs_teacher = [person.yob for person in self.people if person.profession == "teacher"]
        return sum(yobs_teacher) / len(yobs_teacher)
    
    
class Person:
    def __init__(self, name, yob, *args):
        self.name = name
        self.yob = yob
        
    def describe(self):
        self.parts = [f"Name: {self.name}", f"YoB: {self.yob}"]    
        
        
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
        self.profession = "student"
        
    def describe(self):
        super().describe()
        self.parts.insert(0, "Student")
        self.parts.append(f"Grade: {self.grade}")
        print(" - ".join(self.parts))
        
        
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
        self.profession = "teacher"
       
    def describe(self):
        super().describe()
        self.parts.insert(0, "Teacher")
        self.parts.append(f"Subject: {self.subject}")
        print(" - ".join(self.parts))

        
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
        self.profession = "doctor"
               
    def describe(self):
        super().describe()
        self.parts.insert(0, "Doctor")
        self.parts.append(f"Specialist: {self.specialist}")
        print(" - ".join(self.parts))
        
#EXERCISE 3

class Stack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stack_list = []
    
    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False
        
    def is_full(self):
        if len(self.stack_list) == self.capacity:
            return True
        else:
            return False
    
    def pop(self):
        result = self.stack_list[0]
        self.stack_list = self.stack_list[1:]
        return result
    
    def push(self, value):
        self.stack_list.insert(0, value)
    
    def top(self):
        return self.stack_list[0]
    
#EXERCISE 4


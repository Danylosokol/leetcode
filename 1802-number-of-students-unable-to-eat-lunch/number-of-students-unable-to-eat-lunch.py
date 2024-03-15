class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        print(students)
        print(sandwiches)
        result = 0
        sandwichesCounter = {}
        studentsCounter = {}
        for i in range(len(students)):
            student = students[i]
            sandwich = sandwiches[i]
            sandwichesCounter[sandwich] = sandwichesCounter.get(sandwich, 0) + 1
            studentsCounter[student] = studentsCounter.get(student, 0) + 1
        print("I after while:")
        if not sandwiches:
            return len(students)
        elif (0 not in studentsCounter and sandwiches[0] == 0) or (1 not in studentsCounter and sandwiches[0] == 1):
            return len(students)

        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            return self.countStudents(students, sandwiches)
        else:
            print("first element")
            removed_student = students.pop(0)
            print(removed_student)
            students.append(removed_student)
            return self.countStudents(students, sandwiches)
        
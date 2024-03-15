class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        studentsCounter = {}

        if not sandwiches:
            return len(students)

        for i in range(len(students)):
            student = students[i]
            studentsCounter[student] = studentsCounter.get(student, 0) + 1
        print("I after while:")

        if (0 not in studentsCounter and sandwiches[0] == 0) or (1 not in studentsCounter and sandwiches[0] == 1):
            return len(students)

        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            return self.countStudents(students, sandwiches)
        else:
            removed_student = students.pop(0)
            students.append(removed_student)
            return self.countStudents(students, sandwiches)
        
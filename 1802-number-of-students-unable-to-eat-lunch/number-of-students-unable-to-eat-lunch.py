class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        studentsCounter = {}

        if not sandwiches:
            return len(students)

        requiredStudent = 0 if sandwiches[0] == 0 else 1
        i = 0
        while i < len(students):
            if students[i] == requiredStudent:
                break
            i += 1

        if i == len(students):
            return len(students)

        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            return self.countStudents(students, sandwiches)
        else:
            removed_student = students.pop(0)
            students.append(removed_student)
            return self.countStudents(students, sandwiches)
        
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
            Comparing 0 index values of both stack and queue if they didn't match
            go into else condition and append that element of students at the last 
        '''
        
        current = 0
        
        while students:
            if students[0] == sandwiches[0]:
                current = 0
                students.pop(0)
                sandwiches.pop(0)
                
            else:
                current += 1
                students.append(students.pop(0))
            '''
                This code will run when some students are left and now students and sandwiches if              condition doesn't work because in students there are either are 1/0 lefts and in sandwiches
         they have either 0 or 1 at the start which students don't have then else condition will run
         until current lenght is equal to students length
            '''    
            if current == len(students):
                break
                
        return len(students)
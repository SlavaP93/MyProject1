class Student:
    students_lst = list()

    def __init__(self, name, second_name, group, estimation):
        self.students_lst.append([name,second_name,group,estimation])


    def quic_sort_stud(self):
        def custom(lst):
            return lst[-1]
        self.students_lst.sort(key=custom)
        return self.students_lst


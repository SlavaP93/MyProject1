from Sort_student import Student


student_1 = Student('Ivan', 'Mic', 103, 4.5)
student_2 = Student('Petya', 'Hoc', 103, 4.2)
student_3 = Student('Sveta', 'vdfv', 102, 3.3)
student_4 = Student('feaw', 'fasd', 103, 4.9)
student_5 = Student('Nastya', 'cjc', 102, 4.6)
student_6 = Student('Eka', 'Rtye', 102, 4.1)
student_7 = Student('nvb', 'mnbc', 103, 2)
student_8 = Student('Sasha', 'BVV', 103, 5)
students = student_7.quic_sort_stud()
for _, i_stud in enumerate(students):
    print("Имя:", ' '.join(i_stud[:2]), "Группа:", ''.join(str(i_stud[2])), 'Оценка:', ''.join(str(i_stud[3])))
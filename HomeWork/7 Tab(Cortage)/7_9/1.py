students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },

    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def func_stud(dict):
    stud_list = []
    string = ''
    for i_data, _ in dict.items():
        stud_list += dict[i_data]['interests']
        string += dict[i_data]['surname']
    return stud_list, len(string)


pairs = dict()
for id_stud, age in students.items():
    pairs[id_stud] = age['age']

print(pairs)

my_list, lenth = func_stud(students)
print(my_list, lenth)

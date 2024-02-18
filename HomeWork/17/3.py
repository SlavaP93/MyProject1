class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

people = [
    Person("Alice", 30, city="New York", country="USA"),
    Person("Bob", 25, city="London", country="UK"),
    Person("Charlie", 35, city="Paris", country="France")
]

# Отсортировать по возрасту (убывание)
sorted_people_desc = sorted(people, key=lambda x: x.age, reverse=True)

# Отсортировать по возрасту (возрастание)
sorted_people_asc = sorted(people, key=lambda x: x.age)

print("Отсортированные по возрасту (убывание):")
print(sorted_people_desc)
print("\nОтсортированные по возрасту (возрастание):")
print(sorted_people_asc)
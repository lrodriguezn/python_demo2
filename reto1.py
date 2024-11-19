
persons = [{"name": "John", "age": 21, "salary": 1000},
    {"name": "Jane", "age": 22, "salary": 2000},
    {"name": "Jack", "age": 23, "salary": 3000},
    {"name": "Jill", "age": 24, "salary": 4000},
    {"name": "Bob", "age": 25, "salary": 5000},
    {"name": "Alice", "age": 26, "salary": 6000}
    ]

def filter_by_salary(persons, salary):
    return [person for person in persons if person['salary'] > salary]

print(filter_by_salary(persons, 3000))
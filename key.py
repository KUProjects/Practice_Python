

people = [
    {"NAME": "FARH", "AGE": "two"},
    {"NAME": "HUSSEIN", "AGE": "tjree"},
]

def f(person):
    return person ["NAME"] + " is " + person["AGE"] + " years old"

people.sort(key=f)
print(people)
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

p1: Person={'name':'ray', 'age':25}
p2: Person={'name':'vik', 'age':'twenty-seven'}

print(p1)
print(p2)
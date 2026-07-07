from dataclasses import dataclass
from uuid import uuid4
@dataclass
class Person:
    id: str
    name: str
    age: int
    country: str

    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am from {self.country}.")


person1 = Person(
    id=str(uuid4()),
    name="Chris",
    age=22,
    country="Canada"
)

person1.greet()

print(person1.id)


#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @classmethod
    def cobble(cls):
        print("Your shoe is as good as new!")
        cls.condition = "New"

nike = Shoe("Nike", 10)
nike.cobble()
print(nike.condition)
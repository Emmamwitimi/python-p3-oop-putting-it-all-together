#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will use the setter method
    
    # Getter method for size
    def get_size(self):
        return self._size
    
    # Setter method for size with validation
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    # Define size property
    size = property(get_size, set_size)
    
    # Method to repair the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


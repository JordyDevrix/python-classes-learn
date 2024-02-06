class Reken:

    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def substract(self):
        return self.value_a - self.value_b

    def multiply(self):
        return self.value_a * self.value_b

    def divide(self):
        return self.value_a / self.value_b

    def count(self):
        return self.value_a + self.value_b

    def power(self):
        return self.value_a ** self.value_b

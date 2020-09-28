# Basic method of setting and getting attributes in Python
class Celsius:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Making Getters and Setter methods
class CelsiusWithGetterAndSetters:

    def __init__(self, temperature=0):
        self.set_temperature(temperature)
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# using property class
class CelsiusWithPropertyClass:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        # print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        # print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


# Using @property decorator
class CelsiusWithPropertyDecorator:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        # print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

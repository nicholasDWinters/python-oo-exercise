"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        '''Initializes the start variable as well as a counter variable starting at 0'''
        self.start = start
        self.counter = 0

    def __repr__(self):
        return f'<SerialGenerator start={self.start + self.counter} next={self.start + self.counter + 1}>'

    def generate(self):
        '''Adds one to the counter variable and returns the starting number plus our counter'''
        self.counter += 1
        return self.start + self.counter

    def reset(self):
        '''Resets the counter variable'''
        self.counter = 0

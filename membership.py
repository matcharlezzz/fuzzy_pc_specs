from flask import Flask

class TrapMF:

    def __init__(self, min_x, max_x, peak_start, peak_end, peak_y):
        self.min_x = min_x
        self.peak_start = peak_start
        self.peak_end = peak_end
        self.max_x = max_x
        self.peak_y = peak_y

        self.min_slope = self.slope(min_x, 0, peak_start, peak_y)
        self.min_intercept = self.min_slope * -min_x
        self.max_slope = self.slope(peak_end, peak_y, max_x, 0)
        self.max_intercept = self.max_slope * -max_x

        pass

    def slope(self, x1, y1, x2, y2):
        s = (y2-y1)/(x2-x1)
        return s
    def get_output(self, input):
        if input < self.min_x:
            return 0
        elif self.min_x <= input and input < self.peak_start:
            return self.min_slope * input + self.min_intercept
        elif self.peak_start <= input and input < self.peak_end:
            return self.peak_y
        elif self.peak_end <= input and input <= self.max_x:
            return self.max_slope * input + self.max_intercept
        elif input > self.max_x:
            return 0

   
class TriMF:

    def slope(self, x1, y1, x2, y2):
        s = (y2-y1)/(x2-x1)
        return s

    def __init__(self, min_x, peak_x, max_x, peak_y):
        self.min_x = min_x
        self.max_x = max_x
        self.peak_x = peak_x
        self.peak_y = peak_y

        self.min_slope = self.slope(min_x, 0, peak_x, peak_y)
        self.min_intercept = self.min_slope * -min_x
        self.max_slope = self.slope(peak_x, peak_y, max_x, 0)
        self.max_intercept = self.max_slope * -max_x

    def get_output(self, input):
        if input < self.min_x:
            return 0
        elif self.min_x <= input and input < self.peak_x:
            return self.min_slope * input + self.min_intercept
        elif self.peak_x == input:
            return self.peak_y
        elif self.peak_x < input and input <= self.max_x:
            return self.max_slope * input + self.max_intercept
        elif input > self.max_x:
            return 0



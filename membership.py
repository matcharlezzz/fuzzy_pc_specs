from flask import Flask

class TrapMF:

    def __init__(self, min_x, peak_start, peak_end, max_x, peak_y):
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
        
class PCSpecsMembership:

    #Budget
    entry = TrapMF(9999.9999, 10000,20000,30000,1)
    entry_mid = TriMF(20000, 40000, 60000, 1)
    mid_high = TriMF(50000, 65000, 80000, 1)
    high = TrapMF(70000, 80000, 1000000, 1000001, 1)

    #case/workload
    off = TrapMF(0.9999,1, 3, 4, 1)
    lmt = TriMF(3, 4.5, 6, 1)
    lgm = TriMF(5, 6.5, 8, 1)
    hvy = TrapMF(7, 8, 10, 10.0001, 1)

    #storage needs
    light_user = TriMF(1, 2, 3, 1)
    everyday_user = TriMF(2, 3, 4, 1)
    power_user = TriMF(3, 4, 5, 1)


    def budget(self, input):
        result = {"entry": [], "entry_mid": [], "mid_high": [], "high": []}

        result["entry"].append(self.entry.get_output(input))
        result["entry_mid"].append(self.entry_mid.get_output(input))
        result["mid_high"].append(self.mid_high.get_output(input))
        result["high"].append(self.high.get_output(input))

        return result
    
    def workload(self, input):
        result = {"off": [], "lmt": [], "lgm": [], "hvy": []}

        result["off"].append(self.off.get_output(input))
        result["lmt"].append(self.lmt.get_output(input))
        result["lgm"].append(self.lgm.get_output(input))
        result["hvy"].append(self.hvy.get_output(input))

        return result
    
    def storage(self, input):
        result = {"light_user": [], "everyday_user": [], "power_user": []}

        result["light_user"].append(self.light_user.get_output(input))
        result["everyday_user"].append(self.everyday_user.get_output(input))
        result["power_user"].append(self.power_user.get_output(input))

        return result
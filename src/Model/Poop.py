class Poop:
    def __init__(self, num: int, month, day, year, hour, minute):
        self.num = num
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"Mi caca número {self.num} se realizó el día {self.day}/{self.month}/{self.year} a las {self.hour}:{self.minute}"
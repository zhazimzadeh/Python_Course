class Date:
    def __init__(self, Year = 0, Month = 0, Day = 0):
        # Properties
        self.Year = Year
        if(0<Month<13):
            self.Month = Month
        else:
            self.Month=1
        if(0<Day<32):
            self.Day = Day
        else:
            self.Day=1

    

    # Methods
    def Show(self):
        ...

    def Add(self):
        ...

    def Subtract(self):
        ...

    def ConvertDayToDate(self):
        ...

    def ConvertDateToDay(self):
        ...

    def ConvertPersianToMiladi():
        ...

    def ConvertMiladiToPersian():
        ...
    
    def GetToday():
        ...

    def GetWeekDay():
        ...
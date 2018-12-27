
class Counter:
    """Progress indicator for console scripts

    Goal(int) is amount of ticks for function 
    to complete (reach 100%)
    \nkvargs:
    \nbar=int -> length of progress bar; default 40; bar=0 results in no progress bar, max = 100
    \npercentage=int: if =0 percents aren't shown, default 1 """

    _tick = 0
    __barLength = 40
    __showPercent = 1
    __factor = 1

    def __init__(self, goal, **kvargs):
        if int(goal) >= 0:
            if goal < 100:
                self.__factor = 100
                goal *= self.__factor
            self.__nextLevelValue = int(goal)/100.0
            self._percent = 0.0
            self.__level = self.__nextLevelValue
        else:
            return
        if kvargs.get("bar") <= 100 and kvargs.get("bar") >= 0:
            self.__barLength = kvargs.get("bar")
        if kvargs.get("percentage") == 0:
            self.__showPercent = 0

    
    def __outcputCreator(self):
        if self.__barLength == 0:
            bar = ""
        else:
            a = int(self._percent//(100.0/self.__barLength))
            bar = "[" + "."*a + " "*(self.__barLength-a) + "]"
        if self.__showPercent == 1:
            percent = str(int(self._percent))+"%"
        else:
            percent = ""
        print bar, percent, " \r",

    
    def count(self):
        for x in xrange(self.__factor):
            self._tick += 1
            if self._tick >= int(self.__level):
                self._percent += round(self._tick/self.__level)
                self.__level += self.__nextLevelValue
                self.__outcputCreator()
                if int(self._percent) == 100:
                    print "\n"

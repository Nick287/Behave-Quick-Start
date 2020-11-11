class CommonClient:
    def __init__(self, configstring):
        string = 'init' + configstring
        
    def ReturnDoubleNumber(self, x) -> int:
        return x * 2

    def ReturnNumberPlusOne(self,x) -> int:
        return x + 1
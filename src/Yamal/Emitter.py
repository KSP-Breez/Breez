from Extra import errorMes, warningMes, generalMes, Log, successMes

class Yamal_Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.header = ""
        self.code = ""
        
    def emit(self, code):
        self.code += code
        
    def emitLine(self, code):
        self.code += code + "\n"
        
    def headerLine(self, code):
        self.header += code + "\n"
        
    def output(self):
        with open(self.fullPath, "w") as Yamal_Writer:
            Yamal_Writer.write(self.header + self.code)
#Suhu Celcius ke Kelvin

class Celcius:
    @staticmethod
    def Fahrenheit(Cel):
        C = Cel
        CtoF = (9/5) * C + 32
        CtoF = int(CtoF)
        return CtoF
    @staticmethod
    def Kelvin(Cel):
        C = Cel
        CtoK = C + 273
        CtoK = int(CtoK)
        return CtoK
    @staticmethod
    def Reamur(Cel):
        C = Cel
        CtoR = 4/5 * C
        CtoR = int(CtoR)
        return CtoR

CelToF = 45
CelToR = 30
CelToK = 70


fahrenheit = Celcius.Fahrenheit(CelToF)
reamur = Celcius.Reamur(CelToR) 
kelvin = Celcius.Kelvin(CelToK)
print("")
print("Konversi Celcius dengan  Prosedural")
print("")
print("Konversi ",CelToF, "derajat Celcius ke Fahrenhite adalah :",fahrenheit, "derajat")
print("Konversi ",CelToK, "derajat Celcius ke Kelvin adalah     :",kelvin, "derajat")
print("Konversi ",CelToR, "derajat Celcius ke Reamur adalah     :",reamur, "derajat")
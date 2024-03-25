# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 4

class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight /( self.height ** 2 )
    
    def __eq__(self, other):
        if self.weight == other.weight and self.height == other.height:
            return True
        else:
            return False
        
test1 = Bmi(137, 6)
test2 = Bmi(150, 7)
test3 = Bmi(137, 6)

print(test1 == test2)
print(test1 == test3)

print(test1.BMI_Value())
print(test2.BMI_Value())



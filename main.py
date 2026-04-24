# 1-m
class Odam:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salom(self):
        print("Salom", end="")

class Talaba(Odam):
    def salom(self):
        super().salom()
        print(", Men talaba")

o1 = Odam("Sevinch", 15)
o1.salom()

print()
t1 = Talaba("Sevinch", 15)
t1.salom()

# 2-m
class Hayvon:
    def __init__(self,nomi):
        self.nomi = nomi

    def ovoz(self):
        print("Ovoz chiqardi", end=" ")

class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print("Miyov")

h1 = Hayvon("Hayvon")
h1.ovoz()

print()

m1 = Mushuk("Mushuk")
m1.ovoz()

class Car:
    def __init__(self,mark,model,age):
        self.mark=mark
        self.model=model
        self.age=age
        self.adometr=0
    def get_descript_name(self):
        print(f" mark:{self.mark}\n model:{self.model}\n age:{self.age}")
    def read_adometr(self):
        print(f" nachalnoe znachenye adometra: {self.adometr}")
    def update_adometr(self):
        if n>=self.adometr:
            self.adometr=n
        else:
            print("nizya")
    def increment_adometr(self,m):
        self.adometr+=m
        print(f" konechnoe znahchenie={self.adometr}")
class Electrocar(Car):
    def __init__(self,mark,model,age,electro,price):
        super().__init__(mark,model,age)
        self.electro=electro
        self.price=price
        print(f"\tmark= {self.mark}\n\tmodel= {self.model}\n\tage= {self.age}\n\telectro= {self.electro}\n\t price:{self.price}")
    def butureya(self):
        self.electro=h
        print(f"\tiznachalniy zapas electro={self.electro}")
    def coins(self):
        if j>=self.price:
            self.price=j
            print(f"zabirayte za vashu tsenu v :{self.price}")
        else:
            print(f"za takie dengi kupi lanas")
a=Car('Tesla','Y','1996')
n=int(input("n= "))
j=int(input("j= "))
m=int(input("m= "))
h=int(input("h= "))
a.get_descript_name()
#a.adometr=23
a.update_adometr()
a.read_adometr()
a.increment_adometr(m)
b=Electrocar("Lodka",'podlodka','2222','2000',100000)
b.butureya()
b.coins()

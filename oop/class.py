#Class
# class orang :
#     pass
# nama = orang()
# print nama

#Object
# class Orang:
#     def greet(self, nama):
#         print "Hallo",nama
#         return
# org = Orang() #define Object
# org.greet("egin") #call a method from object

#Object with __init__ like constructor
class Orang:
    def __init__(self, nama):
        self.nama = nama
    
    def hasil(self):
        name = self.nama
        print "Selamat Datang", name
org = Orang('Egin')
org.hasil()
Orang('egin').hasil() #Direct Call
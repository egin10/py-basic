# print "Hallo Gaes"

# name = 'Ginanjar'
# i = 20
# print "Nama saya",name,"dan saya berumur",i

# i = 1
# if (i < 10) :
#     print ("nilai yang anda masukan kurang dari 10")
# elif (i > 50):
#     print ("nilai yang anda masukan lebih dari 50")
# else :
#     print ("nilai yang anda masukan lebih dari 10")

# i = 1
# while (i < 10) :
#     print i
#     i += 1

# angka = [1, 2, 3, 4]
# for i in angka :
#     print i

# nama = ["wahid", "egin", "siska"]
# for n in nama :
#     print n

# n = 0
# while (n < 20) :
#     n += 1
#     if((n % 3 == 0) & (n % 5 == 0)):
#         print 'PT SYDECO'
#     elif (n % 5 == 0):
#         print 'SYDECO'
#     elif (n % 3 == 0):
#         print 'PT'
#     else:
#         print n
#     # print n

# kendaraan = ['mobil', 'motor', 'sepeda', 'bus']
# for data in kendaraan :
#     print "Nama kendaraan : %s" %data

# n = len(kendaraan) - 1
# i = 0
# while ( i < n ) :
#     i += 1
#     print "%s" %kendaraan[i]

# function
# def greeting(nama) :
#     print "Hello %s!" %nama

# greeting("Egin")

# input value
# name = raw_input("input nama :")

# def greet(name):
#     print "Hallo %s" %name

# greet(name)

#import modul
# import mod
# from greet import greeting

# Mod = mod
#print greet.greeting("Egin")
# print greeting("Wahid")
# mod.intro("Egin")
# print mod.tambah(3,4)
# print Mod.add(3,2)
# print Mod.panggil('Wahid')

#import module and class
import mod
from mod import obj

# org = mod.obj.Orang()
org = obj.Orang()

org.intro('Egin')
org.pekerjaan('Programmer')

print "Good Bye!"

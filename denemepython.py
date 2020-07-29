
#This code can be used to convert decimal numbers to binary ones


def reverse_list(liste):
 
 liste_2=[]
 for i in range(0,len(liste)):
     liste_2.append(liste[len(liste)-i-1])
     
 return liste_2.copy()


onluk_sayi = int(input('Lutfen bir sayi giriniz.'))
giris = 0

binary_liste = []

ilk_basamak = False

if onluk_sayi != 0 and onluk_sayi%2 == 1:
   ilk_basamak == True


i = 0
giris = onluk_sayi

while giris/2 >= 1:
 giris = giris/2 
 i += 1
 if giris%2 == 1:
    giris = giris-1
      
# Assigning zeros to inside of the binary_list

for j in range(0,i+1):
   binary_liste.append(0) 
if i !=0 or onluk_sayi == 1: 
 binary_liste [i] = 1
if ilk_basamak == True:
 binary_liste.append[0] = 1

onluk_sayi = onluk_sayi - 2**i
i=0

while True:

   if onluk_sayi > 0:
    giris = onluk_sayi

    while giris/2 >= 1:
       giris = giris/2 
       if giris%2 == 1:
           giris = giris-1
       i += 1

    binary_liste [i] = 1
    onluk_sayi = onluk_sayi - 2**i
    i=0
   else:
       break 

reverse_list(binary_liste)
print(*reverse_list(binary_liste))

 
 
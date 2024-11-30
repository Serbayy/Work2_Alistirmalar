### Work 2 ###

### Pytho_Alistirmalar ###

## Görev 1:  Verilen değerlerin veri yapılarını inceleyiniz.

## Type () metodunu kullanınız.

x = 8
type (x)

# int
y = 3,2
type (y)

# float

z = 8j + 18
type (z)
# complex

a = 'Hello World'
type(a)
# str

b = true
type(b)
# bool

C = 23 < 22
type(b)
# boool


L = [1, 2, 3, 4]
type (l)
# list

d = {'Name': 'Jake',
     'Age': 27,
     'Adres': 'Downtown'}
 type (d)
 # dict

t = ( 'Machine Learning', 'Data Science')
type (t)
# tuple

s = ( 'Pyhton', 'Machine Learning' 'Data Science' )
type (s)
# set

 ### Görev 2:  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

 text = 'The goal ıs to turn data into information, and information into insight.'

 new_text = text.upper() .replace(',','') .replace('.'',''').split()
 print (new_text)

 ### Görev 3:  Verilen listeye aşağıdaki adımları uygulayınız.

 lst = ['D,A,T,A,S,C,I,E,N,C,E']

 # Adım1: Verilen listenin eleman sayısına bakınız.

 len (lst)
 print (len)

 # Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

print (lst[0])
print (lst[10])
print (f'Sifirinci indeks: (lst)[0]), Onuncu indeks: (lst)[10]')

# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

new_list = lst [:4 ]
print (f'olusturulan liste: new_list)')

# Adım4: Sekizinci indeksteki elemanı siliniz.

lst.pop (8)
print (lst)

del lst[8]
print (f'new_list: (lst)')

# Adım5: Yeni bir eleman ekleyiniz.
lst = ['D,A,T,A,S,C,I,E,N,C,E']
lst.append('F')

## Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert (8, 'N')
print (lst)

##Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ['America', 18],
        'Daisy': ['England', 12],
        'Antonio': ['Spain', 22],
        'Dante': ['ıtaly', 25]}

## Adım1: Key değerlerine erişiniz.

 dict.keys()
# dict.keys(['Christian', 'Daisy', 'Antonio', 'Dante])

## Adım2: Value'lara erişiniz.

dict.values()

# dict.values([['America',18], ['England', 12], ['Spain', 22], ['ıtaly', 25]])

## Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

# dict ['Daisy'] [12] = 13

## Adım4: Key değeriAhmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
# dict ['Ahmet'] ['Turkey', 24]

## Adım5: Antonio'yu dictionary'den siliniz.

 del dict ['Antonio']

 ## Görev 5:Argümanolarakbir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

 l = [2, 13, 18, 93, 22]
 def func(..):
     ...
     ...
     return..
     even_list, odd_list = func(l)

     l = [2, 13, 18, 93, 22 ]
     def sayılar (l):
         cift_sayılar = []
         tek_sayılar[]
         for sayı in [l]:
             if sayi 0 2 == 0:
                 cift_sayılar.append(sayi)
             else:
                 tek_sayilar.append(sayi)
                 return cift_sayilar, tek_sayılar
             print ('cift sayılar:', ciftler)
             print (Tek sayılar:', tekler')

             ## Görev 6:Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

             # ogrenciler = ['Ali','Veli', 'Ayşe','Talat','Zeynep','Ece']


             for index, ogrenci in enumarate (ogrenciler[:3], 1):
                 print (f'Muhendislik Fakultesi( index), ogrenci:  (ogrenci)')

                for index, in enumarate (ogrenciler[:3],1):
                    print (f'Tıp Fakultesi index'), ogrenci: (ogrenci)')

                    ##  Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ['CMP1005', 'PSY1001', 'SEN2204']

kredi = [3, 4, 2, 4]

kontenjan = [30, 75, 150, 25]

 for kod, kredi , kontenjan in zip (ders_kodu, kredi, kontenjan):
    print (f'kredisi(kredi) olan (kod) kodlu dersin kontenjanı (kontenjan) kisidir.')

    ## Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1= set (['Data', 'Pyhton'])
kume2 = set (['data', 'function', 'gcut', 'lambbda', 'python', 'miuul'])

kume1.issuperset (kume2)
#kapsamiyor

kume1.intersection (kume2)
kume2.difference (kume1)
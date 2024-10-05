#mutable
#list
makanan = ['mie', 'bakso', 'es teh', 'sate', 'batagor']
print(makanan)
print(id(makanan))

#elemen ditambahkan, list tidak akan berubah

makanan.append('pangsit')
print(makanan)
print(id(makanan))

#pada saat liat diubah elemenny, id list tidak akan berubah karena ini merupakan
#pembaruan nilai bukan pembuatan objek baru

#immutable
motor = ['yamaha', 'honda', 'ninja', 'ducati']
print(motor)
print(id(motor))

#ketika nilai di tambahkan elemen baru, id akan berubah

motor = motor + ['supra']

#ketika nilai di ibuah, id akan berubah karena membuat objek baru bukan pembaruan nilai

#List
#1. mutable
list = [1, 2, 3, 4, 5]
print(list)
print(id(list))
list.append(6)
print(list)
print(id(list))

#2. immutable
list2 = [1, 2, 3, 4, 5]
print(list2)
print(id(list2))
list2 = list2 + [6]
print(list2)
print(id(list))

#Tuple
#1. mutable
tuple = ("NIKE","BALENCIAGA", "ADIDAS", "PUMA","VANS", "ANTA"  )
print(tuple)
x = list(tuple)
x.append("COMPAS")
tuple = tuple(x)
print(tuple)
print(id(tuple))

#2. immutable
tuple2 = ("NIKE", "ADIDAS", "PUMA", "ANTA", "BALENCIAGA", "VANS")
print(tuple2)
print(id(tuple2))
tuple2 = tuple2 + ("COMPAS")
print(tuple2)
print(id(tuple2))

#Set
#1.mutable
set = ('baju', 'clana', 'tas', 'topi')
print(set)
set.add('spatu')
print(set)
print(id(set))

#2. immutable
set2 = {'sulis', 'supriatno', 'sutrisno', 'situ'}
print(set2)
print(id(set2))
set2 = set2.union({'sulis'})
print(set2)
print(id(set2))
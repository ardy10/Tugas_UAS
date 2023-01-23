#Recursive
def tampilkanAngka (batas, i = 1):
  print(f'Perulangan ke {i}')

  if (i < batas):
    tampilkanAngka(batas, i + 1)

tampilkanAngka(10)


#Function
def my_function(fname):
  print(fname + " tugas_uas")

my_function("Ardy Andhika Haydar")
my_function("20210801084")
my_function("Teknik Informatika")

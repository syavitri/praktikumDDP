from gempa import *
#buat object
g1 = gempa("banten",1.2)
g2 = gempa("palu",6.1)
g3 = gempa("cianjur",5.6)
g4 = gempa("jayapura",3.3)
g5 = gempa("garut",4.0)

#panggil fungsi di class gempa
g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()
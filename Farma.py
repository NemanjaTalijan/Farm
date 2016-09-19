import sys
import os



class Farm_animal:
    __id = 0
    __weight = 0
    __data_of_birth = 0

    def __init__(self, id, weight, date_of_birth):
        self.__id = id
        self.__weight = weight
        self.__date_of_birth = date_of_birth
        
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self.i__d


    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.__date_of_birth

    def toString(self):
        return "ID krave je {} , tezina joj je {} kg, rodjena {}".format(self.__id,
                                                                       self.__weight,
                                                                       self.__date_of_birth)
        
farma_zivotinja = []
count = 0

#krava
krava = Farm_animal(0,300,07210015)
farma_zivotinja.append(krava)
count = count + 1
for x in farma_zivotinja:
    print x.toString()    
print "Trenutno na farmi ima {} krava/e".format(count)
    

#krava1
krava1 = Farm_animal(1,400,11222016)
farma_zivotinja.append(krava1)
count = count + 1
for x in farma_zivotinja:
    print x.toString()    
print "Trenutno na farmi ima {} krava/e".format(count)

    
#krava2
krava2 = Farm_animal(2,350,12225015)
farma_zivotinja.append(krava2)
count = count + 1
for x in farma_zivotinja:
    print x.toString()    
print "Trenutno na farmi ima {} krava/e".format(count)

#krava3
krava3 = Farm_animal(3,100,236598)
count = count + 1
farma_zivotinja.append(krava3)
for x in farma_zivotinja:
    print x.toString()
print "Trenutno na farmi ima {} krava/e".format(count)
    



#farma_zivotinja[0].toString()





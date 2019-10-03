import random
class Aircraft:
    x=0
    y=0
    acceleration=1
    def __init__(self, obj_no, new_x=0, new_y=0):
        print "Aircraft # ",obj_no, " has been istantiated"
        self.flight_number = obj_no
        self.x=new_x
        self.y=new_y

class Boeing_747(Aircraft):
    destination_x=0
    destination_y=0
    def __init__(self, obj_no=0):
        Aircraft.__init__(self,obj_no, new_x=0, new_y=0)
        self.x=random.randint(1,101)
        self.y=random.randint(1,101)
        self.destination_x=random.randint(1,101)
        self.destination_y=random.randint(1,101)


anurag_airlines= []
for i in range(0,5):
    anurag_airlines.append(Boeing_747(i+1))
    print "Initial X-Coord:",anurag_airlines[i].x
    print "Initial X-Coord:",anurag_airlines[i].y
        

    print "Final X-Coord:",anurag_airlines[i].destination_x
    print "Final X-Coord:",anurag_airlines[i].destination_y

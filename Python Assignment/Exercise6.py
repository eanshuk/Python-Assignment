import random
class Aircraft:
    x=0
    y=0
    acceleration=1
    def __init__(self, obj_no, new_x=0, new_y=0):
        print "Aircraft # ",obj_no
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
    def flight_path(self, x_path):
        m=float(self.destination_x - self.x) / float(self.destination_y - self.y)
        b= self.y - (m * self.x)
        return float((m*x_path)+ b)
    def Aircraft_acceleration(self):
        return self.acceleration


anurag_airlines= []
for i in range(0,5):
    anurag_airlines.append(Boeing_747(i+1))
    end=anurag_airlines[i].destination_x
    start = anurag_airlines[i].x
    if(anurag_airlines[i].x > anurag_airlines[i].destination_x):
        start=anurag_airlines[i].destination_x
        end =anurag_airlines[i].x
        print "Sarting from: (",start,",",anurag_airlines[i].flight_path(start) ,")"
        print "Headed to: (",end,",", anurag_airlines[i].y,")"
    else:
        print "Sarting from: (",start,",",anurag_airlines[i].y ,")"
        print "Headed to: (",end,",",anurag_airlines[i].flight_path(end) ,")"
    for j in range(start, end+1):
        print j,", ",anurag_airlines[i].flight_path(j)

    print "We have arrived!"
    print "Acceleration constant:",anurag_airlines[i].Aircraft_acceleration()

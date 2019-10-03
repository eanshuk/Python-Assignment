aircrafts=[{'x':1,'y':7},{'x':3,'y':5},{'x':4,'y':8},{'x':9,'y':10},{'x':6,'y':12}]
aircraft_number=1
for aircraft in aircrafts:
    print "Air-craft Number: ",aircraft_number
    print(aircraft['x'])
    print(aircraft['y']) 
    print '\n'
    aircraft_number+=1
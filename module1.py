import alto
import time
import sys

if len(sys.argv) != 4:
    print('[URL][USER_NAME][PASSWORD]')
    exit(1)

# go to url
myUrl = sys.argv[1]
myUser = sys.argv[2]
myPass = sys.argv[3]

# go to venues
myModule = alto.venues(myUrl, myUser, myPass)
myModule.goToVenues()

#with open('citiList.txt') as f:
#    citiList = f.readlines()
#for city in citiList:
#    myModule.addVenue(city, city)

myModule.addVenue('New York', 'New York')
myModule.addVenue('Tokyo', 'Tykyo')
myModule.addVenue('London', 'London')
myModule.addVenue('São Paulo', 'São Paulo')
myModule.addVenue('Sydney', 'Sydney')

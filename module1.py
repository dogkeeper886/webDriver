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
myModule.addVenue('Roma', 'Roma')
myModule.addVenue('Milano', 'Milano')
myModule.addVenue('Tokyp', 'Tykyo')
myModule.addVenue('Osaka', 'Osaka')

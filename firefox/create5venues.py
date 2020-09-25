from venue import venues
from sys import argv

if len(argv) != 4:
    print('[URL][USER_NAME][PASSWORD]')
    exit(1)

# go to url
myUrl = argv[1]
myUser = argv[2]
myPass = argv[3]

# go to venues
myModule = venues(myUrl)
myModule.login(myUser, myPass)
myModule.basic5()

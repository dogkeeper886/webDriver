from deepTools import deepTools
from sys import argv

if len(argv) != 3:
    print('[DEEPTOOLS_URL][APSERIAL]')
    exit(1)

# go to url
myUrl = argv[1]
myApSerial = argv[2]

# go to venues
myTool = deepTools(myUrl)
myTool.searchAP(myApSerial)
# status check
#myTool.status()
#myTool.checkResult()
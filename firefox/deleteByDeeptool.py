from deepTools import deepTools
from sys import argv

if len(argv) != 3:
    print('[DEEPTOOLS_URL][IDMID]')
    exit(1)

# go to url
myUrl = argv[1]
myIdmId = argv[2]

# go to venues
myTool = deepTools(myUrl)
myTool.deleteByIdmId(myIdmId)
myTool.status()
myTool.checkResult()

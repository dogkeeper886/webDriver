from deepTools import deepTools
from sys import argv

if len(argv) != 3:
    print('[DEEPTOOLS_URL][TENANTID]')
    exit(1)

# go to url
myUrl = argv[1]
myTenantId = argv[2]

# go to venues
myTool = deepTools(myUrl)
myTool.searchTenant(myTenantId)
# status check
myTool.status()
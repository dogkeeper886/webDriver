from slackMonitor import slackMonitor
from sys import argv
import logging
from time import sleep

if len(argv) < 3:
    logging.error('ARGUMENT COUNT LESS THAN REQUIREMENT')
    exit(1)

USERNAME = argv[1]
USERPASSWORD = argv[2]

mySlack = slackMonitor('https://arris.slack.com/')
mySlack.login(USERNAME, USERPASSWORD)
mySlack.channel('CC04J4E3V')
sleep(20)

msg = '/alto-tenant lookup 0012h00000NrlBUAAZ dev'
mySlack.sendMessage(msg)
sleep(1)
# mySlack.checkCommand(msg)
# mySlack.checkQueued(msg)
mySlack.readResponse()
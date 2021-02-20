#helper functions

commands=['!google','!recent']

def predicate(message):
    return not message.author.bot and "!google" in message.content

def formatMessage(message):
    for command in commands:
        message = message.replace(command+' ','')
    return message

def printList(data):
    return ','.join(map(str,data))

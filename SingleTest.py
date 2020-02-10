#Singel Test file

from androguard.misc import AnalyzeAPK
import zipfile

print ("HI")

file = "D:\\Codes\\malware\\android-malware-master\\BreakBottleneck\\SamplesOfHIP2014TalkBreakBottleneck\\ChinaTop\\Omigo.apk"
# D:\\Codes\\malware\\android-malware-master\\BreakBottleneck\\SamplesOfHIP2014TalkBreakBottleneck\\ChinaTop\\Omigo.apk

apk, d, dx = AnalyzeAPK(file)

# def printIntentFilters(itemtype, name):
#     print ('\t' + "HERE !!!!!!" + name + ':')
#     for action,intent_name in apk.get_intent_filters(itemtype, name).items():
#                 print ('\t\t' + action + ':' + "ACTION")
#                 for intent in intent_name:
#                         print ('\t\t\t' + intent + "O intent")  
#     return



# MY helper to extrac intents
def helper(obj,itemtype):
    alista =[]
    for name in obj:
            for action,intent_name in apk.get_intent_filters(itemtype, name).items():
                        for intent in intent_name:
                                alista.append(intent)
    return alista



# Intent filters 

print(apk.get_providers())


print('=======================')

services = apk.get_services()
print (services)
print("MY =============INTENTS===")
print(helper(services,'service'))


receivers = apk.get_receivers()
r = []
for i in receivers:
    r.append(i) 
print(r)
print("MY =============INTENTS===")
print(helper(receivers,'receiver'))


# try:
#     print (a.get_permissions())
#     print("======services=================================================")
#     print (a.get_services())
#     print("Providers========= =========================================")




 
###GET API CALLS

# print("======providers========")
# x = (list(dx.get_classes()))
# for i in x:
#     i = str(i)
#     print(i)


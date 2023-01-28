import sys
import time

sys.path.append('..')
import cyberfloodDyrulEdit

cfcontroller = "172.18.0.35"
username = "admin@spirent.com"
password = "Spirent@123"




print("Checking for connectivity & credentials...", end=" ")
cfClient = cyberfloodDyrulEdit.CfClient(username=username, password=password, cfcontroller=cfcontroller)
cfClient.generateToken()
if cfClient.isLogged():
    print("success! [" + cfClient.userName + "]")


else:
    print("error! Please check your configuration.")
    

#Find the specified Test case and execute:

print("-------------------------------------------------------------------------------")

cfClient.getTestRun()

#cfClient.converttocsv()



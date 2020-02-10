import os
import csv

# Find Malwares in the Document

mydir = "D:\\Androzoo"
#'D:\\Androzoo'
#"D:\\Malware\\APK - unb malware\\Benign_2015_600"

#mydir = "D:\\Codes\\malware\\android-malware-master"           MALWARE
x = os.walk(mydir)

# Start MAKE CSV with malware.apk dirs
print("START")
with open('Malware_dir_Androzoo.csv','w', newline='') as csv_file:
    fieldname = ['MD','NUMBER']
    writer = csv.DictWriter(csv_file, fieldnames = fieldname)

    malware_Count = 0
    for root_dir, sub_dir, files in x:
        print ("ROOT DIR")
        print (root_dir)
        #print ("SUB DIR")
        #print (sub_dir)
        #print ("FILES")
        #print (files)
        print ("MALWARES")
        for item in files:
            if ".apk" in item:
                malware_Count = malware_Count + 1
                name = root_dir + "\\" + item
                name = name.replace('\\','\\\\')
                print (name)
                writer.writerow({'MD' : name , 'NUMBER' : malware_Count})
        print ("=======================================")








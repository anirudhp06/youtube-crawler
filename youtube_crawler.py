import requests
import json
import os
from sys import exit
from time import sleep
id=input("pls give the youtube id:")
has=0
if "," in id:
    id=id.split(',')
    has=1
if has==1:
    for i in range(0,len(id)):
        flag='flags=0'
        api="https://filmot.com/api/getvideos?key=md5paNgdbaeudounjp39&id={}&{}".format(id[i],flag)
        response=requests.get(api).text
        selc=['yes','y']
        if response == "[]":
            print("'{}' Hasnt been crawled yet".format(id[i]))
            if i==len(id)-1:
                print("All id's searched none were crawled")
                print("Exiting in 3 sec")
                sleep(5)
                exit()
            else:
                print("Proceeding to next id")
                continue
        desc=input("Do you want description too?(y/n)(yes/no):").lower()
        if desc in selc:
            flag="flags=1"
            api="https://filmot.com/api/getvideos?key=md5paNgdbaeudounjp39&id={}&{}".format(id[i],flag)
            response=requests.get(api).text
        dict_data=json.loads(response[1:len(response)-1])
        for k,v in dict_data.items():
            print("{}: {}".format(k,v))
        print()
        choice=input("Do you want to Write this into file?(yes/n):").lower()
        print()
        if choice in selc:
            print("Writing into file...")
            with open("Youtube_data.txt","a") as writer:
                try:
                    for k,v in dict_data.items():
                        writer.write("{} : {}\n".format(k,v))
                except UnicodeEncodeError:
                    print("Description has data which cannot be encoded...Didnt write description into file.")
                writer.write("\n\n\n\n")
else:
    selc=['yes','y']
    flag='flags=0'
    api="https://filmot.com/api/getvideos?key=md5paNgdbaeudounjp39&id={}&{}".format(id,flag)
    response=requests.get(api).text
    if response == "[]":
        print("Hasnt been crawled yet\nExiting in 5 seconds")
        sleep(3)
        exit()
    desc=input("Do you want description too?(y/n)(yes/no):").lower()
    if desc in selc:
        flag="flags=1"
        api="https://filmot.com/api/getvideos?key=md5paNgdbaeudounjp39&id={}&{}".format(id,flag)
        response=requests.get(api).text
    dict_data=json.loads(response[1:len(response)-1])
    for k,v in dict_data.items():
        print("{}: {}".format(k,v))
    print()
    choice=input("Do you want to Write this into file?(y/n):").lower()
    if choice in selc:
        print("Writing into file...")
        with open("Youtube_data.txt","a") as writer:
            try:
                for k,v in dict_data.items():
                    writer.write("{} : {}\n".format(k,v))
            except UnicodeEncodeError:
                print("Description has data which cannot be encoded...Didnt write description into file.")
            writer.write("\n\n\n\n")
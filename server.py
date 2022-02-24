import Pyro4 
import random 
import os 
import datetime 
import subprocess 
now=datetime.datetime.now() 
print('date: '+now.strftime('%d-%m-%y')+' Time:'+now.strftime('%H:%M:%S')) 
@Pyro4.expose 
class Server(object): 
    def add(self, a, b): 
        return "{0} + {1} = {2}".format(a, b, a+b) 
   
    def sortarr(self, arr):
        arr.sort()
        return arr

    def upload_file(self, s, file_list):
        if os.path.exists(s):
            os.remove(s)
        textfile = open(s, "x")
        for i in file_list:
            textfile.write(i)
        textfile.close
        return 1

    def download_file(self, s):
        if os.path.exists(s):
            file_read = open(s, "r")
            file_list = file_read.readlines()
            #print(file_list)
            return file_list
            
        else:
            return 0
        
    def delete_file(self, s):
        if os.path.exists(s):
            os.remove(s)
            return 1
        else:
            return 0
    def rename_file(self, s, s1):
        if os.path.exists(s):
            os.rename(s,s1)
            return 1
        else:
            return 0

    

        



daemon = Pyro4.Daemon()                 
ns = Pyro4.locateNS()                   
url = daemon.register(Server)    
ns.register("RMI.methods", url)    
print("The Server is now active., please request your calculations or start file transfer") 
daemon.requestLoop()                    

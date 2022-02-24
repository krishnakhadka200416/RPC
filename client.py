import Pyro4 
import os 
import datetime 
Client = Pyro4.Proxy("PYRONAME:RMI.methods")    
print('Welcome to the RMI system.')
now=datetime.datetime.now() 
print('date: '+now.strftime('%d-%m-%y')+' Time:'+now.strftime('%H:%M:%S')) 
r = 1
while (r==1): 
   
  print("Enter number to perform the task: \n" +'1.ADD \n'+ '2.SORT  \n'+  '3.Upload File \n' + '4.Download File\n'+'5.Delete File \n'+ '6.Rename File \n' + '7.EXIT \n') 
  c=int(input('Enter your choice: ')) 
  
  if (c==1):  
    a =int(input("Enter a: ")) 
    b =int(input("Enter b: "))
    print(Client.add(a,b)) 
 
  elif (c==2):
    arr = []
    n = int(input("Enter number of numbers : "))
    for i in range(0,n):
      num = int(input())
      arr.append(num)
    print("The unsorted array is {0}".format(arr))
    print("The sorted array is {0}".format(Client.sortarr(arr)))

  elif (c == 3):
    s = input('Enter the filename to upload: ')
    
    if os.path.exists(s):
      file_read = open(s, "r")
      file_list = file_read.readlines()
      #print(file_list)
      Client.upload_file(s,file_list)
      print('File uploaded')
      
    else:
      print('File not found\n')

  elif (c == 4):
    s = input('Enter the filename to download: ')
    file_list = Client.download_file(s)
    if (file_list==0):
      print ('No file found in the server side')
    else:
      #print(file_list)
      #if os.path.exists(s):
      #  os.remove()   
      textfile = open(s, "w")
      for i in file_list:
        textfile.write(i)
      textfile.close
      textfile = open(s, "w")
      for i in file_list:
        textfile.write(i)
      textfile.close
      print('File downloaded\n')
       
      
  elif (c == 5):
    s = input('Enter the filename to delete: ')
    if (Client.delete_file(s)==1):
      print('File deleted\n')
    else:
      print('File not found\n')

  elif (c == 6):
    s = input('Enter the filename to rename: ')
    s1  = input ('Enter the new name for the file: ')
    if (Client.rename_file(s,s1)==1):
      print('File renamed\n')
    else:
      print('File not found\n')

  elif (c==7):
    r = 0
    print('Thank you\n')
  else: 
    print('invalid input\n') 
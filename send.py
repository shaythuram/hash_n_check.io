from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from datetime import datetime
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="98518959",
  database="hash_track",
  use_pure=True
)
print(mydb)
mycursor=mydb.cursor()

# mycursor.execute("ALTER TABLE hash_records ADD timestamp VARCHAR(100) NOT NULL")#adding new tcolumn to table


# # mycursor.execute("CREATE DATABASE hash_track")#create
#
# # mycursor.execute("CREATE TABLE hash_records (id INT AUTO_INCREMENT PRIMARY KEY, FILE_NAME VARCHAR(255) NOT NULL, FILE_HASH VARCHAR(255)NOT NULL UNIQUE)")

set_dir = input("current directory is:" + str(os.getcwd())+ ": ,if you would like to ammend, \nenter \"1\" else enter \"0\": ")

if set_dir == "1":
    new_dir = str(input("Enter new dir here: "))
    os.chdir(new_dir)
    print("current directory is:" , os.getcwd())
    a = input("if you are satisfied,\nenter \"0\" else enter \"1\": ")

    for i in range(int("1")):

        if a == "0":
            break
        elif a == "1":
            new_dir = str(input("Enter your preferd directory here: "))
            os.chdir(new_dir)
            print("Current Directory is:" , os.getcwd())
            break
        else:
            print("I'm sorry please key in a valid directory, \nscript will exit ")
            exit()



hm = int(input("how many: "))
data_list=[]
hash_list = []
for i in range (hm):
    file = input("Input file name: ")
    fdata = open(file,"rb")
    for x in fdata:
        data_list.append(x)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(bytes(str(data_list),'utf-8'))
    fh=str(digest.finalize())
    now = datetime.now()
    # dd/mm/YY H:M:S
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    hash_list.append((file,fh,current_time))
print(hash_list)
insert = ("INSERT INTO hash_records (FILE_NAME,FILE_HASH,TIMESTAMP) VALUES (%s,%s,%s)")
mycursor.executemany(insert,hash_list)
mydb.commit()
# fhandle = input("input file name: ")
# fdata = open(file , "rb")


# # datetime object containing current date and time
# now = datetime.now()
#
# print("now =", now)
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="98518959",
  database="hash_track",
  use_pure=True
)
print(mydb)
mycursor= mydb.cursor()


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
            print("I'm sorry please key in a valid directory, \nscript will now exit ")
            exit()


sql = "SELECT FILE_HASH FROM hash_records WHERE file_name = %s"
file_to_retreive = input("What file do you want to retreive?: ")
request = (file_to_retreive, )

mycursor.execute(sql, request)
myresult = mycursor.fetchall()

what_to_check = input("What file would you like to check?: ")

hash_list = []
data_list = []
fdat = open(what_to_check,"rb")


for x in fdat:
    data_list.append(x)
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(bytes(str(data_list),'utf-8'))
fh=str(digest.finalize())
hash_list.append((fh,)) #need to do it this way because when calling back file hash from databse, it comes tih an extra ',' and a pair of ''

print(hash_list)



for x in myresult:
    if x == hash_list[0]:
        print("File integrity not compromised")
        print(x, " == \n", hash_list[0] )
    else:
        print("Files are not the same")

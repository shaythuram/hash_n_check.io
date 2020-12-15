# hash_n_check.io
This programm: 

1)Receives a file and hashes it using SHA256 algorithm, this is done in send.py. 
2)It sends this hash to your mysql server. 
3) You can request back for this hash, based on the name of the file. 
4) You can use the call.py to check if another file is exactly the same as a file that had been uploaded prior and see if there is any difference between the 2 said files.  

UPDATED 17/10/2019 :
1)Using OS module I have enabled for users to switch directories and upload files from any part of their computer. 
2) Added timestamp feature

fs = open(rw, 'C:\Users\chris\Desktop\Dev\rpc\sbcs\reedy.txt')  
# It will read the 4 characters from the text file  
con = fs.read(4)  
# It will read the 10 characters from the text file  
con1 = fs.read(10)  
# It will read the entire file  
con2 = fs.read()  
print(con)  
fs.close()  # It will read the entire file  

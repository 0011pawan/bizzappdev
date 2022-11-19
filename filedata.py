#open url file and read data of file
file=input('Please enter your file url')

f=open(file,"r+")
data=f.readlines()
for i in data:
    print(i)

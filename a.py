import os
def create(filename):
  with open(filename,'w') as file:
    print(f"{filename} created!!!")
def write(filename,content):
  with open(filename,'w') as file:
    file.write(content)
def read(filename):
  with open(filename,'r') as file:
    content=file.read()
    print(f"{content} read successfully!!!")
def append(filename,content):
  with open(filename,'a') as file:
    file.write(content)
    print("Content appended successfully!!!")
def delete(filename):
  if os.path.exists(filename):
    os.remove(filename)
  print("File deleted successfully!!!")


filename='Soham.txt'
create(filename)
write(filename,"Hi,I am Soham Hajare")
read(filename)
append(filename,"\nAnd I am 19 yrs old!!")
delete(filename)




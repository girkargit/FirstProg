f = open("abhi.txt" , "r")
print(f.readline() , end = '') # end for remove next line print
print(f.tell()) # give us where is pointer in file
print(f.readline() , end = '')
print(f.tell())
f.seek(3) # reste pointer to value is given
print(f.readline())
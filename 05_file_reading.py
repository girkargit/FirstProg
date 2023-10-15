f = open("abhi.txt" , "r") # file name , mode
content = f.read().splitlines() # we can pass number on the basis of print number of character
# print(f.readline())
# content = f.readlines()# return value in list
# content = f.read()
# for line in content: # reade character by character
#     print(line)
# for line in f: # read line by line
#     print(line , end = "")
print(content)
f.close()





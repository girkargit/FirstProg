lst = ["abhi","amol","omii","suraj","bhor"]
# # print odd number element is list
# i = 1
# for item in lst:
#     if i % 2 is not 0:
#         print(item)
#     i = i + 1

for index , item in enumerate(lst): # function
    if index % 2 == 0:
        print(item)
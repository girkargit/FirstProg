import time
# initial = time.time()
# k = 0
# while k < 100:
#     print("hi")
#     k = k + 1
# print(time.time() - initial)
#
# initial2 = time.time()
# for i in range(100):
#     print("hii")
# print(time.time() - initial2)

local_time = time.asctime(time.localtime(time.time())) # Return local time
print(local_time)

for i in range(2):
    print("hii")
    time.sleep(2)
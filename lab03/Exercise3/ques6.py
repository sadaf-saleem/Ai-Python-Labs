# random module
import random

print(random.random())

print(random.randint(1,50)) # 1 se 50 k drmyan numbers print krta he (imp: 1 or 50 bhi aasakty hen isme)

l1 = ['Pakistan', 'India', 'China'] # list k items ko shuffle krega


random.shuffle(l1)

print(l1)
print(l1[1])

l2 = [1, 2, 3, 4, 5, 6,7,8,9,10]

new_l2 = random.sample(l2, 5) # nai list return krega random elements k sath unka count n hoga jo hame dengy
print(new_l2)
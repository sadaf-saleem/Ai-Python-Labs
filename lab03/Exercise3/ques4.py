import time
# Time = time.time()
Time= 1739532924.895901
print(Time)

actual_time= time.ctime(Time) # ye function kisi bhi time ko seconds me input leke usko proper understandable form me convert krta he or agar isme koi argument na daalo to by default curr time understandable form me return krta he , kya samjhy!
print(actual_time)
actual_time= time.ctime()
print(actual_time)

p=time.sleep(5) # yahan function 5 secs k lye stay uske bad prnt statment print hogi !
print('5 seconds completed!')
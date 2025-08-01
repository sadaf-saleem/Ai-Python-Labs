import glob
a=glob.glob('*.py')  # current folder ki sirf .py extension wali files ko hi list me daalega
print(a)

from glob import glob

print( 'astesisk only', glob('*')) # current folder ki saari files ko list me daaldega
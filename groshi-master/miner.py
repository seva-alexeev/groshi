from random import *
from time import time
import hashlib

letters = 'qwertyuiopasdfghjklzxcvbnm'
start = time()
while True:
    test_string = "".join([choice(letters) for i in range(10)])
    if hashlib.md5(test_string.encode('utf8')).hexdigest()[:4] == '0000':
        print(test_string)



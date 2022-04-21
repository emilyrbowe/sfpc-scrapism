import requests, re, string, random
# import random

vow_start = "I promise to "

for i in range(0,10):
    random_int = random.randint(10,15)
    print(vow_start + str(random_int) + ' \r')
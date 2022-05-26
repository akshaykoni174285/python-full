# just using any module to perform a simple task 

import os

from django.urls import path

path = "/home/whoami/Documents"

list_dir = os.listdir(path)

for i in list_dir:
    print(i)
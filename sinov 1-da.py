# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 12:07:59 2025

@author: Azizxon
"""

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh<=16:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")
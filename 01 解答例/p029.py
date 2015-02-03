# -*- coding: utf-8 -*-
"""
Project Euler Problem 29
2 ≤ a ≤ 5 と 2 ≤ b ≤ 5について, a**b を全て考えてみよう:

2**2=4, 2**3=8, 2**4=16, 2**5=32
3**2=9, 3**3=27, 3**4=81, 3**5=243
4**2=16, 4**3=64, 4**4=256, 4**5=1024
5**2=25, 5**3=125, 5**4=625, 5**5=3125
これらを小さい順に並べ, 同じ数を除いたとすると, 15個の項を得る:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

2 ≤ a ≤ 100, 2 ≤ b ≤ 100 で同じことをしたときいくつの異なる項が存在するか?

"""
l=[]
#a1=2;a2=5;b1=2;b2=5
a1=2;a2=100;b1=2;b2=100
for a in range(a1,a2+1):
    for b in range(b1,b2+1):
        ab=a**b
        if not ab in l:
            l.append(ab)
print len(l)

            
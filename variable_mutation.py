
# # make the "a" variable's value bigger by 10
a = 3
a += 10
print(a)
#

# # make b smaller by 7
b = 100
b -= 7
print(b)
#

# # please double c's value
c = 44
c *= 2
print(c)
#

# # please divide by 5 d's value
d = 125
d = d / 5
print(d)
#

# # please cube of e's value
e = 8
e = e **3
print(e)
#
# # tell if f1 is bigger than f2 (pras a boolean)
f1 = 123
f2 = 345
if f1 > f2:
    print(True)
else:
    print(False)
#
# # tell if the double of g2 is bigger than g1 (pras a boolean)
g1 = 350
g2 = 200
if g2 * 2 > g1:
    print(True)
else:
    print(False)
#
# # tell if 11 is a divisor of h (pras a boolean)
h = 1357988018575474
if h % 11 == 0:
    print(True)
else:
    print(False)
#
# # tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
i1 = 10
i2 = 3
if i1 > i2**2 and i1< i2**3:
    print(True)
else:
    print(False)
#
# # tell if j is divisible by 3 or 5 (pras a boolean)
j = 1521
if j % 3 or 5 == 0:
    print(True)
else:
    print(False)
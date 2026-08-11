from math import sqrt

R = 2
S = 5
T = -1
X = 3
Y = 1
Z = 0

if (R >= 5) or (T > Z) and (X - Y + R > 3 * Z) == True:
    print(f"A = True")
else:
    print(f"A = False")
    
if T + 3 >= 4 and not(3 * R / 2 < S * 3) == True:
    print(f"B = True")
else:
    print(f"B = False")
    
if (X == 2) or ((Y == 1) and ((Z == 0)) or ((R > 3)) and S < 10) == True:
    print(f"C = True")
else:
    print(f"C = False")

if (R != S) or (not(sqrt(R) < sqrt(X)) and (4327 * X * S * Z == 0)) == True:
    print(f"D = True")
else:
    print(f"D = False")
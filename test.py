# supporting logic function(s)
def xor(x, y):
    return (x or y) and not (x and y)


# Your Boolean function goes here:
def F(A, B, C, D):
    P = xor(A, B)
    Q = xor(C, D)
    R = xor(P, Q)
    return R


# Translates between 'T'/'F' and True/False:
def f(a, b, c, d):
    t = 'T'
    (A, B, C, D) = (a == t, b == t, c == t, d == t)
    R = F(A, B, C, D)
    return "FT"[R]


print("Truth Table")
print()
print("A B C D |   Output")
print("========|===========")
r = "TF"
for a in r:
    for b in r:
        for c in r:
            for d in r:
                print(a, b, c, d, "|    ", f(a, b, c, d))
w = 0.8
lam = 0.1
for i in range(5):
    w = w - lam*(-2+8*w)
    print(w)
a, b, c = 2, 1, 1
x1, x2 = -2, 2
dx = 0.5

print("x\tF(x)")
x = x1
while x <= x2:
    if abs(x) < 1:
        F = x - a * b
    else:
        F = x**2 / (a + c)
    
    print(f"{x:.1f}\t{F:.4f}")
    x += dx
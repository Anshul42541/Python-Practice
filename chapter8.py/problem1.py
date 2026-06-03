def Greatest_Of_Three_Numbers(a,b,c):
    if a > b and a > c:
        return f"{a} is the greatest number"
    elif b > a and b > c:
        return f"{b} is the greatest number"
    else:
        return f"{c} is the greatest number"

print(Greatest_Of_Three_Numbers(10, 20, 30))
print(Greatest_Of_Three_Numbers(160, 220, 130))
print(Greatest_Of_Three_Numbers(108, 520, 630))

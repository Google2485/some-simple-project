import math

def quadratic():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    d = (b*b) - (4*a*c)
    
    if d < 0:
        print("Roots are imaginary")
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        print("Roots are Real")

# Call the function once
quadratic()

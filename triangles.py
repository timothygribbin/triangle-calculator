import math
from sys import exit

def main():
    ans = prompt()
    if ans == "A":
        sas_triangle_computation()
    elif ans == "B":
         asa_triangle_computation()
    elif ans =="C":
         sss_triangle_computation()
    else:
         print("Answer not found, please run the program again and enter 'A', 'B', or 'C'.")

def prompt():
    x = ""
    while (len(x) < 1):
        x = input("What information will you be providing me with today? \n A) 2 sides and the angle between those 2 sides \n B) 2 angles and one side in between those angles \n C) 3 sides and no angles \n Enter your letter choice below: \n").capitalize().strip()
    return x

def sas_triangle_computation():
    side_a = side_prompt_and_validation_a()
    side_b = side_prompt_and_validation_b()
    angle_C = angle_prompt_and_validation_c()
    side_c = law_of_cos_side(side_a,side_b,angle_C)
    smallest_side = min([side_a, side_b])
    if smallest_side == side_b:
        angle_B = law_of_sin_angle(side_b, angle_C, side_c)
        angle_A = third_angle(angle_C, angle_B)
    if smallest_side == side_a: 
        angle_A = law_of_sin_angle(side_a, angle_C, side_c)
        angle_B = third_angle(angle_C, angle_A)
    area = calculate_area(side_a,side_b,side_c)
    print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area) 

def asa_triangle_computation(): 
    angle_A = angle_prompt_and_validation_a()
    angle_B = angle_prompt_and_validation_b()
    side_c = side_prompt_and_validation_c()
    angle_C = third_angle(angle_A, angle_B)
    side_a = law_of_sin_side(side_c, angle_A,angle_C)
    side_b = law_of_sin_side(side_c,angle_B,angle_C)
    area = calculate_area(side_a,side_b,side_c)
    print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area)  

def sss_triangle_computation():
    side_a = side_prompt_and_validation_a()
    side_b = side_prompt_and_validation_b()
    side_c = side_prompt_and_validation_c()
    validate_triangle(side_a,side_b,side_c)
    angle_C = law_of_cos_angle(side_a, side_b,side_c)
    angle_A = law_of_cos_angle(side_b,side_c,side_a)
    angle_B = third_angle(angle_A, angle_C)
    area = calculate_area(side_a,side_b,side_c)
    print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area) 

def print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area):
    print("\nResults:\n")
    print("Side a: " + str(side_a))
    print("Side b: " + str(side_b))
    print("Side c: " + str(side_c))
    print("Angle A: " + str(angle_A))
    print("Angle B: " + str(angle_B))
    print("Angle C: " + str(angle_C))
    print("Area: " + (str((area))))

def calculate_area(side_a,side_b,side_c):
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
    return area

def law_of_sin_angle(x,y,z):
     return math.degrees(math.asin(math.radians((x * math.degrees(math.sin(math.radians(y)))/ z))))

def law_of_sin_side(x,y,z):
     return ((x * math.degrees(math.sin(math.radians(y))))/ math.degrees(math.sin(math.radians(z))))

def law_of_cos_side(x,y,z):
    return math.sqrt(x ** 2 + y ** 2 - (2 *x) * (y) * math.cos(math.radians(z)))

def law_of_cos_angle(x,y,z):
     return math.degrees(math.acos((x ** 2 + y ** 2 - z ** 2)/ (2 * x * y)))
     
def third_angle(a,b):
    return 180 - (a + b)

def angle_prompt_and_validation_a():
    while True:
        a = input(("Angle A: "))
        if not float(a.isnumeric()) or float(a) > 180:
            print("Angles are always a numeric value and cannot exceed 180°")
            continue
        elif float(a) <= 0:
            print("Angle measure must be > 0")
        else:
            a = float(a)
            break
    return a
    
def angle_prompt_and_validation_b():
    while True:
        a = input(("Angle B: "))
        if not float(a.isnumeric()) or float(a) > 180:
            print("Angles are always a numeric value and cannot exceed 180°")
            continue
        elif float(a) <= 0:
            print("Angle measure must be > 0")
            continue
        else:
            a = float(a)
            break
    return a

def angle_prompt_and_validation_c():
    while True:
        a = input(("Angle C: "))
        if not float(a.isnumeric()) or float(a) > 180:
            print("Angles are always a numeric value and cannot exceed 180°")
            continue
        elif float(a) <= 0:
            print("Angle measure must be > 0")
            continue
        else:
            a = float(a)
            break
    return a

def side_prompt_and_validation_a():
    while True:
        a = input(("Side a: "))
        if not float(a.isnumeric()):
            print("Sides are always a numeric value")
            continue
        elif float(a) <= 0:
            print("Side measure must be > 0")
            continue
        else:
            a = float(a)
            break
    return a

def side_prompt_and_validation_b():
    while True:
        a = input(("Side b: "))
        if not float(a.isnumeric()):
            print("Sides are always a numeric value")
            continue
        elif float(a) <= 0:
            print("Side measure must be > 0")
            continue
        else:
            a = float(a)
            break
    return a

def side_prompt_and_validation_c():
    while True:
        a = input(("Side c: "))
        if not float(a.isnumeric()):
            print("Sides are always a numeric value")
            continue
        elif float(a) <= 0:
            print("Side measure must be > 0")
            continue
        else:
            a = float(a)
            break
    return a

def validate_triangle(side_a,side_b,side_c):
    if(side_a + side_c <= side_b):
        print("Not a valid Triangle inequality: a + c <= b")
        exit()
    elif(side_a + side_b <= side_c):   
        print("Not a valid Triangle inequality: a + b <= c")
        exit()
    elif(side_b + side_c <= side_a):
        print("Not a valid Triangle inequality: b + c <= a")
        exit()

main()

import math
def main():
    ans = prompt()
    if ans == "A":
        A()
    elif ans == "B":
         B()
    elif ans =="C":
         C()
    else:
         print("Answer not found, please run the program again and enter 'A', 'B', or 'C'.")

def prompt():
    x = ""
    while (len(x) < 1):
        x = input("What information will you be providing me with today? \n A) 2 sides and the angle between those 2 sides \n B) 2 angles and one side in between those angles \n C) 3 sides and no angles \n Enter your letter choice below: \n").capitalize().strip()
    return x

def A():
        side_a = float(input("Side a: "))
        side_b = float(input("Side b: "))
        angle_C = float(input("Angle C in degrees: "))
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

def B(): 
    angle_A = float(input(("Angle A: ")))
    angle_B = float(input(("Angle B: ")))
    side_c = float(input(("Side c: ")))
    angle_C = third_angle(angle_A, angle_B)
    side_a = law_of_sin_side(side_c, angle_A,angle_C)
    side_b = law_of_sin_side(side_c,angle_B,angle_C)
    area = calculate_area(side_a,side_b,side_c)
    print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area)  

def C():
     side_a = float(input(("Side a: ")))
     side_b = float(input(("Side b: ")))
     side_c = float(input(("Side c: ")))
     if(side_a + side_c <= side_b) or (side_a + side_b <= side_c) or (side_b + side_c <= side_a):
        print("Not a valid Triangle inequality: a + c <= b")
        return
     elif(side_a + side_b <= side_c):   
        print("Not a valid Triangle inequality: a + b <= c")
        return
     elif(side_b + side_c <= side_a):
        print("Not a valid Triangle inequality: b + c <= a")
        return
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

main()

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
        side_c = math.sqrt(side_a ** 2 + side_b ** 2 - (2 *side_a) * (side_b) * math.cos(math.radians(angle_C)))
        smallest_side = min([side_a, side_b])
        if smallest_side == side_b:
            sin_b = (side_b * math.degrees(math.sin(math.radians(angle_C)))/ side_c)
            angle_B = math.degrees(math.asin(math.radians(sin_b)))
            angle_A = 180 - (angle_C + angle_B)
        if smallest_side == side_a: 
            sin_a = (side_a * math.degrees(math.sin(math.radians(angle_C)))/ side_c)
            angle_A = math.degrees(math.asin(math.radians(sin_a)))
            angle_B = 180 - (angle_C + angle_A)
        area = calculate_area(side_a,side_b,side_c)
        print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area) 
def B(): 
    angle_A = float(input(("Angle A: ")))
    angle_B = float(input(("Angle B: ")))
    side_c = float(input(("Side c: ")))
    angle_C = 180 - (angle_A + angle_B)
    side_a = ((side_c * math.degrees(math.sin(math.radians(angle_A))))/ math.degrees(math.sin(math.radians(angle_C))))
    side_b = ((side_c * math.sin(math.radians(angle_B)))/math.sin(math.radians(angle_C)))
    area = calculate_area(side_a,side_b,side_c)
    print_results(side_a,side_b,side_c,angle_A,angle_B,angle_C, area)    
def C():
     side_a = float(input(("Side a: ")))
     side_b = float(input(("Side b: ")))
     side_c = float(input(("Side c: ")))
     if(side_a + side_c <= side_b):
          print("Not a valid Triangle inequality: a + c <= b")
          return
     cos_c  = (side_a ** 2 + side_b ** 2 - side_c ** 2) / (2* (side_a ) * (side_b)) 
     angle_C = math.degrees(math.acos((cos_c)))
     sin_a = (side_a  * math.degrees(math.sin(math.radians(angle_C)))) / side_c
     angle_A = math.degrees(math.asin((math.radians(sin_a))))
     angle_B = 180-(angle_A + angle_C)
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
main()

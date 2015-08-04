#########################################################
#Name: Thalla Divya
#Class: CMPS 5363 Cryptography
#Date: 4th August 2015
#Program 3 - Elliptical Curve Encryption
#########################################################
import argparse
import sys
import ellipse as p
import fractions

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--scalar", dest="a", help="Given y^2 = x^3 + a*x + b: Input 'a'")
    parser.add_argument("-b", "--constant", dest="b", help="Given y^2 = x^3 + a*x + b: Input 'b'")
    parser.add_argument("-x1", "--firstXValue", dest="x1", help="Given P1(x1,y1): Input x1")
    parser.add_argument("-y1", "--firstYValue", dest="y1", help="Given P1(x1,y1): Input y1")
    parser.add_argument("-x2", "--secondXValue", dest="x2", help="Given P2(x2,y2): Input x2")
    parser.add_argument("-y2", "--secondYValue", dest="y2", help="Given P1(x2,y2): Input y2")
    args = parser.parse_args()
    print("a=", args.a, "b=", args.b, "x1=", args.x1, "y1=", args.y1, "x2=", args.x2, "y2=", args.y2)
    a = fractions.Fraction(args.a)
    b = fractions.Fraction(args.b)
    x1 = fractions.Fraction(args.x1)
    x2 = fractions.Fraction(args.x2)
    y1 = fractions.Fraction(args.y1)
    y2 = fractions.Fraction(args.y2)
    print("Elliptical Curve Equation:y^2 = x^3 +", a, "* x +", b)
   #checking the condition that the points passing through the curve or not
    if (y1**2) == (x1**3) + (a*x1) + b and (y2**2) == (x2**3) + (a*x2) + b:
        print("points  lie on the curve")
    else:
        print("points does not lie on the curve")    
    #If x values are similar derivative slope is used instead of point slope
    if x1 == x2 or y1 == y2:
        m = (3 * x1**2 + a) / (2 * y1)
    else:
        m = (y1-y2)/(x1-x2)
    
   #Determining the third coordinate
    x3 = fractions.Fraction((m**2) - x1 - x2).limit_denominator(1000)
    y3 = fractions.Fraction(y1 + m * (x3-x1)).limit_denominator(1000)
    print(x3,y3)
    Max = max(abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3))
    #width and height of plot
    w = Max + 10
    h = Max + 10
	#passing the values to plot graph
    p.plotcurve(w,h,a,b,m,x1,y1,x2,y2,x3,y3)
      
if __name__ == '__main__':
    main()

print("Perform various Things")
print("1.Check even/Odd\n2.Check which is greater no.\n3.Check if you can vote?\n4.Tables\n5.Exit")
while True:
    try:
        n=int(input("Enter your choice: "))
        if n==5:
            print("Exit is Success")
            break
        if 0<n<=4:
            if n==1:
                a=int(input("Enter the number:"))
                if a%2==0:
                    print(f"{a} is an even number")
                else:
                    print(f"{a} is an odd number")
            elif n==2:
                b=int(input("Enter the 1st number:"))
                c=int(input("Enter the 2nd number:"))
                if b>c:
                    print(f"{b} is greater than {c}")
                elif b<c:
                    print(f"{b} is smaller than {c}")
                else:
                    print(f"{b} & {c} are equal")
            elif n==3:
                d=int(input("Enter your age:"))
                if d>=18:
                    print("Ofcourse you can vote!")
                else:
                    print("No you cannot, because your age is less than 18")
            elif n==4:
                e=int(input("Enter the number:"))
                for i in range(11):
                    print(f"{e} x {i} = {e*i}")
        else:
            print("Enter between 1-5")
    except ValueError:
        print("Only numeric values are accepted,other input might give an error")

    
                    

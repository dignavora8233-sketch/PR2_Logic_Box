#Logic Box

print("Welcome to the Pattern Generator and Number Analyzer!")

print("select an option:")

while True:
   
    print("1.Generate a Pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")

    choice=input("Enter Your Choice:")

    if choice == "1":
         rows=int(input("how many rows:"))
         print("Pattern")

         for i in range(1,rows+1):
             for j in range(i):
                 print("*",end="")
             print()

    elif choice == "2":

        first=int(input("Enter starting number:"))
        last=int(input("Enter ending number:"))

        sum_num=0
        
        for num in range(first,last+1):
            if num % 2 == 0:
                print(num,"Even")
            else:
                print(num,"Odd")

            sum_num += num
                
        print("Total Sum:",sum_num)

    elif choice == 3:
        print("Exiting the program.Goodbye!")

        break
    
    else:
        print("Please enter avalid choice.")

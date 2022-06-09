n_t = int(input ("How many terms the user wants to print? "))  
  
# First two terms  
n_1 = 0  
n_2 = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if n_t <= 0:  
    print ("Please enter a positive integer, the given no. is not valid")  
# if there is only one term, it will return n_1  
elif n_t == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_t, ": ")  
    print(n_1)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the no.s is:")  
    while count < n_t:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1 

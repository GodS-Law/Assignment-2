#This "a" represents the count(Total)
a = 0

#This loops counts and adds the numbers in the range.
#I wrote 51 instead of 50 because it does not count 50 if I write 50 there.
for i in range(1,51):
    a += i

#This prints the result of the calculation
print(f'The sum of numbers from 1 to 50 is: {a}')

'''
#This is something I tried to make for custom value inputs.
#But I can not get the negative and other sum with this like sum from 90 to 30 or 9 to -4. 
#Why cannot it sums for these types of value?
#Would you please tech me why, Thank you very much.

start = int(input("From: "))
end = int(input("To: "))
total = 0

for i in range(start,end + 1):
    total += i
    
print(f'The total is {total}')
'''
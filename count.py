n=int(input("enter a value: "))

even_count=0
odd_count=0

for i in range(1,n+1):
    if i%2 ==0:
        even_count+=1
    else:
        odd_count+=1

print("even number count is: ",even_count)
print("odd number count is:",odd_count)

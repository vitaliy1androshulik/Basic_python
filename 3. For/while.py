i=0
n=5
while i<n:
    print(f"i= {i+1}")
    i+=1

mas=range(1,10)
for item in mas:
    if item==3:
        continue
    print(item)
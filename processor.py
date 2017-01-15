import csv
a = []
b = []
temp = []
norms = [0,0,0,0,0,0,0,0,0,0,0]
with open("output.csv","rb") as f:
	reader = csv.reader(f)
	for row in reader:
		lrow = list(row)
		for i in range(0,len(lrow)):
			if(float(lrow[i])>norms[i]):
				norms[i]=float(lrow[i])			
		a.append(lrow)
			
#print(a)
print(norms)

for row in a:
	for x in range(0,len(row)):
		temp.append(float(row[x])/norms[x])	
	b.append(temp)
	temp = []

print "end"
print b

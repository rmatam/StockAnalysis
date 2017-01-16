import csv
from sys import argv

ticker = argv[1]
a = []
b = []
temp = []
norms = [0,0,0,0,0,0,0,0,0,0,0]
with open(ticker+"_raw.csv","r") as f:
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

print( "end")
print( b)
print("stuff")
print(b[0][0])
print("b[1000][0]="+str(b[1000][0]))
with open(ticker+"_norm.csv","w") as f:
	writer = csv.writer(f)
	writer.writerows(b)

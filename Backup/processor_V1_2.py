import csv
from sys import argv

#ticker = argv[1]

def process(ticker):
	a = []
	b = []
	temp = []

	norms = []
	#norms = [0,0,0,0,0,0,0,0,0,0,0]
	firstRow=True
	with open("StockData/"+ticker+"_raw.csv","r") as f:
		reader = csv.reader(f)#create a csv reader
		for row in reader:#loop over each row (date)
			lrow = list(row)
			#print(lrow)
			if firstRow:
				numNorms=len(lrow)
				print(numNorms)
				firstRow=False
				for x in range(0,numNorms):
					norms.append(0)

			for i in range(0,len(lrow)):
			
				if(abs(float(lrow[i]))>norms[i]):
					norms[i]=abs(float(lrow[i]))			
			a.append(lrow)

	#create a normalization constant (starting at zero) for each column
	#numNorms = len(a[0])
	#print(len(norms))
	#print(numNorms)
	#for x in range(0,numNorms):
	#	norms.append(0)

	print(norms)

	for row in a:
		for x in range(0,len(row)):
			temp.append(float(row[x])/norms[x])	
		b.append(temp)
		temp = []

	print( "end")
	#print( b)
	#print("stuff")
	#print(b[0][0])
	#print("b[1000][0]="+str(b[1000][0]))
	with open("StockData/"+ticker+"_norm.csv","w") as f:
		writer = csv.writer(f)
		writer.writerows(b)

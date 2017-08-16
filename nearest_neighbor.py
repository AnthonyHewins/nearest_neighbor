import numpy as np
import pandas
import matplotlib.pyplot as plot
import random as r
import math

n = 100

def main():
	positive, negative = generate_random_data()
	classify([[0] + point], positive, negative)
	scatterplot(negative, positive, point)
	
def generate_random_data():
	positive, negative = matrix_creation(1), matrix_creation(0)
	return positive, negative

def scatterplot(negative, positive, point):
	plot.scatter(positive.iloc[0:, 0], positive.iloc[0:,1], alpha=0.5, color='r')
	plot.scatter(negative.iloc[0:, 0], negative.iloc[0:,1], alpha=0.5, color='b')
	plot.scatter(point[0], point[1], color='purple')
	plot.show()

def matrix_creation(bit):
	start = 0 if bit else n//2
	stop = n//2 if bit else n
	data = []
	for i in range(start, stop):
		data += [[r.uniform(start,stop), r.uniform(0,100)]]
	return pandas.DataFrame(sorted(data))

def classify(lst, positive, negative):
	least_distance = float("inf")
	answer = 0
	hypotenuse = 0
	n = np.array(negative.values)
	p = np.array(positive.values)
	for i in lst:
		for j in n:
			hypotenuse = distance(i[1:3],j)
			if hypotenuse < least_distance:
				print("Next closest point from negative:", j)
				least_distance = hypotenuse
				answer = 0
		for j in p:
			hypotenuse = distance(i[1:3],j)
			if hypotenuse < least_distance:
				print("Next closest point from positive:", j)
				least_distance = hypotenuse
				answer = 1
		print("Answer:", answer)
		if answer == i[0]:
			print("Correct")
		else:
			print("Wrong")
		
def distance(p0,p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
		
main()

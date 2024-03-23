

import time
import math

def calculate_time(func):

	def inner_wrapper(*args, **kwargs):
		begin = time.time()

		#run the function
		func(*args,**kwargs)

		end = time.time()

		print ( "total time taken by the funtion {} is {} sec".format(func.__name__, end - begin))

	return inner_wrapper

@calculate_time
def factorial(num):

	#time.sleep(2)

	print (math.factorial(num))




# a new decorator funtion


def func_dec(func):

	def inner_wrapper(*args,**kwargs):
		print("this is the begining of the funtion")


		value = func(*args, **kwargs)

		print ("this is the end of the funtion")

		return value

	return inner_wrapper



@func_dec

@calculate_time


def sum1(a, b):

	print ("Now we are in the sum Fucntion")
	c = a + b

	print ("we did the calculation and here is the end of this Fucntion", c )
	
	#return c 



soo= sum1(8,9)
#print (soo)








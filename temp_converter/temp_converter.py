#!/usr/bin/python3
"""
    temp.py: converts celsius to fahrenheit
    created by: christine roe
    course number: csc138-en
    created on: 09082024
    changes made: added paranthesis added comments
"""
# process
# conversion formula
# def c2f(c):
# return c * (9.0 / 5.0) + 32.0 #pemdas

def f2c_raw(f): 
	return f - 32 * 5 / 9
	
def f2c_op(f): 
	return (f - 32) * 5 / 9 #pemdas 
    
def main():
	f = 0
	c = f2c(f)
        print(f"{f}F is {c} C") 
    
if __name__ == "__main__":
	main() 
   
   

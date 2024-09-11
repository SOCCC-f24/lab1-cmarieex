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
def c2f(c):
    return c * (9.0 / 5.0) + 32.0

def main(cel):
    return c2f(cel)
    
if __name__ == "__main__":
    cel = 100         # input
    print(main(cel))  # output
   

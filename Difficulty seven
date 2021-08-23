import math
def get_middle(s):
    #Returns middle two or one chars of string
    m = math.ceil(len(s)/2)-1
    return s[0+m:len(s)-m]
    
def xo(s):
    #Return Bool, True if number of O or o == number of X or x in string
    s = s.lower()
    return s.count("o") == s.count("x")
    
def square_digits(num):
    #Squares each didget in number and concat in result
    s = ""
    for n in str(num):
        s += str(int(n)**2)
    return int(s)

# Work in progress.  intent is to create a bubbly programming language, with the following tokens:

#start: marks the start of a program
#return_ (return_ <value>): marks the end of a program, and returns the given <value>
#let (let <var_name> <value>): sets the variable <var_name> to the given <value>
#add (add <value> <value>) returns the sum of the two <value>
#sub (sub <value> <value>) returns the result of the first <value> minus the second <value>
#mul (mul <value> <value>) returns the product of the two <value>
#div (div <value> <value>) returns the result of the first <value> divided by the second <value> (integer division)

# (start)(return_)(add)(add)(5)(add)(3)(2)(5) should return 15
# (start)(let)('my_var')(add)(5)(8)(let)('banana')(mul)('my_var')(2)(return_)('banana')  should return 26

# Classes are not allowed in this challenge.  
# nor is the type function

#TODO marry callstack with argstack for a super stack, have the cont function continue eating from that stack wherever two valid values exist on the end.  

callstack = []
argstack = []
_dict = {}


# helpers
def get(arg):
    if arg in _dict:
        return _dict[arg]
    else:
        return arg


def cont(arg, arg2=None):
    # called by let, add, sub, mul, div. to continue executing until it can return its own value at its own depth
    if callable(arg):
        return arg
    else:
        func = callstack.pop(-1)
        arg2 = argstack.pop(-1)
        func(get(arg), get(arg2))
        #if len(callstack) > 0 and (callstack[-1] == return_ or callstack[-1] == let):
        if len(callstack) > 0 and
            if callstack[-1] == return_:
                return get(argstack[-1])
            if callstack[-1] == let:
                func = callstack.pop(-1)
                arg = argstack.pop(-1)
                arg2 = argstack.pop(-1)
                func(arg, arg2)
                return cont
        else:
            return cont




# Tokens: start, return_, let, add, sub, mul, div
def start(arg):
    _dict = {}
    return arg


def return_(arg, arg2=None):
    if arg2:
        return arg2
    else:
        callstack.append(return_)
        if callable(arg):
            return arg
        else:
            return get(arg)


def let(arg, arg2=None):
    global _dict
    if arg2:
        _dict[arg2] = arg
    else:
        callstack.append(let)
        if callable(arg):
            return arg
        else:
            argstack.append(arg)
        return cont


def add(arg, arg2=None):
    if arg2:
        argstack.append(arg2 + arg)
    else:
        callstack.append(add)
        if callable(arg):
            return arg
        else:
            argstack.append(arg)
        return cont


def sub(arg, arg2=None):
    if arg2:
        argstack.append(arg2 - arg)
    else:
        callstack.append(sub)
        if callable(arg):
            return arg
        else:
            argstack.append(arg)
        return cont

def mul(arg, arg2=None):
    if arg2:
        argstack.append(arg2 * arg)
    else:
        callstack.append(mul)
        if callable(arg):
            return arg
        else:
            argstack.append(arg)
        return cont


def div(arg, arg2=None):
    if arg2:
        argstack.append(arg2 / arg)
    else:
        callstack.append(div)
        if callable(arg):
            return arg
        else:
            argstack.append(arg)
        return cont

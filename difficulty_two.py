def calc(expression):
    #Evaluate basic mathimatical expressions without using eval() or exec() 

    NUMERIC = ".0123456789"
    # remove whitespace for easier parsing
    expression = expression.replace(" ", "")

    # convert string to more managable list
    expr_list = []
    running_n = ""
    i = 0
    while i < len(expression):
        while i < len(expression) and not expression[i] in NUMERIC:
            expr_list += expression[i]
            i += 1

        while i < len(expression) and expression[i] in NUMERIC:
            running_n += expression[i]
            i += 1
        else:
            if i < len(expression):
                expr_list.append(float(running_n))
                running_n = ""
    else:
        if len(running_n) > 0:
            expr_list.append(float(running_n))

    return sub_calc(expr_list)[0]


def sub_calc(e_list):
    # recursively evaluate all expressions in parentheses
    while "(" in e_list:
        left_index = e_list.index("(")
        right_index = left_index
        is_opn = -1

        # expression is opn until we've seen as many closing parentheses as we have opn ones.
        while is_opn:
            right_index += 1
            c = e_list[right_index]
            if c == "(":
                is_opn += -1
            elif c == ")":
                is_opn += 1
        left_index += 1

        n_e_list = e_list[left_index:right_index]
        e_list = e_list[:left_index - 1] + sub_calc(n_e_list) + e_list[right_index + 1:]

        
    #give all negative numbers a negative value
    if "-" in e_list:
        j = 0
        for i in range(e_list.count("-")):
            j = e_list.index("-", j)
            #sign is only a negative sign when the item to it's left is not a number and the item to its right is a number
            if (j == 0 or not isinstance(e_list[j - 1], float)) and isinstance(e_list[j + 1], float):
                e_list[j + 1] *= -1
                del e_list[j]
            j += 1
            
            
    while "*" in e_list or "/" in e_list:
        # brute force find first index of * or /
        i = 0
        while not (e_list[i] == "*" or e_list[i] == "/"):
            i += 1
        i -= 1
        n1 = e_list.pop(i)
        sym = e_list.pop(i)
        n2 = e_list.pop(i)

        e_list.insert(i, pseudo_eva(n1, n2, sym))

    while "+" in e_list or "-" in e_list:
        # brute force find first index of * or /
        i = 0
        while not (e_list[i] == "+" or e_list[i] == "-"):
            i += 1
        i -= 1
        n1 = e_list.pop(i)
        sym = e_list.pop(i)
        n2 = e_list.pop(i)

        e_list.insert(i, pseudo_eva(n1, n2, sym))

    return e_list


def pseudo_eva(n1, n2, sym):
    # Due to API restrictions, this is the best way I can think to translate the symbols to an operation
    if sym == "+":
        return n1 + n2
    elif sym == "-":
        return n1 - n2
    elif sym == "*":
        return n1 * n2
    elif sym == "/":
        return n1 / n2

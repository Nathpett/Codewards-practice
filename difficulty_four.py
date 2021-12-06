import re

def get_pins(observed):
    #brute force guesses a pin pad given seed values as potential ranges.  Returns list of all possible combinations given observed pin pad input offset by atleast one key horizontally or vertically.
    PIN_PAD = ["123", "456", "789", " 0 "]
    def get_potential_pins(c):
        #return string of all pins offset by 1 horizontal or vertical move on a pin pad, and also the seed pin c
        pins = ""
        pins += c
        for i in range(len(PIN_PAD)):
            row = PIN_PAD[i]
            if c in row:
                # horizontal pins
                h_index = row.index(c)
                if h_index != len(row) - 1:
                    pins += row[h_index + 1]
                if h_index != 0:
                    pins += row[h_index - 1]
                
                # vertical pins
                # i == v_index
                if i != len(PIN_PAD) - 1:
                    pins += PIN_PAD[i + 1][h_index]
                if i != 0:
                    pins += PIN_PAD[i - 1][h_index]
                    
                #delete "blank" pins
                pins = pins.replace(" ", "")
                
                return pins
    
    potential_pins = []
    for c in observed:
        potential_pins.append(get_potential_pins(c))
    
    r = set()
    index_list = [0] * len(potential_pins)
    while True:
        cur_combo = ""
        for i in range(len(potential_pins)):
            cur_index = index_list[i]
            cur_combo += potential_pins[i][cur_index]
        r.add(cur_combo)

        i = 0
        index_list[i] += 1
        while index_list[i] == len(potential_pins[i]):
            index_list[i] = 0
            i += 1
            if i == len(potential_pins):
                return list(r)
            index_list[i] += 1
            
    return r

def next_bigger(n):
    #returns the next biggest number that can be made using the given number's didgets
    #returns -1 if input is already the biggest number that can be made
    
    n = list(str(n))
    for i in range(len(n)):
        r = n[-1-i:]
        if r == sorted(r, reverse=True):
            continue
        highest_place = r[0]
        higher = [v for v in r if int(v) > int(highest_place)]
        next_largest = min(higher)
        r.remove(next_largest)
        return int("".join(n[:-1-i] + [next_largest] + sorted(r, reverse=False)))
    return -1
        
        
def knight(p1, p2):
    #returns minimum number of moves a knight in chess can make between two positions on a chess board
    #input is given as 'a1', 'h8', etc.
    
    #Going to use Breadth First Search.
    #node = column + row * 8
        #where row = ROWS.index(p[1])
        #and column = COLS.index(p[0])
    COLS = 'abcdefgh'
    ROWS = '12345678'
    K_MOVES = [-17, -15, -10, -6, 6, 10, 15, 17] 
    
    n0 = COLS.index(p1[0]) + 8 * ROWS.index(p1[1])
    nd = COLS.index(p2[0]) + 8 * ROWS.index(p2[1])
    
    visited = [None] * 64
    queue = [n0]
    
    found = False
    while queue and not found:
        n = queue.pop(0)
        n_col = n % 8
        valid_moves = [n + offset for offset in K_MOVES]
        valid_moves = [e for e in valid_moves if (0 <= e <= 63) and n_col - 2 <= (e % 8) <= n_col + 2]
        for e in valid_moves:
            if e == nd:
                found = True
            if visited[e] == None:
                visited[e] = n
                queue.append(e)

    #Traverse parents starting at nd to get to n0.
    series = [nd]
    while n0 not in series:
        n = series[-1]
        series.append(visited[n])
    
    return len(series) - 1

def valid_sudoku(board):
    #validates sudoku board, returns false if any 0s
    #board is a list of lists of length 9
    
    def simple_validate(_list):
        for row in _list:
            if sum(row) != 45:
                return False
            for i in range(1, 9):
                if row.count(i) != 1:
                    return False
        return True
    
    cells = [[] for i in range(9)]
    columns = [[] for i in range(9)]
    for i, row in enumerate(board):
        for j, n in enumerate(row):
            if n == 0:
                return False
            columns[j].append(n)
            cells[i//3 + 3 * (j//3)].append(n)
    
    return simple_validate(board) and simple_validate(cells) and simple_validate(columns)
    
def top_3_words(text):
    #returns top 3 most common words in a given text
    text = re.findall(r"[A-Za-z|']+", text)
    word_cts = {}
    for word in text:
        if word.count("'") != len(word):
            word = word.lower()
            word_cts[word] = word_cts.get(word, 0) + 1
    
    champs = []
    champ_ct = 0 #champ_ct is set by the 3rd place's count
    for word, ct in word_cts.items():
        if ct > champ_ct or len(champs) < 3:
            champs.append(word)
            champs.sort(key=word_cts.get, reverse = True)
            if len(champs) > 3:
                champs = champs[:3]
            champ_ct = word_cts[champs[-1]]
            
    return champs
    
    
  
  class RomanNumerals:
    #Class for encodeing and decoding roman numerals
    #ROMAN = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def to_roman(val):
        ROMAN = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
        def sub_to_roman(n, one):
            if n == 0:
                return ""
            elif n == 9:
                return ROMAN[one] + ROMAN[one * 10]
            elif 9 > n > 4:
                return  ROMAN[one * 5] + (n - 5) * ROMAN[one]
            elif n == 4:
                return ROMAN[one] + ROMAN[one * 5]
            else:
                return n * ROMAN[one]
        
        val = str(val).rjust(4, "0")
        r = ""
        if val[0] != "0":
            r += "M"*int(val[0])
        for i in range(3, 0, -1):
            n = int(val[-1*i])
            r += sub_to_roman(n, 10 ** (i- 1))
            
        return r


    def from_roman(roman_num):
        NUM = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        n = 0
        for i, c in enumerate(roman_num):
            if i != len(roman_num) - 1 and NUM[c] < NUM[roman_num[i+1]]:
                n -= NUM[c]
            else:
                n += NUM[c]
        
        return n

from math import ceil
#WIP MAJOR BREAKTHROUGH! ODD LENGTHS CHANGE INDEX BY 10, BUT EVEN CHANGE IT BY 9!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def find_reverse_number(n):
    r_len = 1
    skipped = 0
    while n >= 10 ** ceil(r_len / 2):
        skipped += 10 ** ceil(r_len / 2)
        n -= 10 ** ceil(r_len / 2)
        r_len += 1

    # With the length of r, we can assemble list of symmetrical 1/0 numbers, the index of which each element changes
    # n by 10^i
    sym_list = []
    for i in range(ceil(r_len / 2) - 1, -1, -1):
        sym = ["0"] * r_len
        sym[i] = "1"
        sym[r_len - 1 - i] = "1"
        sym_list.append(int("".join(sym)))

    # If we change r by value in sym_list at index i, n decreases by 10^i
    # starting at largest number, add values in sym_list until n==0

    r = sym_list[-1]
    i = len(sym_list) - 1
    while n > 0:
        if n >= 10 ** i:
            mult = n // 10 ** i
            n = n % 10 ** i
            r += mult * sym_list[i]
        else:
            i -= 1

    return r

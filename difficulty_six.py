def high(x):
    #returns word with highest "score", score the sum of a word's characters' index + 1 in the alphabet
    alp = 'abcdefghijklmnopqrstuvwxyz'
    def get_index_score(w):
        score = 0
        for c in w:
            score += alp.index(c) + 1
        return score
    
    champ = 0
    for word in x.split(" "):
        cur_score = get_index_score(word)
        if cur_score > champ:
            champ = cur_score
            champ_word = word
    return champ_word



def dig_pow(n, p):
    #returns k if any, where k is: (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k <abcd... being each didget in n>
    s = 0
    for i, d in enumerate(str(n)):
        d = int(d)
        s += d**(p + i)
    if s % n == 0:
        return s//n
    else:
        return -1


def bishop(start_pos, end_pos, num_moves):
    returns whether a bishop in chess can reach end_pos from start_pos given some number of moves num_moves
    row_l = "12345678"
    col_l = "abcdefgh"

    y, x = start_pos
    y, x = col_l.index(y), row_l.index(x)
    yy, xx = end_pos
    yy, xx = col_l.index(yy), row_l.index(xx)
    return ((x + y) % 2 == (xx + yy) % 2) \
           and ((num_moves == 0 and start_pos == end_pos) \
           or (num_moves == 1 and abs(x - xx) == abs(y - yy)) \
           or (num_moves >= 2))
           

def tower_builder(n_floors, brick = "*", space = " "):
    #returns pyramid of n_floors height
    return [(n_floors - 1 - i) * space + (i * 2 + 1) * brick + (n_floors - 1 - i) * space for i in range(n_floors)]
    
def likes(names):
    #given list of names, returns short summary of those who like it.
    l = len(names)
    if l == 0:
        return 'no one likes this'
    elif l == 1:
        return f'{names[0]} likes this'
    elif l == 2:
        return f'{names[0]} and {names[1]} like this'
    elif l == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {str(l - 2)} others like this'

def last_survivors(string):
    #substitute two equal letters by the next letter of the alphabet until no further substitutions can be made
    ALPHA = "abcdefghijklmnopqrstuvwxyza"
    _list = list(string)
    z_repeat = True
    
    while z_repeat:
        for c in ALPHA[:-1]:
            while _list.count(c) > 1:
                _list.remove(c)
                _list.remove(c)
                _list += ALPHA[ALPHA.index(c) + 1]
        else:
            z_repeat = _list.count('a') > 1
    return "".join(_list)


def decode(r):
    #decodes string encoding using following pseudocode
    #encode("mer", 6015)  -->  "6015ekx"
    # for each char in string, multiply index in ALPHA by n, take modulo, and use result as index in ALPHA for new encoded value

    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    
    c = "0"
    i = 0
    while c.isnumeric():
        c = r[i]
        i += 1
    i -= 1
    
    n = int(r[:i])
    s = r[i:]
    
    step = n % 26
    
    if step % 2 == 0 or step == 13:
        return "Impossible to decode"
    
    decode_key = [step * i % 26 for i in range(26)]
    sd = ''
    for c in s:
        i = ALPHA.index(c)
        sd += ALPHA[decode_key.index(i)]
    return sd

def uncollapse(digits):
    #Takes string of written out single didget numbers without spaces, returns with spaces
    # "fourfiveeightninenine" ==> "four five eight nine nine" 
    NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    s = []
    while digits:
        i = 0
        while digits[:i] not in NUMS:
            i += 1
        s.append(digits[:i])
        digits = digits[i:]
    return " ".join(s)
    
def encode_v1(text):
    #swaps 2nd and last letter, replaces first letter with its character code
    s = []
    if len(text) < 2: return text
    for word in text.split(" "):
        word = list(word)
        if len(word) > 1:
            word[-1], word[1] = word[1], word[-1]
        word[0] = str(ord(word[0]))
        s.append("".join(word))
    return " ".join(s)
    
def decipher_v1(string):
    s = []
    for word in string.split(" "):
        i = 1
        while word[:i].isnumeric() and i != len(word) + 1:
            i += 1
        i -= 1
        a = chr(int(word[:i]))
        word = list(word[i:])
        if len(word) > 1:
            word[0], word [-1] = word[-1], word[0]
        s.append(a + "".join(word))
    return " ".join(s)
    
def polybius(text):
    #encodes text with polybius square using the modern latin alphabet
    square = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    r = ""
    for c in text:
        if c in square:
            i = square.index(c)
            r += str(i//5 + 1) + str(i % 5 + 1)
        elif c == "J":
            r += "24"
        else:
            r += c
    return r

def bowling_pins(arr):
    #returns ASCII image of bowling pins minus those passed in arr
    crude = {1:27, 2:18, 3:20, 4:9, 5:11, 6:13, 7:0, 8:2, 9:4, 10:6}
    pins = list("I I I I\n I I I \n  I I  \n   I   ")
    for n in arr:
        pins[crude[n]] = " "
    return "".join(pins)

def get_simple_binomial(n):
    #returns expansion of (a+b)^n
    
    if n == 0:
        return '1'
    row = [1]
    r = ""
    #Generate row of pascal's triangle for coefficients 
    for i in range(abs(n)):
        row = [row[i] + row[i + 1] for i in range(len(row) - 1)]
        row = [1] + row + [1]
    p_row = [str(i) if i > 1 else "" for i in row]
        
    for i in range(abs(n) + 1):
        r += f'{p_row[i]}'
        if abs(n) - i > 0:
            if abs(n) - i > 1:
                r += f'a^{abs(n) - i}'
            else:
                r += 'a'
        if i > 0:
            if i > 1:
                r += f'b^{i}'
            else:
                r += 'b'
        r += '+'
    r = r[:-1]
    if n < 0:
        return f'1/({r})'
    else:
        return r

def columnize(items, columns_count):
    #Returns string of given items divided into columns, ljustifying and cell sizing as needed
    if len(items) < columns_count:
        return " | ".join(items)
    max_lens = [max([len(items[i]) for i in range(j, len(items), columns_count)]) for j in range(columns_count)]
    items = [item.ljust(max_lens[i % columns_count]) for i, item in enumerate(items)]
    delimiter_pattern = [" | "] * (columns_count - 1) + ["\n"]
    delimiters = [delimiter_pattern[i % len(delimiter_pattern)] for i in range(len(items))]
    delimiters[-1] = ""
    return "".join([items[i] + delimiters[i] for i in range(len(items))])

def narcissistic( value ):
    #Returns bool, whether number is narcissistic.  I.e. whether the sum of each didget raised to the number's total number of didgets is equal to the given number.  
    return value == sum([int(n) ** len(str(value)) for n in str(value)])

def wave(text):
    #returns list of given string actign as frames in an animated wave, where the wave is a capital letter
    return [text[:i] + text[i].upper() + text[i + 1:] for i in range(len(text)) if text[i] != " "]

def sum_multipule(n, m1, m2):
    #returns sum of all multiples of m1 or m2 for numbers up to n
    if n <= 0:
        return 0
    return sum([i for i in range(n) if i % m1 == 0 or m2 % 5 == 0])
  
def find_missing_number(numbers):
    #Returns missing number in unsorted list of numbers 1 to n
    return (len(numbers) + 1)/2 * (2 + len(numbers)) - sum(numbers)
    

from __future__ import print_function

def parse_field(info):
    return [int(x) for x in info.split(' ')]

def level1(info):
    """
    >>> print(level1("3 4"))
    1 2 3 4 8 7 6 5 9 10 11 12
    >>> print(level1("2 5"))
    1 2 3 4 5 10 9 8 7 6
    >>> print(level1("5 2"))
    1 2 4 3 5 6 8 7 9 10
    >>> print(level1("23 12"))
    1 2 3 4 5 6 7 8 9 10 11 12 24 23 22 21 20 19 18 17 16 15 14 13 25 26 27 28 29 30 31 32 33 34 35 36 48 47 46 45 44 43 42 41 40 39 38 37 49 50 51 52 53 54 55 56 57 58 59 60 72 71 70 69 68 67 66 65 64 63 62 61 73 74 75 76 77 78 79 80 81 82 83 84 96 95 94 93 92 91 90 89 88 87 86 85 97 98 99 100 101 102 103 104 105 106 107 108 120 119 118 117 116 115 114 113 112 111 110 109 121 122 123 124 125 126 127 128 129 130 131 132 144 143 142 141 140 139 138 137 136 135 134 133 145 146 147 148 149 150 151 152 153 154 155 156 168 167 166 165 164 163 162 161 160 159 158 157 169 170 171 172 173 174 175 176 177 178 179 180 192 191 190 189 188 187 186 185 184 183 182 181 193 194 195 196 197 198 199 200 201 202 203 204 216 215 214 213 212 211 210 209 208 207 206 205 217 218 219 220 221 222 223 224 225 226 227 228 240 239 238 237 236 235 234 233 232 231 230 229 241 242 243 244 245 246 247 248 249 250 251 252 264 263 262 261 260 259 258 257 256 255 254 253 265 266 267 268 269 270 271 272 273 274 275 276
    """
    rows, columns = parse_field(info)
    plots = range(rows * columns)
    seq = []
    for x in range(rows):
        start = columns * x + 1
        end = columns * (x + 1) + 1
        if x % 2 == 0:
            seq.extend(range(start, end))
        else:
            seq.extend(range(end - 1, start - 1, -1))

    output = ""
    for x in seq:
        output += str(x) + " "
    return output.rstrip()

def level2(info):
    """
    #>>> print(level2(""))
    """
    pass

def level3(info):
    """
    #>>> print(level3(""))
    """
    pass

def level4(info):
    """
    #>>> print(level4(""))
    """
    pass

def level5(info):
    """
    #>>> print(level5(""))
    """
    pass

def level6(info):
    """
    #>>> print(level6(""))
    """
    pass

def level7(info):
    """
    #>>> print(level7(""))
    """
    pass


def parse_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
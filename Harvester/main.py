from __future__ import print_function
import itertools

def parse_info(info):
    return [int(x) for x in info.split(' ')]

def concat_field(field):
    output = ""
    for x in itertools.chain.from_iterable(field):
        output += str(x) + " "
    return output.rstrip()

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
    rows, columns  = parse_info(info)
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
    >>> print(level2("3 4 1 1"))
    1 2 3 4 8 7 6 5 9 10 11 12
    >>> print(level2("2 5 2 1"))
    6 7 8 9 10 5 4 3 2 1
    >>> print(level2("5 2 5 2"))
    10 9 7 8 6 5 3 4 2 1
    >>> print(level2("23 12 1 12"))
    12 11 10 9 8 7 6 5 4 3 2 1 13 14 15 16 17 18 19 20 21 22 23 24 36 35 34 33 32 31 30 29 28 27 26 25 37 38 39 40 41 42 43 44 45 46 47 48 60 59 58 57 56 55 54 53 52 51 50 49 61 62 63 64 65 66 67 68 69 70 71 72 84 83 82 81 80 79 78 77 76 75 74 73 85 86 87 88 89 90 91 92 93 94 95 96 108 107 106 105 104 103 102 101 100 99 98 97 109 110 111 112 113 114 115 116 117 118 119 120 132 131 130 129 128 127 126 125 124 123 122 121 133 134 135 136 137 138 139 140 141 142 143 144 156 155 154 153 152 151 150 149 148 147 146 145 157 158 159 160 161 162 163 164 165 166 167 168 180 179 178 177 176 175 174 173 172 171 170 169 181 182 183 184 185 186 187 188 189 190 191 192 204 203 202 201 200 199 198 197 196 195 194 193 205 206 207 208 209 210 211 212 213 214 215 216 228 227 226 225 224 223 222 221 220 219 218 217 229 230 231 232 233 234 235 236 237 238 239 240 252 251 250 249 248 247 246 245 244 243 242 241 253 254 255 256 257 258 259 260 261 262 263 264 276 275 274 273 272 271 270 269 268 267 266 265
    """
    rows, columns, start_row, start_column = parse_info(info)

    field = generate_field(rows, columns)

    if start_row == rows:
        field.reverse()

    if start_column == columns:
        [row.reverse() for row in field]

    for i in range(len(field)):
        if i % 2 == 1:
            field[i].reverse()

    return concat_field(field)

def generate_field(rows, columns):
    field = []
    for r in range(rows):
        start = columns * r + 1
        end = columns * (r + 1) + 1
        field.append(range(start, end))
    return field

def level3(info):
    """
    >>> print(level3("3 4 1 1 S"))
    1 5 9 10 6 2 3 7 11 12 8 4
    >>> print(level3("2 5 1 5 S"))
    5 10 9 4 3 8 7 2 1 6
    >>> print(level3("5 2 5 2 N"))
    10 8 6 4 2 1 3 5 7 9
    >>> print(level3("23 12 23 1 N"))
    265 253 241 229 217 205 193 181 169 157 145 133 121 109 97 85 73 61 49 37 25 13 1 2 14 26 38 50 62 74 86 98 110 122 134 146 158 170 182 194 206 218 230 242 254 266 267 255 243 231 219 207 195 183 171 159 147 135 123 111 99 87 75 63 51 39 27 15 3 4 16 28 40 52 64 76 88 100 112 124 136 148 160 172 184 196 208 220 232 244 256 268 269 257 245 233 221 209 197 185 173 161 149 137 125 113 101 89 77 65 53 41 29 17 5 6 18 30 42 54 66 78 90 102 114 126 138 150 162 174 186 198 210 222 234 246 258 270 271 259 247 235 223 211 199 187 175 163 151 139 127 115 103 91 79 67 55 43 31 19 7 8 20 32 44 56 68 80 92 104 116 128 140 152 164 176 188 200 212 224 236 248 260 272 273 261 249 237 225 213 201 189 177 165 153 141 129 117 105 93 81 69 57 45 33 21 9 10 22 34 46 58 70 82 94 106 118 130 142 154 166 178 190 202 214 226 238 250 262 274 275 263 251 239 227 215 203 191 179 167 155 143 131 119 107 95 83 71 59 47 35 23 11 12 24 36 48 60 72 84 96 108 120 132 144 156 168 180 192 204 216 228 240 252 264 276
    """
    info = info.split(' ')
    rows = int(info.pop(0))
    columns = int(info.pop(0))
    start_row = int(info.pop(0))
    start_column = int(info.pop(0))
    direction = info.pop(0)

    field = generate_field(rows, columns)

    if start_row == rows:
        field.reverse()

    if start_column == columns:
        [row.reverse() for row in field]

    if direction in {'S', 'N'}:
        field = [list(x) for x in zip(*field)]

    for i in range(len(field)):
        if i % 2 == 1:
            field[i].reverse()

    return concat_field(field)

def level4(info):
    """
    >>> print(level4("3 4 1 4 S Z"))
    4 8 12 9 5 1 3 7 11 10 6 2
    >>> print(level4("2 5 2 1 N S"))
    6 1 2 7 8 3 4 9 10 5
    >>> print(level4("5 2 5 2 N Z"))
    10 8 6 4 2 1 3 5 7 9
    >>> print(level4("23 12 23 1 N Z"))
    265 253 241 229 217 205 193 181 169 157 145 133 121 109 97 85 73 61 49 37 25 13 1 12 24 36 48 60 72 84 96 108 120 132 144 156 168 180 192 204 216 228 240 252 264 276 266 254 242 230 218 206 194 182 170 158 146 134 122 110 98 86 74 62 50 38 26 14 2 11 23 35 47 59 71 83 95 107 119 131 143 155 167 179 191 203 215 227 239 251 263 275 267 255 243 231 219 207 195 183 171 159 147 135 123 111 99 87 75 63 51 39 27 15 3 10 22 34 46 58 70 82 94 106 118 130 142 154 166 178 190 202 214 226 238 250 262 274 268 256 244 232 220 208 196 184 172 160 148 136 124 112 100 88 76 64 52 40 28 16 4 9 21 33 45 57 69 81 93 105 117 129 141 153 165 177 189 201 213 225 237 249 261 273 269 257 245 233 221 209 197 185 173 161 149 137 125 113 101 89 77 65 53 41 29 17 5 8 20 32 44 56 68 80 92 104 116 128 140 152 164 176 188 200 212 224 236 248 260 272 270 258 246 234 222 210 198 186 174 162 150 138 126 114 102 90 78 66 54 42 30 18 6 7 19 31 43 55 67 79 91 103 115 127 139 151 163 175 187 199 211 223 235 247 259 271
    """
    """
    """
    info = info.split(' ')
    rows = int(info.pop(0))
    columns = int(info.pop(0))
    start_row = int(info.pop(0))
    start_column = int(info.pop(0))
    direction = info.pop(0)
    mode = info.pop(0)

    field = generate_field(rows, columns)

    #print(field)
    if start_row == rows:
        field.reverse()

    #print(field)
    if start_column == columns:
        [row.reverse() for row in field]

    #print(field)
    if direction in {'S', 'N'}:
        field = [list(x) for x in zip(*field)]

    #print(field)
    #print("mode", mode)
    if mode == 'Z':
        num_rows = len(field)
        for i in range(1, num_rows + 1):
            x = field[i:num_rows]
            x.reverse()
            field[i:num_rows] = x

    #print(field)
    for i in range(len(field)):
        if i % 2 == 1:
            field[i].reverse()
    #print(field)

    return concat_field(field)

def level5(info):
    """
    >>> print(level5(""))
    >>> print(level5(""))
    >>> print(level5(""))
    >>> print(level5(""))
    """
    """
    """
    info = info.split(' ')
    rows = int(info.pop(0))
    columns = int(info.pop(0))
    start_row = int(info.pop(0))
    start_column = int(info.pop(0))
    direction = info.pop(0)
    mode = info.pop(0)

    field = generate_field(rows, columns)

    #print(field)
    if start_row == rows:
        field.reverse()

    #print(field)
    if start_column == columns:
        [row.reverse() for row in field]

    #print(field)
    if direction in {'S', 'N'}:
        field = [list(x) for x in zip(*field)]

    #print(field)
    #print("mode", mode)
    if mode == 'Z':
        num_rows = len(field)
        for i in range(1, num_rows + 1):
            x = field[i:num_rows]
            x.reverse()
            field[i:num_rows] = x

    #print(field)
    for i in range(len(field)):
        if i % 2 == 1:
            field[i].reverse()
    #print(field)

    return concat_field(field)

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

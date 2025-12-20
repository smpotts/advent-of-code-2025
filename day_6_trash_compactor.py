import re
import math

pattern = re.compile(r'^[0-9]+$')

def clean_data(data):
    table = []
    for line in data.splitlines():
        row = []
        # removes leading and trailing white space
        columns = line.strip().split(' ')

        for c in columns:
            if bool(pattern.match(c)):
                row.append(int(c))
            elif c == '*' or c == '+':
                row.append(c)
        table.append(row)

    # print(table)
    return table

def main(input_type):
    file_name = f'data/day_6_{input_type}.txt' 
    with open(file_name, 'r') as file:
        print(f"Loading file '{file_name}'...")
        data = file.read()
        clean = clean_data(data)

        rows = len(clean)
        cols = len(clean[0])

        inversion = []
        column = []
        for c in range(cols):
            for r in range(rows):
                # print(f"r={r}, c={c}, value={clean[r][c]}")
                column.append(clean[r][c])
            inversion.append(column)
            column = []

        total = 0
        for element in inversion:
            symbol = element[-1]
            if symbol == '+':
                 total += sum(element[:-1])
            elif symbol == '*':
                total += math.prod(element[:-1]) 
        
        # print(inversion)
        print(total)


if __name__ == '__main__':
    main('input')

def load_input(day_number, input_type, comma_delimiter=False):
    file_name = f'data/day_{day_number}_{input_type}.txt' 
    with open(file_name, 'r') as file:
        print(f"Loading file '{file_name}'...")
        data = file.read()
        
        if comma_delimiter:
            return [item.strip() for item in data.split(',')]
        
        return [line.strip() for line in data.splitlines()]


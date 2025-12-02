
def load_input(day_number, input_type):
    file_name = f'data/day_{day_number}_{input_type}.txt' 
    with open(file_name, 'r') as file:
        print(f"Loading file '{file_name}'...")
        data = file.read()
        return data.splitlines()


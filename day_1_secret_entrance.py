from utils.data_loader import load_input

def check_zero_click(turns, current_position, step, n):
    count_zero = 0
    for _ in range(turns):
        # NOTE: this is an example of circular indexing
        # the key trick is using the modulo operator % with the length of the list
        # % operator gives a non-negative remainder
        current_position = (current_position + step) % n
        if current_position == 0:
            print("CLICKED ZERO!")
            count_zero += 1
    
    return current_position, count_zero


def main():
    data = load_input(1, 'input')
    dial_nums = list(range(100))
    count_zero = 0
    n = len(dial_nums)

    current_position = 50
    print(f"The dial starts by pointing at {current_position}")
    
    for entry in data:
        direction = entry[0]
        turns = int(entry[1:])

        if direction == 'L':
            step = -1
            current_position, hits = check_zero_click(turns, current_position, step, n)
            count_zero += hits
            print(f"The dial is rotated {entry} to point at {current_position}")
        elif direction == 'R':
            step = 1
            current_position, hits = check_zero_click(turns, current_position, step, n)
            count_zero += hits
            print(f"The dial is rotated {entry} to point at {current_position}")

    print(f"----- ZERO DIAL COUNT: {count_zero}! -----")    
    return count_zero

if __name__ == '__main__':
    main()
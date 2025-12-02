from utils.data_loader import load_input

def main():
    data = load_input(1, 'sample')
    dial_nums = list(range(100))
    count_zero = 0

    current_position = 50
    print(f"The dial starts by pointing at {current_position}")
    
    for entry in data:
        direction = entry[0]
        turns = int(entry[1:])

        if direction == 'L':
            passes = (turns - current_position + len(dial_nums) - 1) // len(dial_nums)
            count_zero += passes
            current_position = (current_position - turns) % len(dial_nums)
            print(f"The dial is rotated {entry} to point at {current_position}")
        elif direction == 'R':
            # NOTE: this is an example of circular indexing
            # the key trick is using the modulo operator % with the length of the list
            # % operator gives a non-negative remainder
            # use integer division here to get the "laps"
            passes = (current_position + turns) // len(dial_nums)
            count_zero += passes
            current_position = (current_position + turns) % len(dial_nums)
            print(f"The dial is rotated {entry} to point at {current_position}")


    print(f"Zero dial count: {count_zero}!!!")    
    return count_zero

if __name__ == '__main__':
    main()
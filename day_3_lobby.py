from utils.data_loader import load_input

def main():
    banks = load_input(3, 'input')

    total_joltages = []
    for battery in banks:
        char_list = list(battery)
        int_list = [int(c) for c in char_list]
        
        max_jolt = int(char_list[0])
        # print(f"orig max_jolt: {max_jolt}")
        joltage_options = []
        for i in range(0, len(int_list)-1):
            number = int_list[i]
            if number >= max_jolt:
                max_jolt = number
                # print(f"new max: {number}")
                max_ahead = max(int_list[i+1:])
                concat_num = str(max_jolt) + str(max_ahead)
                joltage_options.append(int(concat_num))
        
        total_joltages.append(max(joltage_options))
    print(total_joltages)
    print(f"TOTAL: {sum(total_joltages)}")


if __name__ == '__main__':
    main()
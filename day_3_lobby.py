from utils.data_loader import load_input

def part_1(int_list):
    max_jolt = int_list[0]
    joltage_options = []
    for i in range(0, len(int_list)-1):
        number = int_list[i]
        if number >= max_jolt:
            max_jolt = number
            max_ahead = max(int_list[i+1:])
            concat_num = str(max_jolt) + str(max_ahead)
            joltage_options.append(int(concat_num))
    return joltage_options


def main():
    banks = load_input(3, 'input')

    total_joltages = []
    for battery in banks:
        print(f"battery: {battery}")
        char_list = list(battery)

        greedy_list = []
        remove_elts = len(char_list) - 12 

        for c in char_list:
            i = int(c)
            # only pop if:
            # 1) there's something in the stack
            # 2) current digit is better than the last one
            # 3) there are more elements to remove
            while remove_elts > 0 and greedy_list and i > greedy_list[-1]:
                greedy_list.pop()
                remove_elts -= 1
            
            # always append current digit
            greedy_list.append(i)

        # remove leftover digits from the end if needed
        while remove_elts > 0:
            greedy_list.pop()
            remove_elts -= 1

        joltage = int("".join(map(str, greedy_list)))
        total_joltages.append(joltage)
        
    print(total_joltages)
    print(f"TOTAL: {sum(total_joltages)}")


if __name__ == '__main__':
    main()
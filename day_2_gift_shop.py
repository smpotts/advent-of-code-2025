from utils.data_loader import load_input

def main():
    data = load_input(2, 'input', True)
    invalid_ids = []

    for elt in data:
        start, end = elt.split('-')
        # print(f"Starting on {start} and ending on {end}.")

        for i in range(int(start), int(end) + 1):
            elt_str = str(i)
            mid = len(elt_str) // 2 # get the midpoint of the string
            left = elt_str[:mid]
            right = elt_str[mid:]

            if left == right:
                invalid_ids.append(int(elt_str))
    
    total = sum(invalid_ids) 
    print(f"TOTAL: {total}")
    return total


if __name__ == '__main__':
    main()
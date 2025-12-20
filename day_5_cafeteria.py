from utils.data_loader import load_input

def get_fresh_ids(fresh_id_ranges):
    range_pairs = []
    for pair in fresh_id_ranges:
        start, end = map(int, pair.split("-")) 
        range_pairs.append((start, end))
   
    # sort by the start
    range_pairs.sort()
    # print(range_pairs)

    # merge overlapping ranges
    flattened_ranges = []
    previous_start, previous_end = range_pairs[0]

    for start, end in range_pairs:
        # print(f"range_pair: {start}, {end}")
        if previous_start <= start <= previous_end:
            # print(f"overlap: {previous_start} <= {start} <= {end}")
            previous_end = max(previous_end, end)
        else:
            flattened_ranges.append((previous_start, previous_end))
            previous_start = start
            previous_end = end 

    flattened_ranges.append((previous_start, previous_end))
    
    total = 0
    for start, end in flattened_ranges:
        total += (end - start + 1)

    return total 


def main():
    fresh_id_ranges, available_ids = load_input(5, 'input', comma_delimiter=False, newline_separator=True)
    # print(fresh_id_ranges)
    # print(available_ids)

    # available_ids = [int(id) for id in available_ids]
    
    # fresh = 0
    # for available_id in available_ids:
    #     # print(f"available_id: {available_id}")
    #     for range_pair in fresh_id_ranges:
    #         start, end = map(int, range_pair.split("-")) 
    #         # print(f"range_pair: {range_pair}")
    #         if start <= available_id <= end:
    #             fresh += 1
    #             # print("found a fresh one!")
    #             break

    # print(f"fresh total: {fresh}")

    fresh_ingredients_count = get_fresh_ids(fresh_id_ranges)
    print(f"fresh ingredients total: {fresh_ingredients_count}")

if __name__ == '__main__':
    main()
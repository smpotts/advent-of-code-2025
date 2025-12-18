from utils.data_loader import load_input

def get_fresh_ids(fresh_id_ranges):
    # print(fresh_id_ranges)

    range_pairs = []
    for pair in fresh_id_ranges:
       start, end = map(int, pair.split("-")) 
       range_pairs.append((start, end))
    
    fresh_ingredients = set()
    for pair in range_pairs:
        for i in range(pair[0], pair[1]+1):
            fresh_ingredients.add(i)

    return fresh_ingredients


def main():
    fresh_id_ranges, available_ids = load_input(5, 'input', comma_delimiter=False, newline_separator=True)
    # print(fresh_id_ranges)
    # print(available_ids)

    available_ids = [int(id) for id in available_ids]
    
    fresh = 0
    for available_id in available_ids:
        # print(f"available_id: {available_id}")
        for range_pair in fresh_id_ranges:
            start, end = map(int, range_pair.split("-")) 
            # print(f"range_pair: {range_pair}")
            if start <= available_id <= end:
                fresh += 1
                # print("found a fresh one!")
                break

    # print(f"fresh total: {fresh}")

    fresh_ingredients = get_fresh_ids(fresh_id_ranges)
    print(f"fresh ingredients total: {len(fresh_ingredients)}")

if __name__ == '__main__':
    main()
from utils.data_loader import load_input


def remove_rolls(grid):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    rows = len(grid)
    cols = len(grid[0])

    accessible_count = 0

    # for each row and column
    for row in range(rows):
        for col in range(cols):
            roll_count = 0
            current_element = grid[row][col]
            if current_element == '@':
                # looking at each possible direction
                for dir_row, dir_col in directions:
                    neighbor_row = row + dir_row 
                    neighbor_col = col + dir_col

                    if neighbor_row >= 0 and neighbor_row < rows and neighbor_col >= 0 and neighbor_col < cols:
                        neighboring_value = grid[neighbor_row][neighbor_col]
                            
                        if neighboring_value == '@':
                            roll_count += 1
                            # print(f"neighbor_row: {neighbor_row}, neighbor_col: {neighbor_col}, roll_count: {roll_count}")
                    else:
                        continue

                if roll_count < 4:
                    grid[row][col] = '.'
                    accessible_count += 1 
        
    return accessible_count


def main():
    grid = load_input(4, 'sample')
    grid = [list(row) for row in grid]

    total_removed = 0
    while True:
        accessible_count = remove_rolls(grid)

        if accessible_count == 0:
            break

        total_removed += accessible_count
   
    print(f"total: {total_removed}")


if __name__ == '__main__':
    main()
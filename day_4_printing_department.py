from utils.data_loader import load_input

def main():
    grid = load_input(4, 'sample')
    print(grid)

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    rows = len(grid)
    cols = len(grid[0])

    # print(f"rows: {rows}, cols: {cols}")

    accessible_count = 0
    # for each row and column
    for row in range(rows):
        for col in range(cols):
            # looking at each possible direction
            for dir_row, dir_col in directions:
                # up to 4 steps away
                roll_count = 0
                for step in range(1, 5):
                    neighbor_row = row + dir_row * step
                    neighbor_col = col + dir_col * step

                    if neighbor_row >= 0 and neighbor_row < rows and neighbor_col >= 0 and neighbor_col < cols:
                        neighboring_value = grid[neighbor_row][neighbor_col]
                        
                        if neighboring_value == '@':
                            roll_count += 1
                            print(f"neighbor_row: {neighbor_row}, neighbor_col: {neighbor_col}, roll_count: {roll_count}")
                    
                    else:
                        break
                
            if roll_count < 4:
                accessible_count += 1
    
    print(f"accessibility_count: {accessible_count}")


if __name__ == '__main__':
    main()
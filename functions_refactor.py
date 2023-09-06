def main():
    grid = 4
    draw_grid(grid)

def draw_grid(grid):
    line = " ---"
    column = "|   "
    for i in range(grid):
        print(line*grid)
        print(column*(grid+1))
    print(line*grid)

if __name__ == "__main__":
    main()
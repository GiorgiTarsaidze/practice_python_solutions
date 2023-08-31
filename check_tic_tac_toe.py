winner_is_2 = [
    [2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [
    [0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


def main():
    matrix = winner_is_1
    row_winner = determine_rows(matrix)
    column_winner = determine_columns(matrix)
    diagonal_winner = determine_diagonals(matrix)
    
    if row_winner:
        print(row_winner)
    elif column_winner:
        print(column_winner)
    elif diagonal_winner:
        print(diagonal_winner)
    else:
        print("No winner.")

def determine_rows(matrix):
    for index in matrix:
        if len(set(index)) == 1:
            return f"Player {str(index[0])} Won!"
        
def determine_columns(matrix):
    for index in range(3):
        transposed_matrix = [[value[index] for value in matrix]]
        for element in transposed_matrix:
            if len(set(element)) == 1:
                return f"Player {str(element[0])} Won!"

def determine_diagonals(matrix):
    major_d = [matrix[i][i] for i in range(3)]
    minor_d = [matrix[i][2 - i] for i in range(3)]

    if len(set(major_d)) == 1:
        return f"Player {major_d[0]} won!"
    elif len(set(minor_d)) == 1:
        return f"Player {minor_d[0]} won!"
    
if __name__ == "__main__":
    main()
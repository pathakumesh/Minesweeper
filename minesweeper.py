no_of_cols = no_of_rows = 0

def display_mine(mine_values):
	
	for i in range(no_of_rows):
		for j in range(no_of_cols):
			print mine_values[i][j],
		print '\n'


def update_mine_index(mine_values, x, y):

	mine_count = 0
	for i in range(x - 1, x + 2):
		if i == -1 or i == no_of_rows:
			continue
		for j in range(y - 1, y + 2):
			if j == -1 or j == no_of_cols:	
				continue
			if mine_values[i][j] == '*':
				mine_count = mine_count + 1
	mine_values[x][y] = mine_count


def mine_operation():
	
	mine_values = []

	print '\nEnter values for each square beginning for left-top to right bottom'
	print 'separated by spaces and enter for next row\n>'
	for index in range(no_of_rows):
		input_values = []
		input_string = raw_input()
		input_values = input_string.split(' ')
		if len(input_values)!= no_of_cols or not all((v =='*' or v == '.') for v in input_values):
			print 'Input Value Error'
			mine_operation()
			return
		mine_values.append(input_values)
	for i in range(no_of_rows):
		for j in range(no_of_cols):
			if mine_values[i][j] == '.':
				update_mine_index(mine_values, i, j)
	print '\nTHE SOLUTION IS'
	print '==============='		
	display_mine(mine_values)
	
	
def main():
	global no_of_rows, no_of_cols
	input_values = [-1,-1]
	print 'Welcome to the minesweeper solver'
	while input_values[0] != '0' and input_values[1] != '0':
		
		try:
			input_string = raw_input('Enter the number of rows and columns separated by space: ( 0 0 to end)\n\t>>',)
			input_values = input_string.split(' ')
			no_of_rows, no_of_cols = int(input_values[0]), int(input_values[1])
			
			if (no_of_rows >0 and no_of_cols > 0):
				mine_operation()
		except:
			print 'Value Error'
			input_values = [-1,-1]
		
if __name__ == '__main__':
	main()
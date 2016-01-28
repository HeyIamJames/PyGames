def print_board(board):

	print "The board look like this: \n"

	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',	
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',
			
			if j != 2:
				print " | ",
		print
		
		if i != 2:
			print "-----------------"
		else: 
			print 

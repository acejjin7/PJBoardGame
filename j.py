def create_board() :
    board = []
    for i in range(6):
        board.append([])
        for j in range(5):
            if (int(i) == 1 and int(j) == 1):
                board[i].append("車")
            elif (int(i) == 1 and int(j) == 3):
                board[i].append("馬")
            elif (int(i) == 1 and int(j) == 2):
                board[i].append("龍")
            elif (int(i) == 2 and int(j) == 2): 
                board[i].append("兵")
            elif (int(i) == 3 and int(j) == 2):
                board[i].append("卒")
            elif (int(i) == 4 and int(j) == 1): 
                board[i].append("象")
            elif (int(i) == 4 and int(j) == 3):
                board[i].append("包")
            elif (int(i) == 4 and int(j) == 2):
                board[i].append("王")
            elif (i == 0 or i == 5):
                board[i].append("□")
            elif (j == 0 or j == 4):
                board[i].append("□")
            else:
                board[i].append("■")
    return board

def show_board(board):
    for i in range(6):
        for j in range(5):
            print(board[i][j],end="")
        print("")

def check_doing():
	do = input("포로를 소환하시겠습니까? 이동하시겠습니까? (소환, 이동) ")
	while not (do == "소환" or do == "이동"):
		do = input("포로를 소환하시겠습니까? 이동하시겠습니까? (소환, 이동) ")
	if (do == "소환"):
		return 0
	else:
		return 1

def check_alies1(horse):
	if (horse == "卒" or horse == "包" or horse == "王" or horse == "象"):
		return False
	else:
		return True

def check_alies2(horse):
	if (horse == "兵" or horse == "車" or horse == "龍" or horse == "馬"):
		return False
	else:
		return True

def check_alies2(horse):
	if (horse == "兵" or horse == "車" or horse == "龍" or horse == "馬" ):
		return False
	else:
		return True

def check_poro1(board):
	poro = []
	clone = []
	for i in range(1,5):
		for j in range(1,4):
			x = board[i][j]
			clone.append(x)
	if not ("兵" in clone):
		poro.append("卒")
	if not ("車" in clone):
		poro.append("包")
	if not ("馬" in clone):
		poro.append("象")
	return poro

def check_poro2(board):
	poro = []
	clone = []
	for i in range(1,5):
		for j in range(1,4):
			x = board[i][j]
			clone.append(x)
	if not ("卒" in clone):
		poro.append("兵")
	if not ("包" in clone):
		poro.append("車")
	if not ("象" in clone):
		poro.append("馬")
	return poro

def p1_select(board):
	clone = []
	for i in range(1,5):
		for j in range(1,4):
			x = board[i][j]
			clone.append(x)
	p1_select = input("이동하실 말을 선택해 주세요. (졸(卒), 포(包), 왕(王),상(象) ")
	while not (p1_select == "졸" or p1_select == "포" or p1_select == "왕" or p1_select == "상"):
		p1_select = input("이동하실 말을 선택해 주세요. (졸(卒), 포(包), 왕(王),상(象) ")
	return p1_select

def p2_select(board):
	clone = []
	for i in range(1,5):
		for j in range(1,4):
			x = board[i][j]
			clone.append(x)
	p2_select = input("이동하실 말을 선택해 주세요. (병(兵), 차(車), 용(龍), 마(馬) ")
	while not (p2_select == "병" or p2_select == "차" or p2_select == "용" or p2_select == "마"):
		p2_select = input("이동하실 말을 선택해 주세요. (병(兵), 차(車), 용(龍), 마(馬) ")
	return p2_select



def move_mini(board):
	for i in range(1,5):
		if ("卒" in board[i]):
			x = i
			y = board[i].index("卒")
			if (board[x-1][y] == "包" or board[x-1][y] == "象" or board[x-1][y] == "王"):
				print("움직일수 없습니다.")
			else:
				board[x][y], board[x-1][y] = "■", board[x][y] 
				print("졸은 오로지 앞으로만 움직입니다.")


def move_look(board):
	for i in range(1,5):
		if ("包" in board[i]):
			x = i
			y = board[i].index("包")
			while True:
				horse_move = input("이동방향을 선택해주세요. (↑ = 1, → = 2, ↓ = 3, ← = 4) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4"):
					horse_move = input("이동방향을 선택해주세요. (↑ = 1, → = 2, ↓ = 3, ← = 4) ")
				if (horse_move == "1" and check_alies1(board[x-1][y]) and board[x-1][y] != "□"):
					board[x][y], board[x-1][y] = "■", board[x][y]
					break
				elif (horse_move == "2" and check_alies1(board[x][y+1]) and board[x][y+1] != "□"):
					board[x][y], board[x][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "3" and check_alies1(board[x+1][y]) and board[x+1][y] != "□"):
					board[x][y], board[x+1][y] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies1(board[x][y-1]) and board[x][y-1] != "□"):
					board[x][y], board[x][y-1] = "■", board[x][y]
					break
				else:
					print("이동할수 없습니다.")



def move_king(board):
	for i in range(1,5):
		if ("王" in board[i]):
			x = i
			y = board[i].index("王")
			while True:
				horse_move = input("이동방향을 선택해주세요. (↑ = 1, ↗ = 2, → = 3, ↘ = 4, ↓ = 5, ↙ = 6, ← = 7, ↖ = 8) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4" or horse_move == "5" or horse_move == "6" or horse_move == "7" or horse_move == "8"):
					horse_move = input("이동방향을 선택해주세요. (↑ = 1, ↗ = 2, → = 3, ↘ = 4, ↓ = 5, ↙ = 6, ← = 7, ↖ = 8) ")
				if (horse_move == "1" and check_alies1(board[x-1][y]) and board[x-1][y] != "□"):
					board[x][y], board[x-1][y] = "■", board[x][y]
					break
				elif (horse_move == "3" and check_alies1(board[x][y+1]) and board[x][y+1] != "□"):
					board[x][y], board[x][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "5" and check_alies1(board[x+1][y]) and board[x+1][y] != "□"):
					board[x][y], board[x+1][y] = "■", board[x][y] 
					break
				elif (horse_move == "7" and check_alies1(board[x][y-1]) and board[x][y-1] != "□"):
					board[x][y], board[x][y-1] = "■", board[x][y]
					break
				elif (horse_move == "2" and check_alies1(board[x-1][y+1]) and board[x-1][y+1] != "□"):
					board[x][y], board[x-1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies1(board[x+1][y+1]) and board[x+1][y+1] != "□"):
					board[x][y], board[x+1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "6" and check_alies1(board[x+1][y-1]) and board[x+1][y-1] != "□"):
					board[x][y], board[x+1][y-1] = "■", board[x][y]
					break
				elif (horse_move == "8" and check_alies1(board[x-1][y-1]) and board[x-1][y-1] != "□"):
					board[x][y], board[x-1][y-1] = "■", board[x][y] 
					break
				else:
					print("이동 할 수 없습니다.")


	

def move_bishop(board):
	for i in range(1,5):
		if ("象" in board[i]):
			x = i
			y = board[i].index("象")
			while True:
				horse_move = input("이동방향을 선택해주세요. (↖ = 1, ↗ = 2, ↘ = 3, ↙ = 4) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4"):
					horse_move = input("이동방향을 선택해주세요. (↖ = 1, ↗ = 2, ↘ = 3, ↙ = 4) ")
				if (horse_move == "1" and check_alies1(board[x-1][y-1]) and board[x-1][y-1] != "□"):
					board[x][y], board[x-1][y-1] = "■", board[x][y] 
					break
				elif (horse_move == "2" and check_alies1(board[x-1][y+1]) and board[x-1][y+1] != "□"):
					board[x][y], board[x-1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "3" and check_alies1(board[x+1][y+1]) and board[x+1][y+1] != "□"):
					board[x][y], board[x+1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies1(board[x+1][y-1]) and board[x+1][y-1] != "□"):
					board[x][y], board[x+1][y-1] = "■", board[x][y]
					break
				else:
					print("이동할수 없습니다.")


def move_mini1(board):
	for i in range(1,5):
		if ("兵" in board[i]):
			x = i
			y = board[i].index("兵")
			if (board[x-1][y] == "車" or board[x-1][y] == "馬" or board[x-1][y] == "龍"):
				print("움직일수 없습니다.")
			else:
				board[x][y], board[x+1][y] = "■", board[x][y] 
				print("병은 오로지 앞으로만 움직입니다.")


def move_look1(board):
	for i in range(1,5):
		if ("車" in board[i]):
			x = i
			y = board[i].index("車")
			while True:
				print("!!")
				horse_move = input("이동방향을 선택해주세요. (↑ = 1, → = 2, ↓ = 3, ← = 4) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4"):
					horse_move = input("이동방향을 선택해주세요. (↑ = 1, → = 2, ↓ = 3, ← = 4) ")
				if (horse_move == "1" and check_alies2(board[x-1][y]) and board[x-1][y] != "□"):
					board[x][y], board[x-1][y] = "■", board[x][y]
					break
				elif (horse_move == "2" and check_alies2(board[x][y+1]) and board[x][y+1] != "□"):
					board[x][y], board[x][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "3" and check_alies2(board[x+1][y]) and board[x+1][y] != "□"):
					board[x][y], board[x+1][y] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies2(board[x][y-1]) and board[x][y-1] != "□"):
					board[x][y], board[x][y-1] = "■", board[x][y]
					break
				else:
					print("이동할수 없습니다.")

def move_king1(board):
	for i in range(1,5):
		if ("龍" in board[i]):
			x = i
			y = board[i].index("龍")
			while True:
				horse_move = input("이동방향을 선택해주세요. (↑ = 1, ↗ = 2, → = 3, ↘ = 4, ↓ = 5, ↙ = 6, ← = 7, ↖ = 8) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4" or horse_move == "5" or horse_move == "6" or horse_move == "7" or horse_move == "8"):
					horse_move = input("이동방향을 선택해주세요. (↑ = 1, ↗ = 2, → = 3, ↘ = 4, ↓ = 5, ↙ = 6, ← = 7, ↖ = 8) ")
				if (horse_move == "1" and check_alies2(board[x-1][y]) and board[x-1][y] != "□"):
					board[x][y], board[x-1][y] = "■", board[x][y]
					break
				elif (horse_move == "3" and check_alies2(board[x][y+1]) and board[x][y+1] != "□"):
					board[x][y], board[x][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "5" and check_alies2(board[x+1][y]) and board[x+1][y] != "□"):
					board[x][y], board[x+1][y] = "■", board[x][y] 
					break
				elif (horse_move == "7" and check_alies2(board[x][y-1]) and board[x][y-1] != "□"):
					board[x][y], board[x][y-1] = "■", board[x][y]
					break
				elif (horse_move == "2" and check_alies2(board[x-1][y+1]) and board[x-1][y+1] != "□"):
					board[x][y], board[x-1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies2(board[x+1][y+1]) and board[x+1][y+1] != "□"):
					board[x][y], board[x+1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "6" and check_alies2(board[x+1][y-1]) and board[x+1][y-1] != "□"):
					board[x][y], board[x+1][y-1] = "■", board[x][y]
					break
				elif (horse_move == "8" and check_alies2(board[x-1][y-1]) and board[x-1][y-1] != "□"):
					board[x][y], board[x-1][y-1] = "■", board[x][y] 
					break
				else:
					print("이동할수 없습니다.")

def move_bishop1(board):	
	for i in range(1,5):
		if ("馬" in board[i]):
			x = i
			y = board[i].index("馬")
			while True:
				horse_move = input("이동방향을 선택해주세요. (↖ = 1, ↗ = 2, ↘ = 3, ↙ = 4) ")  
				while not (horse_move == "1" or horse_move == "2" or horse_move == "3" or horse_move == "4"):
					horse_move = input("이동방향을 선택해주세요. (↖ = 1, ↗ = 2, ↘ = 3, ↙ = 4) ")
				if (horse_move == "1" and check_alies2(board[x-1][y-1]) and board[x-1][y-1] != "□"):
					board[x][y], board[x-1][y-1] = "■", board[x][y] 
					break
				elif (horse_move == "2" and check_alies2(board[x-1][y+1]) and board[x-1][y+1] != "□"):
					board[x][y], board[x-1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "3" and check_alies2(board[x+1][y+1]) and board[x+1][y+1] != "□"):
					board[x][y], board[x+1][y+1] = "■", board[x][y] 
					break
				elif (horse_move == "4" and check_alies2(board[x+1][y-1]) and board[x+1][y-1] != "□"):
					board[x][y], board[x+1][y-1] = "■", board[x][y]
					break
				else:
					print("이동할수 없습니다.")


def jang(p1_win,p2_win):
	board = create_board()
	while True:
		clone = []
		for i in range(1,5):
			for j in range(1,4):
				x = board[i][j]
				clone.append(x)
		if not ("王" in clone):
			print("플레이어 2 승리!")
			p2_win += 1
			break
		elif not ("龍" in clone):
			print("플레이어 1 승리!")
			p2_win += 1
			break
		show_board(board)
		p1_poro = check_poro1(board)
		print(p1_poro)
		p1_do = check_doing()
		if (p1_do == 0 and p1_poro != []):
			p1_summon(board,p1_poro)
		else:
			if (p1_do == 0):
				print("포로가 없으므로 이동합니다.")	
			p1 = p1_select(board)
			if  (p1 == "졸"):
				move_mini(board)
			elif (p1 == "포"):
				move_look(board)
			elif (p1 == "왕"):
				move_king(board)
			else:
				move_bishop(board)
		if not ("王" in clone):
			print("플레이어 2 승리!")
			p2_win += 1
			break
		elif not ("龍" in clone):
			print("플레이어 1 승리!")
			p2_win += 1
			break
		show_board(board)
		p2_poro = check_poro2(board)
		print(p2_poro)
		p2_do = check_doing()
		if (p2_do == 0 and p2_poro != []):
			p2_summon(board,p2_poro)
		else:
			if (p2_do == 0):
				print("포로가 없으므로 이동합니다.")
			p2 = p2_select(board)
			if (p2 =="병"):
				move_mini1(board)
			elif (p2 == "차"):
				move_look1(board)
			elif (p2 == "용"):
				move_king1(board)
			else:
				move_bishop1(board)


p1_win, p2_win = 0,0
jang(p1_win,p2_win)
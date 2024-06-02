def parse_board(input_lines):
    board = [line.split() for line in input_lines]
    return [[parse_s(s) for s in row] for row in board]

def parse_s(s):
    if s == "Start":
        return 0
    elif s == "End":
        return None
    elif s[0] == 'S':
        return -int(s[2:-1])
    elif s[0] == 'L':
        return int(s[2:-1])
    else:
        return int(s)

def is_valid_move(cur, move, end):
    if cur + move == end:
        return True
    elif cur + move < end:
        return False
    return True

def play_game(board, die_inputs):
    end = board[0][0] 
    cur = 0  
    num_snakes = 0
    num_ladders = 0

    for die in die_inputs:
        if die < 1 or die > 6:
            return "Not possible {} {}".format(num_snakes, num_ladders)

        while cur < end:
            next_s = cur + die

            if board[next_s // 10][next_s % 10] < 0:  
                cur = -board[next_s // 10][next_s % 10]
                num_snakes += 1
            elif board[next_s // 10][next_s % 10] > 0:  
                cur = board[next_s // 10][next_s % 10]
                num_ladders += 1
            else:
                cur = next_s

            if cur == end:
                return "Possible {} {}".format(num_snakes, num_ladders)

    return "Not possible {} {}".format(num_snakes, num_ladders)


input_lines = []
for _ in range(10):
    input_lines.append(input())

board = parse_board(input_lines)
die_inputs = list(map(int, input().split()))

result = play_game(board, die_inputs)
print(result)

import sys

def game_score(enemy, me):
    score = 0
    num_enemy, num_me = ord(enemy) - ord('A'), ord(me) - ord('X')
    
    if num_enemy == num_me:
        score = 3
    else:
        if (num_enemy == 0):
            if (num_me == 1):
                score = 6
        elif (num_enemy == 1):
            if (num_me == 2):
                score = 6
        elif (num_enemy == 2):
            if (num_me == 0):
                score = 6

    return score


FIXED_SCORE_PER_WIN = 6
variable_score_per_shape = {'X': 1, 'Y': 2, 'Z': 3}

def choose_type(enemy, status):
    type = ""
    if (status == 'Y'):
        type = chr(ord('X') + (ord(enemy)-ord('A')))
    elif (status == 'X'):
        type = chr(ord('X') + (ord(enemy)-ord('A')-1)%3)
    elif (status == 'Z'):
        type = chr(ord('X') + (ord(enemy)-ord('A')+1)%3)

    return type

score = 0
fich = open(sys.argv[1], 'r')

for line in fich:
    enemy, status = line.split()
    me = choose_type(enemy, status)
    score += variable_score_per_shape[me]
    score += game_score(enemy, me)
    print (enemy, me)

fich.close()

print(score)

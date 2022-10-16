import random

random_number = random.randint(1,100)
#print(random_number)

game_count = 1

while(True):
    
    try:
        guessed_num = int(input('1-100사이의 숫자를 입력하세요.'))
    except Exception as err:
        print('옳지못한 input error = {}'.format(err))
        
    if guessed_num > random_number:
        print('down')
    elif guessed_num < random_number:
        print('up')
        print('correct 게임횟수  = {}'.format(game_count))
        break
    game_count += 1
    
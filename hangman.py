answer = 'kangaroo'
board = []
guessed = []
max_guesses = 5


board = ['_'] * len(answer)

while ''.join(board) != answer and max_guesses > 0:
    guess = input('Guess a letter! ').lower() # handle caps error

    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                board[i] = guess
    else:
        max_guesses -= 1
        print('Sorry wrong guess. You have ', max_guesses, ' tries remaining.')
    
    guessed.append(guess)
    
    print('Current board', board)
    print('You guessed', guessed)
    print()
    
if max_guesses == 0:
    print('HANG MAN! YOU LOSE. GAME OVER')    

if ''.join(board) == answer:
    print('YOU WIN!')
    print('-------- GAME OVER -------')
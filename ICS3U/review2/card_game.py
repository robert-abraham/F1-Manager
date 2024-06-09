from Card import Card


player1 = Card()
player2 = Card()

#Either wins/tied
condition = ''

#Either Player1/ Player2
winner = ''

player1_SCORE = 0
player2_SCORE = 0 

game_state = True

while(game_state):
    player1.draw_card()
    player2.draw_card()
    
    if player1.get_card_value() > player2.get_card_value(): 
        condition = 'wins'
        winner = 'Player 1'
        player1_SCORE  += 1 

    if player1.get_card_value() == player2.get_card_value(): 
        condition = 'tie'
        winner = 'Player 1 and 2 '

    else:
        condition = 'wins'
        winner = 'Player 2 '
        player2_SCORE += 1        

    print(f"Player 1 Draws: {player1.get_card_name()}, Player 2 Draws: {player2.get_card_name()}, {winner} {condition}")
    print(f"Player 1 has {player1_SCORE} points, Player 2 has {player2_SCORE} points.")

    while(True):
        user_input = input("continue playing? (y/n) ")

        if user_input.lower() == "y":
            break

        if user_input.lower() == "n":
            game_state = False
            break
            

        else:
            print("invaild input")
from GamePlayer import * 

#Start code execution

#Construct Object, provide low and high range values
# for the move value
player1 = GamePlayer(1, 100) 
player2 = GamePlayer(1, 100)

#Play 10 rounds
for idx in range(10):
    print(f"\n** Round: {idx+1} **\n")

    player1.move()  #Player 1 makes a move
    player2.move()  #Player 2 makes a move

    #Output Player Move
    print(f" Player 1 Move: {player1.get_move_value()} Player 2 Move: {player2.get_move_value()}")
    print()

    #Decide Round winner
    if player1.get_move_value() == player2.get_move_value():
        print("Tie Round")
    elif player1.get_move_value() > player2.get_move_value():
        print("Player 1 wins round")
        player1.win()
    else:
        print("Player 2 wins round")
        player2.win()

    #Output game stats
    print(f"\n** Results after {idx+1} Round(s) **\n")
    print(f" Player 1 Rounds Won: {player1.get_wins()}")
    print(f" Player 2 Rounds Won: {player2.get_wins()}")

    #Pause, user can quit game if they wish
    if input("Q to quit or any other character to continue: ").strip().lower() == "q":
        print("Quitting game\n")
        break

#Determine the winner of the game
if player1.get_wins() == player2.get_wins:
    print("Tie game")
elif player1.get_wins() > player2.get_wins():
    print("Player 1 wins the game")
else:
    print("Player 2 wins the game")




import stdio
import stdrandom

# randomizes an int between the card and suit numbers
rank = stdrandom.uniformInt(2, 15)
suit = stdrandom.uniformInt(1, 5)

# displays the card that go with the random number
rankStr = ""
if rank == 14:
    rankStr = "Ace"
elif rank == 13:
    rankStr = "King"
elif rank == 12:
    rankStr = "Queen"
elif rank == 11:
    rankStr = "Jack"
else:
    rankStr = str(rank)

# displays the suit that go with the random number
suitStr = ''
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
elif suit == 4:
    suitStr = "Spades"

# displays the suit and the card
stdio.writeln(rankStr + " of " + suitStr)

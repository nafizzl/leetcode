# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

# Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

# Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
# Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other player wins.

# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

class P2038_RemoveColoredPiecesIfBothNeighborsAreTheSameColor:
    def winnerOfGame(self, colors: str) -> bool:
        colArr = list(colors);                            # convert string to char array
        alice = 0;
        bob = 0;                                          # make alice and bob counters
        i = 1;                                            # increment counter      

        while i < len(colArr) - 1:                        # run loop through second to second last indices
            if colArr[i] == colArr[i-1] == colArr[i+1]:
                if colArr[i] == 'A':
                    alice += 1
                if colArr[i] == 'B':
                    bob += 1                              # adjust scores for alice and bob as necessary
            i += 1                                        # increment
        
        if alice > bob:
            return True
        else:
            return False                                  # conditions on who wins based on scores

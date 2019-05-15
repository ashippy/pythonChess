#this file contains all of the classes of each type of chess piece

#Parent class Piece
class Piece(object):

    #dictionary of letter and its corresponding number. This is used to change a position on the chess board to a
    #a position in the 2D array
    fromLettertoNumb = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    #a dictionary of number and corresponding number. This is used to change a position in a 2D array to a position
    #on the chess board
    fromNumbtoLetter = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }

    #contructor, number of moves is always initialized at zero, everything else is initilaized in the child classes
    def __init__(self, player, value, pos, image, name):
        self.player = player
        self.value = value
        self.numberOfmoves = 0
        self.pos = pos
        self.image = image
        self.name = name;

    # This function is inherited by all of the classes. This function removes the positions in a list of possible moves
    #that is already occupied by a piece of the same color.

    def confirmValidMove(self, possibleMoves, chessboard):
        validMoves = []
        #iterate through all the moves in the list and check if that position is alreacy occupied by a piece of teh
        #same color
        for move in possibleMoves:
            #change from chess position to row and column in 2D array
            column, row = list(move.strip().lower())
            i = int(row) - 1
            j = Piece.fromLettertoNumb[column]
            piece = chessboard[i][j]
            #add to the valid moves array if the piece and piece in the destination position are not the same
            if not (isinstance(piece, int)):
                if self.player == 'black':
                    if piece.player != 'black':
                        validMoves.append([i, j])
                if self.player == 'white':
                    piece = chessboard[i][j]
                    if piece.player != 'white':
                        validMoves.append([i, j])
            #position is a zero and therfore empty so it can be added to the valid moves lsit
            else:
                validMoves.append([i, j])
        #convert back into chess board position format
        allValidMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in validMoves]
        allValidMoves.sort()
        return allValidMoves

    def allThreatenedSpots(self, board):
        allThreatenedSpots = []
        if self.player == 'white':
            for row in board:
                for piece in row:
                    if piece != 0 and piece.name != 'p':
                        if piece.player == 'black' and piece.name != 'k':
                            allThreatenedSpots.append(piece.moves(board))
                    if piece != 0 and piece.name == 'p' and piece.player == 'black':
                        dangerMoves = []
                        column, row = list(piece.pos.strip().lower())
                        row = int(row) - 1
                        column = Piece.fromLettertoNumb[column]
                        dangerMoves.append([row + 1, column + 1])
                        dangerMoves.append([row + 1, column - 1])
                        temp = [i for i in dangerMoves if i[0] >= 0 and i[1] >= 0 and i[0]<8 and i[1]<8]
                        pawnDanger = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
                        allThreatenedSpots.append(pawnDanger)

        else:
            for row in board:
                for piece in row:
                    if piece != 0 and piece.name != 'p':
                        if piece.player == 'white' and piece.name != 'k':
                            allThreatenedSpots.append(piece.moves(board))
                    if piece != 0 and piece.name == 'p' and piece.player == 'white':
                        dangerMoves = []
                        column, row = list(piece.pos.strip().lower())
                        row = int(row) - 1
                        column = Piece.fromLettertoNumb[column]
                        dangerMoves.append([row - 1, column + 1])
                        dangerMoves.append([row - 1, column - 1])
                        temp = [i for i in dangerMoves if i[0] >= 0 and i[1] >= 0 and i[0]<8 and i[1]<8]
                        pawnMoves = ["".join([self.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
                        allThreatenedSpots.append(pawnMoves)
        allMovesFlat = [item for sublist in allThreatenedSpots for item in sublist]
        return allMovesFlat

class Pawn(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 1, pos, image, 'p')

    def moves(self, chessBoard):
        # change from chess position to row and column in 2D array
        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        solutionMoves = []
        #if player is black pawn will be moving up the board, adding 1
        if self.player == 'black':
            #try statement checks to see if the chessboard position exits
            try:
                temp = chessBoard[row + 1][column]
                #pawn moves ahead one space if it is open
                if chessBoard[row +1][column] == 0:
                    solutionMoves.append([row + 1, column])
            #chessboard positoin does not exist, so continue
            except:
                pass
            try:
                temp = chessBoard[row + 1][column + 1]
                #pawn moves diagonally to the right one space if there is a piece there to capture
                if chessBoard[row + 1][column + 1] != 0:
                    solutionMoves.append([row + 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column - 1]
                #pawn moves diagonally to the left one space if there is a piece there to capture
                if chessBoard[row + 1][column - 1] != 0:
                    solutionMoves.append([row + 1, column - 1])
            except:
                pass
            try:
                temp = chessBoard[row + 2][column]
                #if it is the pawns first move it can move forward twice
                if self.numberOfmoves == 0:
                    solutionMoves.append([row + 2, column])
            except:
                pass
        #if player is white pieces are moving down the board and we will subtract
        #the below logic for the pawn moving is the same as above, but moving down the board instead
        if self.player == 'white':
            try:
                temp = chessBoard[row - 1][column]
                if chessBoard[row-1][column] == 0:
                    solutionMoves.append([row - 1, column])
            except:
                pass
            try:
                temp = chessBoard[row - 1][column + 1]
                if chessBoard[row - 1][column + 1] != 0:
                    solutionMoves.append([row - 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row - 1][column - 1]
                if chessBoard[row - 1][column - 1] != 0:
                    solutionMoves.append([row - 1, column - 1])
            except:
                pass
            try:
                temp = chessBoard[row - 2][column]
                if self.numberOfmoves == 0:
                    if chessBoard[row-2][column] ==0 & chessBoard[row-1][column] == 0:
                        solutionMoves.append([row - 2, column])
            except:
                pass
        # get rid of negative indexes
        temp = [i for i in solutionMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, allPossibleMoves, chessBoard)

        return validMoves


class Rook(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 7, pos, image, 'r')

    def moves(self, chessBoard):
        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        solutionMoves = []

        #add all the spots in the current row starting at the current positon and moving all the way to the
        #left of the board. Stop adding spots if there is a piece in the way, since a rook cant jump over pieces
        for i in range(row, -1, -1):
            if i != row:
                if chessBoard[i][column] != 0:
                    if chessBoard[i][column].player == self.player:
                        break
                    else:
                        solutionMoves.append((i, column))
                        break
                solutionMoves.append((i, column))
        #add all the spots in the current row starting at the current position and moving all the way to the left
        #off the board, break out of the for loop if  there is a piece in the way
        for i in range(row, 8, 1):
            if i != row:
                if chessBoard[i][column] != 0:
                    if chessBoard[i][column].player == self.player:
                        break
                    else:
                        solutionMoves.append((i, column))
                        break
                solutionMoves.append((i, column))
        #add all the spots in the current column starting at the current position and moving all the way to the bottom
        #off the board, break out of the for loop if  there is a piece in the way
        for j in range(column, -1, -1):
            if j != column:
                if chessBoard[row][j] != 0:
                    if chessBoard[row][j].player == self.player:
                        break
                    else:
                        solutionMoves.append((row, j))
                        break
                solutionMoves.append((row, j))
        #add all the spots in the current column starting at the current position and moving all the way to the top
        #off the board, break out of the for loop if  there is a piece in the way
        for j in range(column, 8, 1):
            if j != column:
                if chessBoard[row][j] != 0:
                    if chessBoard[row][j].player == self.player:
                        break
                    else:
                        solutionMoves.append((row, j))
                        break
                solutionMoves.append((row, j))

        #change from row and column in the board list to chess position format
        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, solutionMoves, chessBoard)
        return validMoves


class Queen(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 9, pos, image, 'q')

    #the logic of the queen moving is just the logic of the rook and the bishop combined
    def moves(self, chessBoard):
        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for i in range(row, -1, -1):
            if i != row:
                if chessBoard[i][column] != 0:
                    if chessBoard[i][column].player == self.player:
                        break
                    else:
                        solutionMoves.append((i, column))
                        break
                solutionMoves.append((i, column))

        for i in range(row, 8, 1):
            if i != row:
                if chessBoard[i][column] != 0:
                    if chessBoard[i][column].player == self.player:
                        break
                    else:
                        solutionMoves.append((i, column))
                        break
                solutionMoves.append((i, column))

        for j in range(column, -1, -1):
            if j != column:
                if chessBoard[row][j] != 0:
                    if chessBoard[row][j].player == self.player:
                        break
                    else:
                        solutionMoves.append((row, j))
                        break
                solutionMoves.append((row, j))
        for j in range(column, 8, 1):
            if j != column:
                if chessBoard[row][j] != 0:
                    if chessBoard[row][j].player == self.player:
                        break
                    else:
                        solutionMoves.append((row, j))
                        break
                solutionMoves.append((row, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if j < 8:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if 8 > j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, solutionMoves, chessBoard)

        return validMoves


class King(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 10, pos, image, 'k')

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        possibleMoves = []
        try:
            #move forward one
            temp = chessBoard[row + 1][column]
            possibleMoves.append([row + 1, column])
        except:
            pass
        try:
            #move backward one
            temp = chessBoard[row - 1][column]
            possibleMoves.append([row - 1, column])
        except:
            pass
        try:
            #move to the right one
            temp = chessBoard[row][column + 1]
            possibleMoves.append([row, column + 1])
        except:
            pass
        try:
            #move to the left one
            temp = chessBoard[row][column - 1]
            possibleMoves.append([row, column - 1])
        except:
            pass
        try:
            #move diagonally
            temp = chessBoard[row - 1][column - 1]
            possibleMoves.append([row - 1, column - 1])
        except:
            pass
        try:
            #move diagonally
            temp = chessBoard[row + 1][column + 1]
            possibleMoves.append([row + 1, column + 1])
        except:
            pass
        try:
            #move diagonally
            temp = chessBoard[row - 1][column + 1]
            possibleMoves.append([row - 1, column + 1])
        except:
            pass
        try:
            #move diagonally
            temp = chessBoard[row + 1][column - 1]
            possibleMoves.append([row + 1, column - 1])
        except:
            pass

        temp = [i for i in possibleMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, allPossibleMoves, chessBoard)

        threatened = Piece.allThreatenedSpots(self, chessBoard)
        print("here are all the threatened piecces")
        print(threatened)
        noCheck = []
        for move in validMoves:
            if move not in threatened:
                print("Checking if this move is in threatened moves")
                print(move)
                noCheck.append(move)

        return noCheck


class Bishop(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 5, pos, image, 'b')

    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        solutionMoves = []

        i, j = row, column
        #add all the positions diagonally to the left and up, starting at the current position and working to the
        #left side of the board. break out of the loop if the positoin is not empty, since a bishop cannot jump over
        #other pieces
        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        #add all the positions diagonally to the right and up, starting at the current position and working to the
        #right side of the board. break out of the loop if the positoin is not empty, since a bishop cannot jump over
        #other pieces
        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if 0 <= j < 8:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        #add all the positions diagonally to the left and down, starting at the current position and working to the
        #left side of the board. break out of the loop if the positoin is not empty, since a bishop cannot jump over
        #other pieces
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if 8 > j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        i, j = row, column
        #add all the positions diagonally to the right and down, starting at the current position and working to the
        #right side of the board. break out of the loop if the positoin is not empty, since a bishop cannot jump over
        #other pieces
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 0:
                        if chessBoard[i][j].player == self.player:
                            break
                        else:
                            solutionMoves.append((i, j))
                            break
                    solutionMoves.append((i, j))

        solutionMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, solutionMoves, chessBoard)

        return validMoves


class Knight(Piece):

    def __init__(self, player, pos, image):
        Piece.__init__(self, player, 5, pos, image, 'k')

    #knight can jump over other pieces and moves in an L shape
    def moves(self, chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = Piece.fromLettertoNumb[column]
        possibleMoves = []

        try:
            temp = chessBoard[row + 1][column - 2]
            possibleMoves.append([row + 1, column - 2])
        except:
            pass
        try:
            temp = chessBoard[row + 2][column - 1]
            possibleMoves.append([row + 2, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row + 2][column + 1]
            possibleMoves.append([row + 2, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column + 2]
            possibleMoves.append([row + 1, column + 2])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column + 2]
            possibleMoves.append([row - 1, column + 2])
        except:
            pass
        try:
            temp = chessBoard[row - 2][column + 1]
            possibleMoves.append([row - 2, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row - 2][column - 1]
            possibleMoves.append([row - 2, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column - 2]
            possibleMoves.append([row - 1, column - 2])
        except:
            pass

        temp = [i for i in possibleMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([Piece.fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()
        # take out positions that have a players piece at it
        validMoves = Piece.confirmValidMove(self, allPossibleMoves, chessBoard)

        return validMoves


class ComputerMoves(Pawn, Rook, Queen, Bishop, King):

    # def __init__(self,player,pos):

    def getdangerpieces(self):
        allPossibleMoves = Pawn.moves(Pawn)
        allPossibleMoves.extend(Rook.moves(Rook))
        allPossibleMoves.extend(Queen.moves(Queen))
        allPossibleMoves.extend(Bishop.moves(Bishop))
        allPossibleMoves.extend(King.moves(King))
        allPossibleMoves.extend(Knight.moves(Knight))
        return allPossibleMoves











class Piece(object):

    def __init__(self, player, value, name, pos):
        self.color = player.color
        self.value = value
        self.value = name
        self.numberOfmoves = 0
        self.pos = pos


class Pawn(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 1, 'Pawn', pos)

    def moves(chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
        solutionMoves = []
        if self.color == white:
            try:
                temp = chessBoard[row + 1][column]
                solutionMoves.append([row + 1, column])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column + 1]
                if chessBoard[row + 1][column + 1] != 1:
                    solutionMoves.append([row + 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column - 1]
                if chessBoard[row + 1][column - 1] != 1:
                    solutionMoves.append([row + 1, column - 1])
            except:
                pass
        if self.color == black:
            try:
                temp = chessBoard[row + 1][column]
                solutionMoves.append([row + 1, column])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column + 1]
                if chessBoard[row + 1][column + 1] != 1:
                    solutionMoves.append([row + 1, column + 1])
            except:
                pass
            try:
                temp = chessBoard[row + 1][column - 1]
                if chessBoard[row + 1][column - 1] != 1:
                    solutionMoves.append([row + 1, column - 1])
            except:
                pass
            # get rid of negative indexes
            temp = [i for i in solutionMoves if i[0] >= 0 and i[1] >= 0]
            allPossibleMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
            allPossibleMoves.sort()

            return allPossibleMoves


class Rook(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 7, 'Rook', pos)

    def moves(chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
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

        temp = [i for i in possibleMovess if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()

        return allPossibleMoves


class Queen(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 9, 'Queen', pos)

    def getQueenMoves(pos, board):
        column, row = list(pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if chessBoard[i][j] != 1:
                    break
                if j >= 0:
                    solutionMoves.append((i, j))

        i, j = row, column

        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if chessBoard[i][j] != 1:
                    break
                if j < 8:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for j in range(row, 0, -1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for j in range(row, 8, 1):
            if j != column:
                if chessBoard[row][j] != 1:
                    break
                solutionMoves.append((row, j))

        for i in range(column, 0, -1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))
        for i in range(column, 8, 1):
            if i != row:
                if chessBoard[i][column] != 1:
                    break
                solutionMoves.append((i, column))

        solutionMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()

        return solutionMoves


class King(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 10, 'King', pos)

    def moves(chessBoard):

        column, row = list(self.pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
        possibleMoves = []
        try:
            temp = chessBoard[row + 1][column]
            possibleMoves.append([row + 1, column])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column]
            possibleMoves.append([row - 1, column])
        except:
            pass
        try:
            temp = chessBoard[row][column + 1]
            possibleMoves.append([row, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row][column - 1]
            possibleMoves.append([row, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column - 1]
            possibleMoves.append([row - 1, column - 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column + 1]
            possibleMoves.append([row + 1, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row - 1][column + 1]
            possibleMoves.append([row - 1, column + 1])
        except:
            pass
        try:
            temp = chessBoard[row + 1][column - 1]
            possibleMoves.append([row + 1, column - 1])
        except:
            pass

        temp = [i for i in possibleMoves if i[0] >= 0 and i[1] >= 0]
        allPossibleMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()

        return allPossibleMoves


class Bishop(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 5, 'Bishop', pos)

    def getBishopMoves(pos, chessBoard):

        column, row = list(pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
        i, j = row, column
        solutionMoves = []

        for i in range(row, -1, -1):
            if i != row:
                j = j - 1
                if chessBoard[i][j] != 1:
                    break
                if j >= 0:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j + 1
                if chessBoard[i][j] != 1:
                    break
                if j < 8:
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, -1, -1):
            if i != row:
                j = j + 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        i, j = row, column
        for i in range(row, 8, 1):
            if i != row:
                j = j - 1
                if j >= 0:
                    if chessBoard[i][j] != 1:
                        break
                    solutionMoves.append((i, j))

        solutionMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
        solutionMoves.sort()

        return solutionMoves


class Knight(Piece):

    def __init__(self, player, pos):
        Piece.__init__(player, 5, 'Knight', pos)

    def getKnightMoves(pos, chessBoard):

        column, row = list(pos.strip().lower())
        row = int(row) - 1
        column = fromLettertoNumb[column]
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
        allPossibleMoves = ["".join([fromNumbtoLetter[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()
        print(allPossibleMoves)
        return allPossibleMoves


class ComputerMoves(Pawn,Rook,Queen,Bishop,King):

    #def __init__(self,player,pos):


    def getdangerpieces(self):
        allPossibleMoves = Pawn.moves(Pawn)
        allPossibleMoves.extend(Rook.moves(Rook))
        allPossibleMoves.extend(Queen.moves(Queen))
        allPossibleMoves.extend(Bishop.moves(Bishop))
        allPossibleMoves.extend(King.moves(King))
        allPossibleMoves.extend(Knight.moves(Knight))
        return allPossibleMoves










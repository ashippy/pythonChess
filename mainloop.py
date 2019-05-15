import os
import Classes
import Board
import pygame
import time
from random import *


def playerInCheck(board, pos):
    for row in board:
        for piece in row:
            if piece!=0:
                moves = piece.moves(board)
                if pos in moves:
                    return piece
    return False


def checkIfKingCanMove(board, threateningPieces):
    kingMoves =[]
    if threateningPieces.player == 'white':
        for row in board:
            for piece in row:
                if piece != 0:
                    if piece.name == 'k' and piece.player == 'black':
                        kingMoves.append(piece.moves(board))
        return kingMoves

    if threateningPieces.player == 'black':
         for row in board:
             for piece in row:
                 if piece != 0:
                     if piece.name == 'k' and piece.player == 'white':
                         kingMoves.append(piece.moves(board))
         return kingMoves


#this function accepts a the curent board, and a list of possible moves that the king can make,
#the threateningPieces is a lsit of pieces that are putting the king in check and are used to identify
#which colored king is in check
def removeCheck(board, kingMoves, threateningPiece):
    allMoves = []
    if threateningPiece.player == 'white':
        #iterate through all white pieces on the board and created a list of all the positions they can move to
        for row in board:
            for piece in row:
                if piece!= 0:
                    if piece.player == 'white':
                        moves = piece.moves(board)
                        allMoves.append(moves)
    #iterate through all the black pieces on teh board and create a list of all the positions they can move to
    if threateningPiece.player == 'black':
        for row in board:
            for piece in row:
                if piece !=0:
                    if piece.player == 'black':
                        moves = piece.moves(board)
                        allMoves.append(moves)
    #if the king can move then iterate through all the possible moves and check if that position is threatened by another
    #piece by checking if it is in the allMoves list, this is done since the king cannot put himself in check
    allMovesFlat = [item for sublist in allMoves for item in sublist]
    validMoves = []
    print(allMovesFlat)
    if len(kingMoves)>0:
        for move in kingMoves:
            if move not in allMovesFlat:
                print(move)
                #return a move once it is found to be possible
                validMoves.append(move)
        return validMoves

    #else the king cannot move anywhere so he is in check mate
    else:
        return 'check mate'


playerColor = 'black'

pawn1 = Classes.Pawn('black', 'a2', pygame.image.load("images/black_pawn.png"))
pawn2 = Classes.Pawn('black', 'b2', pygame.image.load("images/black_pawn.png"))
pawn3 = Classes.Pawn('black', 'c2', pygame.image.load("images/black_pawn.png"))
pawn4 = Classes.Pawn('black', 'd2', pygame.image.load("images/black_pawn.png"))
pawn5 = Classes.Pawn('black', 'e2', pygame.image.load("images/black_pawn.png"))
pawn6 = Classes.Pawn('black', 'f2', pygame.image.load("images/black_pawn.png"))
pawn7 = Classes.Pawn('black', 'g2', pygame.image.load("images/black_pawn.png"))
pawn8 = Classes.Pawn('black', 'h2', pygame.image.load("images/black_pawn.png"))
rook1 = Classes.Rook('black', 'a1', pygame.image.load("images/black_rook.png"))
rook2 = Classes.Rook('black', 'h1', pygame.image.load("images/black_rook.png"))
knight1 = Classes.Knight('black', 'b1', pygame.image.load("images/black_knight.png"))
knight2 = Classes.Knight('black', 'g1', pygame.image.load("images/black_knight.png"))
bishop1 = Classes.Bishop('black', 'c1', pygame.image.load("images/black_bishop.png"))
bishop2 = Classes.Bishop('black', 'f1', pygame.image.load("images/black_bishop.png"))
queen = Classes.Queen('black', 'd1', pygame.image.load("images/black_queen.png"))
king = Classes.King('black', 'e1', pygame.image.load("images/black_king.png"))
computerpawn1 = Classes.Pawn('white', 'a7', pygame.image.load("images/white_pawn.png"))
computerpawn2 = Classes.Pawn('white', 'b7', pygame.image.load("images/white_pawn.png"))
computerpawn3 = Classes.Pawn('white', 'c7', pygame.image.load("images/white_pawn.png"))
computerpawn4 = Classes.Pawn('white', 'd7', pygame.image.load("images/white_pawn.png"))
computerpawn5 = Classes.Pawn('white', 'e7', pygame.image.load("images/white_pawn.png"))
computerpawn6 = Classes.Pawn('white', 'f7', pygame.image.load("images/white_pawn.png"))
computerpawn7 = Classes.Pawn('white', 'g7', pygame.image.load("images/white_pawn.png"))
computerpawn8 = Classes.Pawn('white', 'h7', pygame.image.load("images/white_pawn.png"))
computerrook1 = Classes.Rook('white', 'a8', pygame.image.load("images/white_rook.png"))
computerrook2 = Classes.Rook('white', 'h8', pygame.image.load("images/white_rook.png"))
computerknight1 = Classes.Knight('white', 'b8', pygame.image.load("images/white_knight.png"))
computerknight2 = Classes.Knight('white', 'g8', pygame.image.load("images/white_knight.png"))
computerbishop1 = Classes.Bishop('white', 'c8', pygame.image.load("images/white_bishop.png"))
computerbishop2 = Classes.Bishop('white', 'f8', pygame.image.load("images/white_bishop.png"))
computerqueen = Classes.Queen('white', 'd8', pygame.image.load("images/white_queen.png"))
computerking = Classes.King('white', 'e8', pygame.image.load("images/white_king.png"))

board = [
    [rook1, knight1, bishop1, queen, king, bishop2, knight2, rook2],
    [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [computerpawn1, computerpawn2, computerpawn3, computerpawn4, computerpawn5, computerpawn6, computerpawn7,
     computerpawn8],
    [computerrook1, computerknight1, computerbishop1, computerqueen, computerking, computerbishop2, computerknight2,
     computerrook2]
]

computerpieces = [computerpawn1, computerpawn2, computerpawn3, computerpawn4, computerpawn5, computerpawn6, computerpawn7,
                  computerpawn8, computerrook1, computerknight1, computerbishop1, computerqueen, computerking, computerbishop2,
                  computerknight2, computerrook2]
playerpieces = [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8, rook1, knight1, bishop1, queen, king, bishop2,
                knight2, rook2]

logo = pygame.image.load("images/white_knight.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("chess v0.5")
pygame.init()
screen = pygame.display.set_mode((400, 400))
Board.printBoard(board, '', screen)
pygame.display.flip()
# define a variable to control the main loop
running = True
# define variable that checks if this is the first or second click
hightlighting = False
# keeps track if it is the player or computer's turn
whosemove = 1
# main loop
while running:
    # event handling, gets all event from the event queue
    if whosemove % 2 == 0:
        for event in pygame.event.get():
            # capture mouse button event
            if event.type == pygame.MOUSEBUTTONUP:
                # this is the second click code
                if hightlighting == True:
                    pos = pygame.mouse.get_pos()
                    destinationPiece = Board.getClickedPiece(board, pos)
                    destination = Board.convertToGrid(pos)
                    # if there exists an enemy piece at the destination and the move is good
                    if isinstance(destinationPiece, Classes.Piece):
                        if destinationPiece.player != playerColor and destination in moveList:
                            # move piece
                            targetPiece.pos = destinationPiece.pos
                            # delete destination piece
                            for x in playerpieces:
                                if x.pos == destinationPiece.pos:
                                    del x
                                    #print(computerpieces)
                            destinationPiece.player = 'none'
                            board = Board.fixGrid(board)
                            Board.printBoard(board, moveList, screen)
                            pygame.display.flip()
                            hightlighting = False
                            targetPiece.numberOfmoves +=1
                            whosemove += 1
                    # if there is not a piece at the estination and the move is good
                    if not destinationPiece and destination in moveList:
                        targetPiece.pos = destination
                        moveList = ''
                        board = Board.fixGrid(board)
                        Board.printBoard(board, moveList, screen)
                        pygame.display.flip()
                        hightlighting = False
                        targetPiece.numberOfmoves += 1
                        whosemove += 1
                    # if the destination is not a vaild move
                    else:
                        moveList = ''
                        Board.printBoard(board, moveList, screen)
                        pygame.display.flip()
                        hightlighting = False
                # if this is the first click this move
                else:
                    pos = pygame.mouse.get_pos()
                    targetPiece = Board.getClickedPiece(board, pos)
                    if isinstance(targetPiece, Classes.Piece) and targetPiece.player == playerColor:
                        checkPlayer = playerInCheck(board, king.pos)
                        if checkPlayer!= False:
                            kingMoves = king.moves(board)
                            safeKingMoves = removeCheck(board, kingMoves, checkPlayer)
                            if safeKingMoves == 'check mate':
                                moveList = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3]

                                print(moveList)
                            else:
                                moveList = safeKingMoves
                                print(moveList)
                        else:
                            moveList = targetPiece.moves(board)
                            print(moveList)
                    else:
                        moveList = ''
                    board = Board.fixGrid(board)
                    Board.printBoard(board, moveList, screen)
                    pygame.display.flip()
                    hightlighting = True
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    else:
        time.sleep(1)
        for x in computerpieces:
            if whosemove % 2 == 0:
                break
            for y in playerpieces:
                if whosemove % 2 == 0:
                    break
                for z in x.moves(board):
                    if whosemove % 2 == 0:
                        break
                    if z == y.pos:
                        if whosemove % 2 == 0:
                            break
                        x.pos = y.pos
                        whosemove += 1
                        moveList = ''
                        board = Board.fixGrid(board)
                        Board.printBoard(board, moveList, screen)
                        pygame.display.flip()

        if whosemove % 2 != 0:
            compMoveList = []
            computerpieces = Board.getComputerPieces(board)
            while compMoveList == []:
                randnum = randint(1, len(computerpieces))
                randnum -= 1
                #print(randnum)
                #print(computerpieces[randnum])
                #compMoveList = computerpawn1.moves(board)
                compMoveList = computerpieces[randnum].moves(board)
            randnum2 = randint(1, len(compMoveList))
            randnum2 -= 1
            newCompPosition = compMoveList[randnum2]
            #computerpawn1.pos = newCompPosition
            for row in board:
                for piece in row:
                    if isinstance(piece, Classes.Piece) and piece.pos == newCompPosition:
                        piece.player = 'none'
            computerpieces[randnum].pos = newCompPosition
            computerpieces[randnum].numberOfmoves += 1
            #print(newCompPosition)
            #print(compMoveList)
            moveList = ''
            board = Board.fixGrid(board)

            checkComputer = playerInCheck(board, computerking.pos)
            if checkComputer != False:
                kingMoves = computerking.moves(board)
                safeKingMoves = removeCheck(board, kingMoves, checkComputer)
                if safeKingMoves == "check mate":
                    moveList = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6]
                    print(moveList)
                else:
                    moveList = []
                    moveList.append(safeKingMoves)
                    print(moveList)

            Board.printBoard(board, moveList, screen)
            pygame.display.flip()
            # if randint == 2:
            whosemove += 1


import pygame
import Classes

def printBoard( board, highlights, screen):
    brown_square = pygame.image.load("images/brown_square.png")
    white_square = pygame.image.load("images/white_square.png")
    cyan_square = pygame.image.load("images/cyan_square.png")
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                screen.blit(white_square, (j*100+50, i*50))
            else:
                screen.blit(white_square, (j*100, i*50))
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                screen.blit(brown_square, (j*100, i*50))
            else:
                screen.blit(brown_square, (j*100+50, i*50))
    if highlights != (''):
        for tile in highlights:
            screen.blit(cyan_square,convertToPixels(tile))
    for row in board:
        for piece in row:
            if isinstance(piece,Classes.Piece):
                screen.blit(piece.image, convertToPixels(piece.pos))


def fixGrid(board):
    outBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    board = pawnPromotion(board)
    for row in board:
        for piece in row:
            column = ''
            row = ''
            if isinstance(piece, Classes.Piece) and piece.player != 'none':
                if piece.pos[0] == 'a':
                    column = 0
                if piece.pos[0] == 'b':
                    column = 1
                if piece.pos[0] == 'c':
                    column = 2
                if piece.pos[0] == 'd':
                    column = 3
                if piece.pos[0] == 'e':
                    column = 4
                if piece.pos[0] == 'f':
                    column = 5
                if piece.pos[0] == 'g':
                    column = 6
                if piece.pos[0] == 'h':
                    column = 7
                if piece.pos[1] == '1':
                    row = 0
                if piece.pos[1] == '2':
                    row = 1
                if piece.pos[1] == '3':
                    row = 2
                if piece.pos[1] == '4':
                    row = 3
                if piece.pos[1] == '5':
                    row = 4
                if piece.pos[1] == '6':
                    row = 5
                if piece.pos[1] == '7':
                    row = 6
                if piece.pos[1] == '8':
                    row = 7
                outBoard[row][column]= piece
    return outBoard

def convertToPixels(pos):
    column = ''
    row = ''
    if pos[0] == 'a':
        column = 0
    if pos[0] == 'b':
        column = 50
    if pos[0] == 'c':
        column = 100
    if pos[0] == 'd':
        column = 150
    if pos[0] == 'e':
        column = 200
    if pos[0] == 'f':
        column = 250
    if pos[0] == 'g':
        column = 300
    if pos[0] == 'h':
        column = 350
    if pos[1] == '1':
        row = 350
    if pos[1] == '2':
        row = 300
    if pos[1] == '3':
        row = 250
    if pos[1] == '4':
        row = 200
    if pos[1] == '5':
        row = 150
    if pos[1] == '6':
        row = 100
    if pos[1] == '7':
        row = 50
    if pos[1] == '8':
        row = 0
    return [column,row]

def convertToGrid(pos):
    grid = ''
    if 0 < pos[0] < 50:
        grid += 'a'
    if 50 < pos[0] <= 100:
        grid += 'b'
    if 100 < pos[0] <= 150:
        grid += 'c'
    if 150 < pos[0] <= 200:
        grid += 'd'
    if 200 < pos[0] <= 250:
        grid += 'e'
    if 250 < pos[0] <= 300:
        grid += 'f'
    if 300 < pos[0] <= 350:
        grid += 'g'
    if 350 < pos[0] <= 400:
        grid += 'h'
    if 0 < pos[1] < 50:
        grid += '8'
    if 50 < pos[1] <= 100:
        grid += '7'
    if 100 < pos[1] <= 150:
        grid += '6'
    if 150 < pos[1] <= 200:
        grid += '5'
    if 200 < pos[1] <= 250:
        grid += '4'
    if 250 < pos[1] <= 300:
        grid += '3'
    if 300 < pos[1] <= 350:
        grid += '2'
    if 350 < pos[1] <= 400:
        grid += '1'
    return grid

def getClickedPiece(board, pos):
    for row in board:
        for piece in row:
            if isinstance(piece,Classes.Piece) and piece.pos == convertToGrid(pos):
                return piece

def getComputerPieces(board):
    computerPieces = []
    for row in board:
        for piece in row:
            if isinstance(piece,Classes.Piece) and piece.player == 'white':
                computerPieces.append(piece)
    return computerPieces



def pawnPromotion(board):
    i = 0
    for piece in board[0]:
        if isinstance(piece, Classes.Piece) and piece.value == 1:
            newQueen = Classes.Queen('white', piece.pos, pygame.image.load("images/white_queen.png"))
            piece.player = 'none'
            board[0][i] = newQueen
        i += 1
    j = 0
    for piece in board[7]:
        if isinstance(piece, Classes.Piece) and piece.value == 1:
            newQueen = Classes.Queen('black', piece.pos, pygame.image.load("images/black_queen.png"))
            piece.player = 'none'
            board[7][j] = newQueen
        j += 1
    return board

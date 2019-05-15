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
            if isinstance(piece,Classes.Piece) and piece.color != 'none':
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

    for row in board:
        for piece in row:
            column = ''
            row = ''
            if isinstance(piece, Classes.Piece) and piece.color != 'none':
                if piece.pos[0] == 'a':
                    column = 7
                if piece.pos[0] == 'b':
                    column = 6
                if piece.pos[0] == 'c':
                    column = 5
                if piece.pos[0] == 'd':
                    column = 4
                if piece.pos[0] == 'e':
                    column = 3
                if piece.pos[0] == 'f':
                    column = 2
                if piece.pos[0] == 'g':
                    column = 1
                if piece.pos[0] == 'h':
                    column = 0
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


def loadImages():
    # load images and set the logo
    logo = pygame.image.load("images/brown_square.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("chess v0.1")

    black_king = pygame.image.load("images/black_king.png")
    black_queen = pygame.image.load("images/black_queen.png")
    black_bishop = pygame.image.load("images/black_bishop.png")
    black_knight = pygame.image.load("images/black_knight.png")
    black_rook = pygame.image.load("images/black_rook.png")
    black_pawn = pygame.image.load("images/black_pawn.png")
    white_king = pygame.image.load("images/white_king.png")
    white_queen = pygame.image.load("images/white_queen.png")
    white_bishop = pygame.image.load("images/white_bishop.png")
    white_knight = pygame.image.load("images/white_knight.png")
    white_rook = pygame.image.load("images/white_rook.png")
    white_pawn = pygame.image.load("images/white_pawn.png")

# define a main function
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
def main():
    # initialize the pygame module
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    '''
    bK = Classes.King(0, 10, 'king', [200, 0], pygame.image.load("images/black_king.png"))
    bQ = Piece(0, 10, 'queen', [150, 0], pygame.image.load("images/black_queen.png"))
    bB1=Piece(0, 10, 'bishop', [100, 0],pygame.image.load("images/black_bishop.png"))
    bB2=Piece(0, 10, 'bishop', [250, 0],pygame.image.load("images/black_bishop.png"))
    bKn1=Piece(0, 10, 'knight', [300, 0], pygame.image.load("images/black_knight.png"))
    bKn2=Piece(0, 10, 'knight', [50, 0], pygame.image.load("images/black_knight.png"))
    bR1=Piece(0, 10, 'rook', [0, 0], pygame.image.load("images/black_rook.png"))
    bR2=Piece(0, 10, 'rook', [350, 0],pygame.image.load("images/black_rook.png"))
    bP1=Piece(0, 10, 'pawn', [0, 50], pygame.image.load("images/black_pawn.png"))
    
    bP1 = Classes.Pawn('black',[0, 50])
    bP2 = Classes.Pawn('black',[50, 50])
    bP3 = Classes.Pawn('black',[100, 50])
    bP4 = Classes.Pawn('black',[150, 50])
    bP5 = Classes.Pawn('black',[200, 50])
    bP6 = Classes.Pawn('black',[250, 50])
    bP7 = Classes.Pawn('black',[300, 50])
    bP8 = Classes.Pawn('black',[350, 50])
    
    bP1 = Classes.Pawn('black', 'A7')
    bP2 = Classes.Pawn('black', 'B7')
    bP3 = Classes.Pawn('black', 'C7')
    bP4 = Classes.Pawn('black', 'D7')
    bP5 = Classes.Pawn('black', 'E7')
    bP6 = Classes.Pawn('black', 'F7')
    bP7 = Classes.Pawn('black', 'G7')
    bP8 = Classes.Pawn('black', 'H7')
    '''
    pawn1 = Classes.Pawn('black', '2a')
    pawn2 = Classes.Pawn('black', '2b')
    pawn3 = Classes.Pawn('black', '2c')
    pawn4 = Classes.Pawn('black', '2d')
    pawn5 = Classes.Pawn('black', '2e')
    pawn6 = Classes.Pawn('black', '2f')
    pawn7 = Classes.Pawn('black', '2g')
    pawn8 = Classes.Pawn('black', '2h')
    rook1 = Classes.Rook('black', '1a')
    rook2 = Classes.Rook('black', '1h')
    knight1 = Classes.Knight('black', '1b')
    knight2 = Classes.Knight('black', '1g')
    bishop1 = Classes.Bishop('black', '1c')
    bishop2 = Classes.Bishop('black', '1f')
    queen = Classes.Queen('black', '1d')
    king = Classes.King('black', '1e')
    computerpawn1 = Classes.Pawn('white', '7a')
    computerpawn2 = Classes.Pawn('white', '7b')
    computerpawn3 = Classes.Pawn('white', '7c')
    computerpawn4 = Classes.Pawn('white', '7d')
    computerpawn5 = Classes.Pawn('white', '7e')
    computerpawn6 = Classes.Pawn('white', '7f')
    computerpawn7 = Classes.Pawn('white', '7g')
    computerpawn8 = Classes.Pawn('white', '7h')
    computerrook1 = Classes.Rook('white', '8a')
    computerrook2 = Classes.Rook('white', '8h')
    computerknight1 = Classes.Knight('white', '8b')
    computerknight2 = Classes.Knight('white', '8g')
    computerbishop1 = Classes.Bishop('white', '8c')
    computerbishop2 = Classes.Bishop('white', '8f')
    computerqueen = Classes.Queen('white', '8d')
    computerking = Classes.King('white', '8e')

    board = [[computerrook1, computerknight1, computerbishop1, computerqueen, computerking,computerbishop2, computerknight2,computerrook2],
             [computerpawn1, computerpawn2, computerpawn3, computerpawn4, computerpawn5, computerpawn6, computerpawn7, computerpawn8],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8],
             [rook1, knight1, bishop1, queen, king, bishop2, knight2, rook2]]

    printBoard(board, '', screen)
    pygame.display.flip()
    '''
    screen.blit(black_rook, (0, 0))
    screen.blit(black_knight, (50, 0))
    screen.blit(black_bishop, (100, 0))
    screen.blit(black_queen, (150, 0))
    screen.blit(black_king, (200, 0))
    screen.blit(black_bishop, (250, 0))
    screen.blit(black_knight, (300, 0))
    screen.blit(black_rook, (350, 0))
    for i in range(8):
        screen.blit(black_pawn, (i*50, 50))

    screen.blit(white_rook, (0, 350))
    screen.blit(white_knight, (50, 350))
    screen.blit(white_bishop, (100, 350))
    screen.blit(white_queen, (150, 350))
    screen.blit(white_king, (200, 350))
    screen.blit(white_bishop, (250, 350))
    screen.blit(white_knight, (300, 350))
    screen.blit(white_rook, (350, 350))
    for i in range(8):
        screen.blit(white_pawn, (i * 50, 300))


    pygame.display.flip()
    '''

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                if hightlighting:
                    pos = pygame.mouse.get_pos()
                    destinationPiece = getClickedPiece(board, pos)
                    if destinationPiece and destinationPiece.player != 'black':
                        targetPiece.pos = destinationPiece.pos
                        ## fix grid
                else:
                    pos = pygame.mouse.get_pos()
                    targetPiece = getClickedPiece(board, pos)
                    # moveList = targetPiece.moves()
                    moveList = ['a1']
                    printBoard(board, moveList, screen)
                    pygame.display.flip()
                    hightlighting = true
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
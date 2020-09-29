import pygame
from sys import exit
from DataStructures import Queue, Stack
from Position import Position

pygame.init()
pygame.font.init()

# 40x40 grid, each box in grid is 15x15 pixels
screen = pygame.display.set_mode((600, 600))
myfont = pygame.font.SysFont('Times New Roman', 30)

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (16, 75, 238)

board = []


def options():
    running = True
    bf_button = pygame.Rect(50, 50, 200, 100)
    df_button = pygame.Rect(350, 50, 200, 100)
    aS_button = pygame.Rect(50, 200, 200, 100)
    while running:
        screen.fill(BLACK)

        screen.fill(WHITE, bf_button)
        text = myfont.render("Breadth-first", True, BLACK)
        screen.blit(text, (60, 60))

        screen.fill(WHITE, df_button)
        text = myfont.render("Depth-first", True, BLACK)
        screen.blit(text, (360, 60))

        screen.fill(WHITE, aS_button)
        text = myfont.render("A star", True, BLACK)
        screen.blit(text, (60, 210))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mX, mY = pygame.mouse.get_pos()
                if bf_button.collidepoint((mX, mY)):
                    return "BF"
                elif df_button.collidepoint((mX, mY)):
                    return "DF"
                elif aS_button.collidepoint((mX, mY)):
                    return "A*"

        clock.tick(60)
        pygame.display.update()


def showQueue(curr, queue):
    screen.fill(BLACK)

    for row in range(40):
        for col in range(40):
            pygame.draw.rect(screen, WHITE,
                             (row * 15, col * 15, 15, 15), 1)
            if board[row][col] == "#":
                screen.fill(WHITE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "S":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "F":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "c":
                screen.fill((255, 0, 0), (row * 15, col * 15, 15, 15))

    if board[curr.getRow()][curr.getCol()] not in ["S", "F"]:
        board[curr.getRow()][curr.getCol()] = "c"
        screen.fill((255, 0, 0), (curr.getRow() *
                                  15, curr.getCol() * 15, 15, 15))

    traverseNode = queue.getFront()
    while traverseNode != None:
        screen.fill((0, 255, 0), (traverseNode.getData().getRow()
                                  * 15, traverseNode.getData().getCol() * 15, 15, 15))
        traverseNode = traverseNode.getNext()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    pygame.time.delay(5)


def showStack(curr, stack):
    screen.fill(BLACK)

    for row in range(40):
        for col in range(40):
            pygame.draw.rect(screen, WHITE,
                             (row * 15, col * 15, 15, 15), 1)
            if board[row][col] == "#":
                screen.fill(WHITE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "S":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "F":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "c":
                screen.fill((255, 0, 0), (row * 15, col * 15, 15, 15))

    if board[curr.getRow()][curr.getCol()] not in ["S", "F"]:
        board[curr.getRow()][curr.getCol()] = "c"
        screen.fill((255, 0, 0), (curr.getRow() *
                                  15, curr.getCol() * 15, 15, 15))

    traverseNode = stack.getTop()
    while traverseNode != None:
        screen.fill((0, 255, 0), (traverseNode.getData().getRow()
                                  * 15, traverseNode.getData().getCol() * 15, 15, 15))
        traverseNode = traverseNode.getNext()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    pygame.time.delay(5)


def showAStar(currNode, availNodes):
    screen.fill(BLACK)

    for row in range(40):
        for col in range(40):
            pygame.draw.rect(screen, WHITE,
                             (row * 15, col * 15, 15, 15), 1)
            if board[row][col] == "#":
                screen.fill(WHITE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "S":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "F":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "c":
                screen.fill((255, 0, 0), (row * 15, col * 15, 15, 15))

    if board[currNode.getRow()][currNode.getCol()] not in ["S", "F"]:
        board[currNode.getRow()][currNode.getCol()] = "c"
        screen.fill((255, 0, 0), (currNode.getRow() *
                                  15, currNode.getCol() * 15, 15, 15))

    for node in availNodes:
        if board[node.getRow()][node.getCol()] not in ["c", "S", "F"]:
            screen.fill((0, 255, 0), (node.getRow()
                                      * 15, node.getCol() * 15, 15, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    pygame.time.delay(5)


def showPath(stack):
    screen.fill(BLACK)

    for row in range(40):
        for col in range(40):
            pygame.draw.rect(screen, WHITE,
                             (row * 15, col * 15, 15, 15), 1)
            if board[row][col] == "#":
                screen.fill(WHITE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "S":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "F":
                screen.fill(BLUE, (row * 15, col * 15, 15, 15))
            elif board[row][col] == "c":
                screen.fill((255, 0, 0), (row * 15, col * 15, 15, 15))

    while not stack.isEmpty():
        node = stack.pop()
        node = node.getData()
        screen.fill(BLUE, (node.getRow() *
                           15, node.getCol() * 15, 15, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    pygame.time.delay(1400)


def main():
    global board
    board = [["" for y in range(40)] for x in range(40)]
    startMade = False
    finishMade = False
    wall = False
    click = False
    running = True
    mX, mY = 0, 0
    sX, sY = 0, 0
    fX, fY = 0, 0
    while running:
        screen.fill(BLACK)

        for row in range(40):
            for col in range(40):
                pygame.draw.rect(screen, WHITE,
                                 (row * 15, col * 15, 15, 15), 1)
                if board[row][col] == "#":
                    screen.fill(WHITE, (row * 15, col * 15, 15, 15))

        if startMade:
            screen.fill(BLUE, ((sX//15) *
                               15, (sY//15) * 15, 15, 15))

        if finishMade:
            screen.fill(BLUE, ((fX//15) *
                               15, (fY//15) * 15, 15, 15))

        if wall:
            mX, mY = pygame.mouse.get_pos()
            board[mX//15][mY//15] = "#"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mX, mY = pygame.mouse.get_pos()
                    if not startMade:
                        sX, sY = mX, mY
                        startMade = True
                        board[sX//15][sY//15] = "S"
                    elif not finishMade:
                        fX, fY = mX, mY
                        finishMade = True
                        board[fX//15][fY//15] = "F"
                    else:
                        wall = True
            if event.type == pygame.MOUSEBUTTONUP and wall:
                wall = False

        clock.tick(60)
        pygame.display.update()

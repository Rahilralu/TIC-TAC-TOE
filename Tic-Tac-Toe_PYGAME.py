import pygame


current_player = "X"

def Tic(fs, font):
    mousex, mousey = pygame.mouse.get_pos()
    gridx = mousex // 100
    gridy = mousey // 100

    if board[gridy][gridx] == " ":
        t = font.render(f"{fs}", True, (255,0, 0))
        cell_center_x = gridx * 100 + 50
        cell_center_y = gridy * 100 + 50

        screen.blit(t, (cell_center_x - t.get_width() // 2, cell_center_y - t.get_height() // 2))
        board[gridy][gridx] = fs

        if win(fs):
            print(f"Player {fs} wins!")
            return "win"
        elif is_draw():
            print("It's a draw!")
            return "draw"
        return True
    return False

def win(fs):
    winning_combinations = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    for combo in winning_combinations:
        if all(board[row][col] == fs for row, col in combo):
            return True
    return False

def is_draw():
    return all(board[row][col] != " " for row in range(3) for col in range(3))


pygame.init()


screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TIC - TAC - TOE")
screen.fill((255, 255, 255))


cell_size = 100
board = [[" " for _ in range(3)] for _ in range(3)]
font = pygame.font.Font(None, 100)
running = True


for i in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (300, i * cell_size), 3)
    pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, 300), 3)

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        
                result = Tic(current_player, font)
                if result == "win" or result == "draw":
                    running = False
                elif result:
                    current_player = "O" if current_player == "X" else "X"

        
                pygame.display.update()

pygame.quit()
import pygame
import sys

# Inicializando o pygame
pygame.init()

# Dimensões da janela
WIDTH, HEIGHT = 800, 600

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola e das paletas
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
BALL_SPEED_X = 8
BALL_SPEED_Y = 8

# Criando a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Função principal do jogo
def pong_game(mode):
    clock = pygame.time.Clock()

    # Posicionamento inicial
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

    left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
    right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2

    left_score, right_score = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimento das paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle_y > 0:
            left_paddle_y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
            left_paddle_y += PADDLE_SPEED

        if mode == "player":
            if keys[pygame.K_UP] and right_paddle_y > 0:
                right_paddle_y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
                right_paddle_y += PADDLE_SPEED
        elif mode == "ai":
            if ball_y < right_paddle_y + PADDLE_HEIGHT // 2 and right_paddle_y > 0:
                right_paddle_y -= PADDLE_SPEED
            if ball_y > right_paddle_y + PADDLE_HEIGHT // 2 and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
                right_paddle_y += PADDLE_SPEED

        # Movimento da bola
        ball_x += ball_dx
        ball_y += ball_dy

        # Colisão com as bordas superiores e inferiores
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
            ball_dy *= -1

        # Colisão com as paletas
        if (ball_x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT):
            ball_dx *= -1
        if (ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT):
            ball_dx *= -1

        # Verificação de ponto
        if ball_x < 0:
            right_score += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx *= -1

        if ball_x > WIDTH:
            left_score += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_dx *= -1

        # Desenho dos elementos
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

        # Exibição do placar
        font = pygame.font.Font(None, 74)
        text = font.render(str(left_score), True, WHITE)
        screen.blit(text, (WIDTH // 4, 10))
        text = font.render(str(right_score), True, WHITE)
        screen.blit(text, (WIDTH * 3 // 4, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Menu inicial
def main():
    while True:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Pong Game", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        text = font.render("Tecle 1 para jogar contra outro jogador", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 20))

        text = font.render("Tecle 2 para jogar contra a máquina", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pong_game("player")
                if event.key == pygame.K_2:
                    pong_game("ai")

# Executa o programa
if __name__ == "__main__":
    main()

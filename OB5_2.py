import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 300, 600  # Размеры окна (10x20 клеток)
CELL_SIZE = 30  # Размер одной клетки
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE  # Размеры поля в клетках

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Голубой (I)
    (0, 0, 255),    # Синий (J)
    (255, 165, 0),  # Оранжевый (L)
    (255, 255, 0),  # Желтый (O)
    (0, 255, 0),    # Зеленый (S)
    (128, 0, 128),  # Фиолетовый (T)
    (255, 0, 0)     # Красный (Z)
]

# Фигуры тетриса (матрицы 4x4)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Класс фигуры
class Tetromino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(SHAPES)  # Выбираем случайную фигуру
        self.color = random.choice(COLORS)  # Цвет фигуры

    def rotate(self):
        """Поворот фигуры"""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# Класс игрового поля
class Tetris:
    def __init__(self):
        self.grid = [[BLACK] * COLS for _ in range(ROWS)]  # Игровое поле
        self.tetromino = Tetromino(COLS // 2 - 1, 0)  # Новая фигура
        self.score = 0
        self.game_over = False

    def is_valid(self, shape, x, y):
        """Проверка на выход за границы и на пересечение"""
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]:
                    if x + j < 0 or x + j >= COLS or y + i >= ROWS:
                        return False
                    if y + i >= 0 and self.grid[y + i][x + j] != BLACK:
                        return False
        return True

    def place_tetromino(self):
        """Закрепляем фигуру на поле"""
        for i in range(len(self.tetromino.shape)):
            for j in range(len(self.tetromino.shape[i])):
                if self.tetromino.shape[i][j]:
                    self.grid[self.tetromino.y + i][self.tetromino.x + j] = self.tetromino.color
        self.clear_lines()
        self.tetromino = Tetromino(COLS // 2 - 1, 0)  # Новая фигура
        if not self.is_valid(self.tetromino.shape, self.tetromino.x, self.tetromino.y):
            self.game_over = True  # Игра окончена

    def clear_lines(self):
        """Удаление заполненных линий"""
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        cleared = ROWS - len(new_grid)  # Количество убранных линий
        self.grid = [[BLACK] * COLS for _ in range(cleared)] + new_grid
        self.score += cleared * 100  # Начисляем очки

    def move(self, dx, dy):
        """Двигаем фигуру"""
        if self.is_valid(self.tetromino.shape, self.tetromino.x + dx, self.tetromino.y + dy):
            self.tetromino.x += dx
            self.tetromino.y += dy
        elif dy:  # Если уперлись вниз – зафиксировать фигуру
            self.place_tetromino()

    def rotate(self):
        """Поворот фигуры"""
        rotated_shape = [list(row) for row in zip(*self.tetromino.shape[::-1])]
        if self.is_valid(rotated_shape, self.tetromino.x, self.tetromino.y):
            self.tetromino.shape = rotated_shape

    def draw(self, screen):
        """Отрисовка экрана"""
        screen.fill(BLACK)
        for y in range(ROWS):
            for x in range(COLS):
                pygame.draw.rect(screen, self.grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
                pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        # Рисуем текущую фигуру
        for i in range(len(self.tetromino.shape)):
            for j in range(len(self.tetromino.shape[i])):
                if self.tetromino.shape[i][j]:
                    pygame.draw.rect(screen, self.tetromino.color,
                                     ((self.tetromino.x + j) * CELL_SIZE,
                                      (self.tetromino.y + i) * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE), 0)

        # Отображение счета
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

# Запуск игры
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Тетрис")

    clock = pygame.time.Clock()
    game = Tetris()

    fall_time = 0
    speed = 500  # Интервал падения (мс)

    running = True
    while running:
        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()

        fall_time += clock.get_rawtime()
        clock.tick(30)

        if fall_time >= speed:
            game.move(0, 1)
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

        if game.game_over:
            print("Game Over! Your score:", game.score)
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()

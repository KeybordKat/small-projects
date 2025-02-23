# Required libraries
import random
import pygame
import sys

# Key variables
snake_speed = 15
window_x = 480
window_y = 360
score = 0

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
pink = pygame.Color(255, 126, 226)
peach = pygame.Color(255, 163, 143)
orange = pygame.Color(255, 209, 142)

# Initialize pygame
pygame.init()
pygame.display.set_caption('Snake <3')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Set font for buttons and game text (All Magneto font)
font = pygame.font.SysFont('magneto', 30)  # Global font setting for buttons and text


# Function to create and handle buttons
def draw_button(text, x, y, width, height, normal_color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if mouse is over the button and change color on hover
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(game_window, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()  # Call the action associated with the button
    else:
        pygame.draw.rect(game_window, normal_color, (x, y, width, height))

    # Display the button text using Magneto font
    button_text = font.render(text, True, white)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    game_window.blit(button_text, text_rect)


# Function to show score
def show_score(choice, color, font_name, size):
    score_font = pygame.font.SysFont('magneto', size)  # Magneto font for score
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# Function to handle quitting
def quit_game():
    pygame.quit()
    sys.exit()


# Function for game over
def game_over():
    my_font = pygame.font.SysFont('magneto', 40)  # Magneto font for game over text
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, orange)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Call play again screen immediately
    play_again()


# Play again screen
def play_again():
    while True:
        game_window.fill(black)

        # Draw "Play Again" and "Quit" buttons
        draw_button("Play Again", window_x // 2 - 150, window_y // 2 - 50, 300, 50, pink, peach, run_game)
        draw_button("Quit", window_x // 2 - 150, window_y // 2 + 50, 300, 50, pink, peach, quit_game)

        pygame.display.flip()

        # Handle basic quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()


# Main function
def run_game():
    global score  # Allow score to be modified inside this function
    score = 0  # Reset the score at the start of each new game

    # Start the snake closer to the center of the screen
    snake_position = [window_x // 2, window_y // 2]
    snake_body = [[window_x // 2, window_y // 2],
                  [window_x // 2 - 10, window_y // 2],
                  [window_x // 2 - 20, window_y // 2]]

    # Place the first fruit at a random position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Update the direction
        direction = change_to

        # Move the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake growing mechanism: When it eats the fruit
        snake_body.insert(0, list(snake_position))
        if snake_position == fruit_position:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

        # Fill the game window with the background color
        game_window.fill(black)

        # Draw the snake
        for pos in snake_body:
            pygame.draw.rect(game_window, peach, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw the fruit
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        # Game over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10 or \
                snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Check if the snake hits itself
        for block in snake_body[1:]:
            if snake_position == block:
                game_over()

        # Show score using Magneto font
        show_score(1, pink, 'magneto', 20)

        # Refresh the display
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        fps.tick(snake_speed)


run_game()

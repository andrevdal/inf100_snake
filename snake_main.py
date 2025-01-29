from snake_view import draw_board
import random

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.state = "start"
    app.direction = "east"
    app.info_mode = False
    app.difficulity = ""
    app.snake_size = 3
    app.timer_delay = 150

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if not app.info_mode and app.state == "active":
        move_snake(app)

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if event.key == "i":
        app.info_mode = bool( not app.info_mode)
    if app.state == "start":
        if event.key == "e":
            app.difficulity = "easy"
            app.head_pos = (3,4)
            app.board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
                [0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
            app.board_length = len(app.board[0])
            app.board_height = len(app.board)
        if event.key == "n":
            app.difficulity = "normal"
            app.head_pos = (3,4)
            app.board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0,-1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, -1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
            app.board_height = len(app.board)
            app.board_length = len(app.board[0])
        if event.key == "h":
            app.difficulity = "hard"
            app.board = [
                [2, 3, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, -1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
            app.head_pos = (0,1)
            app.board_height = len(app.board)
            app.board_length = len(app.board[0])
    if event.key == "Enter":
        if app.state == "gameover" or app.state == "win":
            app_started(app)
        elif app.state == "start" and not app.difficulity == "":
            app_started(app)
            app.state = "active"
    if app.state == "active":
        if event.key == "Up":
            app.direction = "north"
        if event.key == "Right":
            app.direction = "east"
        if event.key == "Down":
            app.direction = "south"
        if event.key == "Left":
            app.direction = "west"
        if event.key == "Space":
            move_snake(app)

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    if app.state == "win":
        canvas.create_text(app.width/2, app.height/2, text = "Congratulations you won!", font=('Times', 30, 'italic bold'), fill="green")
        canvas.create_text(app.width/2, app.height/2 + 30, text = 'Press "enter" to restart game')
    elif app.state == "start":
        colore = "black"
        colorn = "black"
        colorh = "black"
        if app.difficulity == "easy":
            colore = "red"
        if app.difficulity == "normal":
            colorn = "red"
        if app.difficulity == "hard":
            colorh = "red"
        canvas.create_text(app.width/2, 2 * app.height/5, text = "Snake", font=('Times', 30, 'italic bold'), fill="green")
        canvas.create_text(app.width/2, app.height/2, text = "Please select diffuculity, then press enter")
        canvas.create_text(app.width/4, 3 * app.height/5, text = '(Press "e" for easy)', fill = colore)
        canvas.create_text(2 * app.width/4, 3 * app.height/5, text = '(Press "n" for normal)', fill = colorn)
        canvas.create_text(3 * app.width/4, 3 * app.height/5, text = '(Press "h" for hard)', fill = colorh)
    elif app.state == "gameover":
        canvas.create_text(app.width/2, app.height/2, text = "Game Over!", font=('Times', 30, 'italic bold'), fill="red")
        canvas.create_text(app.width/2, app.height/2 + 30, text = f"score: {app.snake_size}")
        canvas.create_text(app.width/2, app.height/2 + 60, text = 'Press "enter" to restart game')
    else:
        if app.info_mode == True:
            canvas.create_text(app.width/4, 10, text = f"head pos = {app.head_pos}")
            canvas.create_text(app.width / 2, 10, text = f"snake size = {app.snake_size}")
            canvas.create_text(3 * app.width / 4, 10, text = f"direction = {app.direction}")
            canvas. create_text(app.width/2, app.height - 15, text = 'game started in info mode. Press "i" for regular mode.')
        draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.info_mode)

def move_snake(app):
    y, x = app.head_pos
    if app.direction == "north":
        y = y - 1
    if app.direction == "east":
        x = x + 1
    if app.direction == "south":
        y = y + 1
    if app.direction == "west":
        x = x - 1
    app.head_pos = y, x

    if not is_legal_move(app.head_pos, app.board):
        app.state = "gameover"
        return

    if app.board[y][x] == -1:
        app.snake_size = app.snake_size + 1
        app.board[y][x] = app.snake_size
        if app.snake_size == len(app.board)*len(app.board[0]):
            app.state = "win"
            return
        add_apple_at_random_location(app.board)
    else:
        for y1 in range(app.board_height):
            for x1 in range(app.board_length):
                if app.board[y1][x1] > 0:
                    app.board[y1][x1] = app.board[y1][x1] -1
        app.board[y][x] = app.snake_size

def add_apple_at_random_location(grid):
    random_y = random.choice(range(len(grid)))
    random_x = random.choice(range(len(grid[0])))
    if grid[random_y][random_x] <= 0:
        grid[random_y][random_x] = -1
    else:
        add_apple_at_random_location(grid)

def is_legal_move(pos, board):
    y, x = pos
    if 0 > y or y > len(board)-1 or 0 > x or x > len(board[0])-1:
        return False
    elif board[y][x] > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=400, title='Snake')

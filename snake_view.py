def draw_board(canvas, x1, y1, x2, y2, board, info_mode):
    #Bruker egen kode fra lab4 opgpave: "colored_grid"
    rows = len(board)
    cols = len(board[0])
    width = abs((x1 - x2) / cols)
    height = abs((y1 - y2) / rows)

    for r in range(rows):
        for c in range(cols):
            color = "red"
            if board[r][c]== 0:
                color = "lightgray"
            if board[r][c]>0:
                color = "green"
            canvas.create_rectangle(
                x1 + width * c,
                y1 + height * r,
                x1 + width * (c + 1),
                y1 + height * (r + 1),
                fill = color
                )
            if info_mode:
                canvas.create_text(
                    x1 + width * c + width / 2,
                    y1 + height * r + height / 2 - 7,
                    text = f"{r},{c}"
                )
                canvas.create_text(
                    x1 + width * c + width / 2,
                    y1 + height * r + height / 2 + 7,
                    text = f"{board[r][c]}"
                )
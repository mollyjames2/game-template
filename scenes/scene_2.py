from engine.settings import BLACK, WHITE, WIDTH, HEIGHT, FONT_LARGE


async def run(screen, game_state, keys, event):
    screen.fill(BLACK)
    end_text = FONT_LARGE.render("End", True, WHITE)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))

def draw_wrapped_text(surface, text, font, color, x, y, max_width):
    words = text.split()
    line = ""
    lines = []
    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    for i, l in enumerate(lines):
        rendered = font.render(l, True, color)
        surface.blit(rendered, (x, y + i * font.get_linesize()))
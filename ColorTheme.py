BACKGROUND_COLOR = (255,243,224)
RED_COLOR = (250,119,109)
GREEN_THICK_COLOR = (0,77,64)
GREEN_THIN_COLOR = (178,255,89)
BLUE_THICK_COLOR = (63,81,181)
BLUE_THICK_COLOR = (63,81,181)
TEXT_COLOR = (56,56,62)

MARGIN = 15

def more_whiteish(base_color, delta):
    return tuple(min(x + delta, 255) for x in base_color)


def more_blackish(base_color, delta):
    return tuple(max(x - delta, 0) for x in base_color)


def invert_color(base_color):
    return tuple(255 - x for x in base_color)
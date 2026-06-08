from .Empty import Empty

class Entity:
    def __init__(self, x, y, current_lifaspan):
        self.is_alive = True
        self.x = x
        self.y = y
        self.current_lifaspan = current_lifaspan

    def handle_lifespan(self, matrix):
        if self.current_lifaspan == 0:
            matrix[self.y][self.x] = Empty(self.y, self.x)
            return False
        else:
            self.current_lifaspan -= 1











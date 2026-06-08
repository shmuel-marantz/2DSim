import random
from .Entity import Entity
from .utils import get_neighbors
from .Empty import Empty
from .Plant import Plant


class MobileEntity(Entity):
    def __init__(self, x, y, max_lifespan, current_lifaspan, food):
        super().__init__(x, y, current_lifaspan)
        self.max_lifespan = max_lifespan
        self.food = food

    def reproduce(self, matrix):
        if self.current_prevents_reproduction == 0:
            close_neighbors = get_neighbors(matrix, self.y, self.x)
            for neighbor in close_neighbors:
                if type(neighbor) is type(self) and neighbor.current_prevents_reproduction == 0:
                    for neighbor1 in close_neighbors:
                        if isinstance(neighbor1, Empty):
                            matrix[neighbor1.y][neighbor1.x] = type(self)(neighbor1.x, neighbor1.y)
                            self.current_prevents_reproduction = self.max_prevents_reproduction
                            neighbor.current_prevents_reproduction = neighbor.max_prevents_reproduction
                            return True
                    break
        return False

    def handle_movement(self, matrix):
        close_neighbors = get_neighbors(matrix, self.y, self.x)
        for neighbor in close_neighbors:
            if type(neighbor) in self.food:
                neighbor.is_alive = False
                self.current_lifaspan = self.max_lifespan
                matrix[self.y][self.x] = Empty(self.x, self.y)
                self.x, self.y = neighbor.x, neighbor.y
                matrix[self.y][self.x] = self
                return
        for neighbor in close_neighbors:
            if isinstance(neighbor, Empty) or isinstance(neighbor, Plant):
                neighbors_neighbor = get_neighbors(matrix, neighbor.y, neighbor.x)
                for neighbor1 in neighbors_neighbor:
                    if type(neighbor1) in self.food:
                        neighbor.is_alive = False
                        matrix[self.y][self.x] = Empty(self.x, self.y)
                        self.x, self.y = neighbor.x, neighbor.y
                        matrix[self.y][self.x] = self
                        return
        potential_targets = []
        for neighbor in close_neighbors:
            if isinstance(neighbor, Empty) or isinstance(neighbor, Plant):
                potential_targets.append(neighbor)
        if len(potential_targets) == 0:
            return
        random_target = potential_targets[random.randint(0, len(potential_targets) - 1)]
        random_target.is_alive = False
        matrix[self.y][self.x] = Empty(self.x, self.y)
        self.x, self.y = random_target.x, random_target.y
        matrix[self.y][self.x] = self

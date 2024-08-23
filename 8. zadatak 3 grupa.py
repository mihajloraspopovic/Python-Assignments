class Player:
    def __init__(self, x, y, width, height, health):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._health = health

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if 0 <= value <= 100:
            self._health = value


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._damage = damage

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if 0 <= value <= 100:
            self._damage = value


def check_collision(player, enemy):
    if (player.x < enemy.x + enemy.width and
        player.x + player.width > enemy.x and
        player.y < enemy.y + enemy.height and
        player.y + player.height > enemy.y):
        return True
    return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.health -= enemy.damage


player = Player(50, 50, 30, 30, 100)
enemy1 = Enemy(60, 60, 30, 30, 20)
enemy2 = Enemy(100, 100, 30, 30, 30)

decrease_health(player, enemy1)
decrease_health(player, enemy2)

print(f"Player health: {player.health}")

TITLE = "A Great Game"

WIDTH = 600

alien = Actor('alien')
alien.topright = 0, 10

HEIGHT = alien.height + 20

def update():
    alien.left += 2
    if alien.right >= WIDTH:
        alien.right = 0

def draw():
    screen.fill((128, 0, 0))
    alien.draw()
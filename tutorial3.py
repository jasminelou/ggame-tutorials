from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

green = Color(0x00ff00, 1)
blue = Color(0x2EFEF7, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, green)
bg = Sprite(bg_asset, (0,0))



ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))

ball.scale = 0.07
ball.y = 200

ball.dir = 0.76
ball.go = True

def reverse(b):
    b.dir *= -0.76
    pop.play()

def step():
    if ball.go:
        ball.x += ball.dir
        if ball.x + ball.width > SCREEN_WIDTH or ball.x < 0:
            ball.x -= ball.dir
            reverse(ball)

def spaceKey(event):
    ball.go = not ball.go

def reverseKey(event):
    reverse(ball)

def mouseClick(event):
    ball.x = event.x
    ball.y = event.y
    pew1.play()

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)

myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)

myapp.run(step)

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()

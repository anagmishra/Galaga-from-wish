import pgzrun
import pygame
import random
WIDTH=500
HEIGHT=500
spaceship=Actor("spaceship")
enemies=[]
bullet=[]
score=0
spaceship.pos=(250,HEIGHT-30)
for i in range(50):
    enemies.append(Actor("fly"))
    enemies[-1].x=random.randint(50, 450)
    enemies[-1].y=random.randint(0, 300)

def on_key_down(key):
    global spaceship
    if key==keys.SPACE:
        bullet.append(Actor("bullet"))
        bullet[-1].x=spaceship.x
        bullet[-1].y=spaceship.y-10


def draw():
    screen.fill("cyan")
    screen.draw.text("SCORE: " + str(score), (400, 50), color="lime")
    spaceship.draw()
    for j in enemies:
        j.draw()
    for i in bullet:
        i.draw()

def update():
    global score
    if keyboard.left:
        spaceship.x-=10
        if spaceship.x<=40:
            spaceship.x=40
    if keyboard.right:
        spaceship.x+=10
        if spaceship.x>=460:
            spaceship.x=460
    for i in bullet:
        if i.y<30:
            bullet.remove(i)
        else:
            i.y=i.y-10
    for j in enemies:
        j.y=j.y+1
        for k in bullet:
            if k.colliderect(j):
                score=score+1
                bullet.remove(k)
                enemies.remove(j)
    



pgzrun.go()
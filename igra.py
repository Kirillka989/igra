from pygame import*

scr = display.set_mode((700,500))
background = transform.scale(image.load("fon.png"), (700,500))
hero = transform.scale(image.load("ufo.png"), (200,150))
game = True
clock = time.Clock()
FPS = 60
x1=150
y1=150
while game:
    scr.blit(background,(0, 0))
    scr.blit(hero,(x1,y1))
    for e in event.get():
       if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_RIGHT]:
        x1 +=5
    if keys_pressed[K_LEFT]:
        x1 -=5
    if keys_pressed[K_DOWN]:
        y1 +=5
    if keys_pressed[K_UP]:
        y1 -=5





    display.update()
    clock.tick(FPS)








#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
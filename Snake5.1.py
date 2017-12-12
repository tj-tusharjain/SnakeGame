import pygame, time, random

name = raw_input("Enter your name: ")

pygame.init()

display_width = 800
display_height = 600

gamedisplay = pygame.display.set_mode((display_width,display_height)) 

pygame.display.update()

clock = pygame.time.Clock() 
snake_size = 20

apple_img = pygame.image.load('apple1.png')
bomb_img = pygame.image.load('bomb_img.png')
rotten_img = pygame.image.load('rotten_apple.png')
golden_img = pygame.image.load('ga.png')
bg = pygame.image.load('bg.jpeg')


font1 = pygame.font.SysFont("cooper black", 25)
font2 = pygame.font.SysFont("Comic Sans MS", 25)
font3 = pygame.font.SysFont("cooper black", 60)
font4 = pygame.font.SysFont("Calibri", 50)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill((0,0,0))
        p_text1 = font3.render("Paused ", True, (255,255,255))
        gamedisplay.blit(p_text1, [300,250])
        p_text2 = font2.render("Press C to continue or Q to quit", True, (255,255,255))
        gamedisplay.blit(p_text2, [220,400])
        pygame.display.update()
        clock.tick(5)
                    
def score(score):
    text = font2.render("Score: "+str(score), True, (255,255,255))
    gamedisplay.blit(text, [1,1])

def snake(snake_size,snake_height):
    for i in snake_height:
        pygame.draw.rect(gamedisplay, (0,150,0), [i[0],i[1],snake_size,snake_size])

f=open("highscore.txt","r")
a=f.readlines()
high_score1=int(a[0][0:-1])

f.close()
f=open("highscore.txt","r")
a=f.readlines()
high_scorer1=a[1][0:-1]
f.close()

f=open("highscore.txt","r")
a=f.readlines()
high_score2=int(a[2][0:-1])

f.close()
f=open("highscore.txt","r")
a=f.readlines()
high_scorer2=a[3][0:-1]
f.close()

f=open("highscore.txt","r")
a=f.readlines()
high_score3=int(a[4][0:-1])

f.close()
f=open("highscore.txt","r")
a=f.readlines()
high_scorer3=a[5]
f.close()


def gameloop():
    global high_score1, high_scorer1, high_score2, high_scorer2, high_score3, high_scorer3, name
    gameexit = False
    gameover = False

    x = 400
    y = 300
    block_size = 40
    x_change = 0
    y_change = -10

    snake_height = []
    snake_length = 3

    apple_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    apple_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
    

    bomb_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    bomb_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0

    rotten_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    rotten_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0

    golden_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    golden_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
    
    while not gameexit:
                
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        if x >= display_width-10 or x < 0 or y >= display_height-10 or y < 0:
            gameover = True
        x += x_change
        y += y_change
        
        gamedisplay.fill((0,0,0))
        gamedisplay.blit(apple_img, [apple_x, apple_y, ])
        gamedisplay.blit(bomb_img, [bomb_x, bomb_y, ])
        gamedisplay.blit(rotten_img, [rotten_x, rotten_y, ])
        if snake_length % 7 == 0:
            gamedisplay.blit(golden_img, [golden_x, golden_y, ])
        

        for i in snake_height[:-1]:
            if i == snake_head:
                gameover = True
       
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_height.append(snake_head)
        snake(snake_size,snake_height)

        score(snake_length-3)
        
        pygame.display.update()

        if len(snake_height) > snake_length:
            del snake_height[0]

        if apple_x <= x and apple_x + block_size >= x + snake_size:
            if apple_y <= y and apple_y + block_size >= y + snake_size:
                apple_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                apple_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                bomb_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                bomb_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                rotten_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                rotten_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                snake_length += 1

        if bomb_x <= x and bomb_x + block_size >= x + snake_size:
            if bomb_y <= y and bomb_y + block_size >= y + snake_size:
                gameover = True

        if rotten_x <= x and rotten_x + block_size >= x + snake_size:
            if rotten_y <= y and rotten_y + block_size >= y + snake_size:
                if snake_length > 5:
                    snake_length = snake_length - 3
                    rotten_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                    rotten_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0


        if golden_x <= x and golden_x + block_size >= x + snake_size:
            if golden_y <= y and golden_y + block_size >= y + snake_size:
                snake_length = snake_length + 3
                golden_x = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                golden_y = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                    
        fps = 10
        for i in range(5,1000,5):
            if snake_length-3 >= i:
                fps = fps + 5
        FPS = 0
        FPS += fps
        clock.tick(FPS)

        if snake_length-3 >= high_score1:
            high__score3 = high_score2
            high__scorer3 = high_scorer2
            high__score2 = high_score1
            high__scorer2 = high_scorer1
            high__score1 = snake_length-3
            high__scorer1 = name
        elif snake_length-3 >= high_score2:
            high__score3 = high_score2
            high__scorer3 = high_scorer2
            high__score2 = snake_length-3
            high__scorer2 = name
            high__score1 = high_score1
            high__scorer1 = high_scorer1
        elif snake_length-3 >= high_score3:
            high__score3 = snake_length-3
            high__scorer3 = name
            high__score2 = high_score2
            high__scorer2 = high_scorer2
            high__score1 = high_score1
            high__scorer1 = high_scorer1
        else:
            high__score1 = high_score1
            high__scorer1 = high_scorer1
            high__score2 = high_score2
            high__scorer2 = high_scorer2
            high__score3 = high_score3
            high__scorer3 = high_scorer3

        while gameover == True:
            gamedisplay.fill((0,0,0))
            G_text1 = font3.render("GAME OVER! ", True, (255,0,0))
            gamedisplay.blit(G_text1, [190,80])
            G_text2 = font4.render("Your score was: "+str(snake_length-3), True, (0,175,230))
            gamedisplay.blit(G_text2, [110,200])
            G_text3 = font1.render("High Scorers: ", True, (0,160,0))
            gamedisplay.blit(G_text3, [310,300])
            G_text4 = font2.render(high__scorer1+": "+str(high__score1), True, (255,130,0))
            gamedisplay.blit(G_text4, [310,350])
            G_text5 = font2.render(high__scorer2+": "+str(high__score2), True, (255,130,0))
            gamedisplay.blit(G_text5, [310,400])
            G_text6 = font2.render(high__scorer3+": "+str(high__score3), True, (255,130,0))
            gamedisplay.blit(G_text6, [310,450])
            G_text7 = font1.render("Press C to play again or Q to quit ", True, (255,255,255))
            gamedisplay.blit(G_text7, [190,500])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    if event.key == pygame.K_c:
                        gameloop()

    f=open("highscore.txt","w")
    f.write(str(high__score1))
    f.write('\n')
    f.write(high__scorer1)
    f.write('\n')
    f.write(str(high__score2))
    f.write('\n')
    f.write(high__scorer2)
    f.write('\n')
    f.write(str(high__score3))
    f.write('\n')
    f.write(high__scorer3)
    f.close()

    pygame.quit()
    quit()
gameloop()

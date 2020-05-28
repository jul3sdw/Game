#game.py
#Writen by: Julian de Wet
#Written on: 13/02/2020
#Task 15
#Program is a game where the user tries to catch the prize while avoiding the enemy characters

#Imports
import pygame
import random

#initialise pygame
pygame.init()

#Screen width and height
screen_width = 1040
screen_height =720
screen = pygame.display.set_mode((screen_width,screen_height))

#Loads player and enemy characters
player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("image.png")
prize = pygame.image.load("prize.jpg")

#Length and height of characters
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height= prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

#starting player position
playerXPosition = 100
playerYPosition = 50

#Starting enemy position
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)
prizeXPosition = screen_width - 100
prizeYPosition = random.randint(20, screen_height - prize_height)

#Control keys
keyUp = False
keyDown = False
keyRight = False
keyLeft = False


#Game Loop starts
while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize,  (prizeXPosition, prizeYPosition))

    pygame.display.flip()

    #For loop that contains the all the instructions for the game
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
        # This event checks if the user press a key down.
        
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: #Testing for up key 
                keyUp = True
            elif event.key == pygame.K_DOWN:#Testing for down key
                keyDown = True

            if event.key == pygame.K_RIGHT: #Testing for right key
                keyRight = True
            elif event.key == pygame.K_LEFT: #testing for left key
                keyLeft = True

        
        #Checks if the key is releases by the user
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP: #Checks up key
                keyUp = False
            if event.key == pygame.K_DOWN: #Checks down key
                keyDown = False
            
            if event.key == pygame.K_RIGHT: #Checks right key
                keyRight = False
            if event.key == pygame.K_LEFT: #Checks left key
                keyLeft = False

        #this allows the game to be quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        
        
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
 
    #If up key is pressed down
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    #If down key is pressed
    if keyDown == True:
        if playerYPosition < screen_height - image_height: #Makes sure the movement of the player does not leave the window
            playerYPosition += 1
    #If right key is pressed down
    if keyRight == True:
        if playerXPosition < screen_width - image_height : # This makes sure that the user does not move the player out the window.
            playerXPosition += 1
    #If left key is pressed down
    if keyLeft == True:
        if playerXPosition > 0:  # This makes sure that the user does not move the player out the window.
            playerXPosition -= 1
    
    #Creating a box around the player
    playerBox = pygame.Rect(player.get_rect())

    #Creating the length and width of the box
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    #Creating a box around the prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    #Quits game when player touches prize
    if playerBox.colliderect(prizeBox):
        #Displays message "you win"
        print("You Win!!!")
        pygame.quit()
        exit(0)
    
    #Creating a box around the enemy
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    #Quits game when you lose and are touched by the enemy
    if playerBox.colliderect(enemy1Box) :
        #Displays message "you lose"
        print("You lose!")

        pygame.quit()
        exit(0)
        
    #Creating a box around the enemy
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    #Quits game when you lose and are touched by the enemy
    if playerBox.colliderect(enemy2Box) :
        #Displays message "you lose"
        print("You lose!")

        pygame.quit()
        exit(0)
    #Creating a box around the enemy
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    #Quits game when you lose and are touched by the enemy
    if playerBox.colliderect(enemy3Box) :
        #Displays message "you lose"
        print("You lose!")

        pygame.quit()
        exit(0)

    #Movement speed of the enemy
    enemy1XPosition -= 0.40
    enemy2XPosition -= 0.30
    enemy3XPosition -= 0.20
    

import pygame
from pygame.locals import *
import socket
import pickle
import sys
import time

#legenda komunikacionog objekta
#1. komanda: l - login, p - potvrda, o - logout, u - update
#2. id: broj dodeljen korisniku
#3. x: x pozicija
#4. y: y pozicija
#5. color: boja dodeljena korisniku
#6. adress: adresa klijenta

def int_to_rgb(n):
    b = (n & 0xff0000) >> 16
    g = (n & 0x00ff00) >> 8
    r = (n & 0x0000ff)
    return (r, g, b)


if(len(sys.argv) < 3):
    print('Usage : python gameclient.py hostname port')
    sys.exit()

server_address = (sys.argv[1], int(sys.argv[2]))

# set up pygame
pygame.init()
sout = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sin = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sin.sendto(pickle.dumps(["l", 0, 0, 0, 0, '']), server_address)

display_width = 800
display_height = 600

white = (255,255,255)
idd = 0
color = 0
x = display_width / 2
y = display_height / 2
x_change = 0
y_change = 0

while True:
    data, address = sin.recvfrom(4096)
    p = pickle.loads(data)
    print('connected to server, received id %s' % p[1])
    if len(p) == 6 and p[0] == "p":
        idd = p[1]
        x = p[2]
        y = p[3]
        color = p[4]
        break

clock = pygame.time.Clock()
# set up the window
windowSurface = pygame.display.set_mode((display_width, display_height), 0, 32)
pygame.display.set_caption('Online Igrica')
my_font = pygame.font.SysFont("Courier", 16)
windowSurface.fill(white)

pygame.display.update()

#sock.setblocking(0)
#sout.settimeout(0)
sin.settimeout(0)

try:
# run the game loop
    frame_count = 0
    frame_rate = 0
    t0 = pygame.time.get_ticks()
    pygame.time.delay(int(1000/30))
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 5
        elif keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_UP]:
            y -= 5
        elif keys[pygame.K_DOWN]:
            y += 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change = -5
            #     elif event.key == pygame.K_RIGHT:
            #         x_change = 5
            #     if event.key == pygame.K_UP:
            #         y_change = -5
            #     elif event.key == pygame.K_DOWN:
            #         y_change = 5
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         x_change = 0
            #         y_change = 0
            # pygame.event.clear()
            # break

        # x += x_change
        # y += y_change

        if x < 0:
            x = 0
        if x > display_width:
            x = display_width
        if y < 0:
            y = 0
        if y > display_height:
            y = display_height
            
#        if x_change != 0 or y_change != 0:
        l = ["u", idd, x, y, 0, '']
        sout.sendto(pickle.dumps(l), server_address)

        t1 = pygame.time.get_ticks()
        frame_rate = 1000 / (t1-t0)
        t0 = t1

        L = []
        L.append(l)
        try:
            for i in range(10):
                data, address = sin.recvfrom(4096)
                L = pickle.loads(data)
        except Exception as e:
            pass

        windowSurface.fill(white)
        for user in L:
            if user[0] == "u":
                pygame.draw.circle(windowSurface, int_to_rgb(user[4]), (user[2], user[3]), 5, 0)
                #print >> sys.stderr, 'drawing at %d, %d, color %d' % (user[2], user[3], user[4])

        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        windowSurface.blit(the_text, (10, 10))

        pygame.display.flip()
        # clock.tick(60)
        pygame.time.delay(int(1000/30))
    
finally:
    pygame.quit()
    print('logging out id %s' % idd)
    sout.sendto(pickle.dumps(["o", idd, 0, 0, 0, '']), server_address)
    print('closing socket')
    sout.close()
    sin.close()


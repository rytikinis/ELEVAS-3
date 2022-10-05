import pygame, random
from Data import Time as time    
import csv

class Type():
    def __init__(self, Type_, pos):
        self.Type = Type_
        self.x = pos[0]
        self.y = pos[1]
        if self.Type == "blue":
            self.time_left = random.randint(15, 30)
            self.size = 27
        if self.Type == "darkblue":
            self.time_left = random.randint(5, 14)
            self.size = 70
        if self.Type == "yellow":
            self.time_left = random.randint(1000, 10000)
            self.size = 10
        if self.Type == "yellow_binary":
            self.time_left = random.randint(1000, 10000)
            self.size = 15
        if self.Type == "red_ag":
            self.time_left = random.randint(2, 3)
            self.size = 70
        if self.Type == "red_fbh":
            self.time_left = random.randint(2, 3)
            self.size = 70
        if self.Type == "red_ad":
            self.time_left = random.randint(2, 3)
            self.size = 70
        if self.Type == "red_yb":
            self.time_left = random.randint(2, 3)
            self.size = 15
        if self.Type == "red_y":
            self.time_left = random.randint(2, 3)
            self.size = 30
        if self.Type == "white":
            self.time_left = random.randint(30, 100)
            self.size = 25
        if self.Type == "orange":
            self.time_left = random.randint(100000000000, 100000000000)
            self.size = 20
        if self.Type == "white small":
            self.time_left = float("inf")
            self.size = 7
        if self.Type == "black_hole":
            self.time_left = float("inf")
            self.size = 40

def q(num):
    if num == 0:
        return 1
    else:
        return num

def set_4_digits(num):
    if len(str(num)) == 4:
        return str(num)
    elif len(str(num)) == 3:
        return str(num) + "0"
    elif len(str(num)) == 2:
        return str(num) + "00"
    elif len(str(num)) == 1:
        return str(num) + "000"

def SetUp(fqs, g):
    global stars, blue, darkblue, white, yellow, yellow_binary, red, red_yellow_binary, orange, black_hole, cx, cy, q, stars_born, gass, mryp, sn2, s_born, s_alive, s_died, b_born, b_alive, b_died,\
           w_born, w_alive, w_died, y_born, y_alive, y_died, o_born, o_alive, o_died, font, last_output, writer, file, sny
    pygame.font.init()
    font = pygame.font.Font("Data/Fonts/digital.ttf", 15)
    blue = pygame.image.load("Data/Images/blue.png")
    darkblue = pygame.image.load("Data/Images/darkblue.png")
    white = pygame.image.load("Data/Images/white.png")
    yellow = pygame.image.load("Data/Images/yellow.png")
    yellow_binary = pygame.image.load("Data/Images/yellow_binary.png")
    red = pygame.image.load("Data/Images/red.png")
    red_yellow_binary = pygame.image.load("Data/Images/yellow_binary_red.png").convert_alpha()
    black_hole = pygame.image.load("Data/Images/black_hole.png")
    orange = pygame.image.load("Data/Images/orange.png")
    sn2 = [pygame.image.load("Data/Images/sn2-1.png"), pygame.image.load("Data/Images/sn2-2.png"), pygame.image.load("Data/Images/sn2-3.png")]
    sny = [pygame.image.load("Data/Images/sny-1.png"), pygame.image.load("Data/Images/sny-2.png"), pygame.image.load("Data/Images/sny-3.png"), pygame.image.load("Data/Images/sny-4.png")]
    stars = list()
    cx = 0
    cy = 0
    q = 0
    stars_born = 0
    gass = g
    mryp = 0
    last_output = 0
    if fqs > 0:
        filename = "Data/Outputs/Simulation_id-"+ set_4_digits(random.randint(1, 9999)) +".csv"
        file = open((filename), "w")
        print("The file is named: " + filename)
        writer = csv.writer(file, 0, lineterminator="\n")
        writer.writerow(["time", "s_alive", "s_born", "s_died", "b_alive", "b_born", "b_died", "w_alive", "w_born", "w_died", "y_alive", "y_born", "y_died", "o_alive", "o_born", "o_died"])
        file.flush()
    s_born = 0
    s_alive = 0
    s_died = 0
    
    b_born = 0
    b_alive = 0
    b_died = 0
    
    w_born = 0
    w_alive = 0
    w_died = 0
    
    y_born = 0
    y_alive = 0
    y_died = 0
    
    o_born = 0
    o_alive = 0
    o_died = 0

def center(x, y, size):
    return (x - size / 2) - cx, (y - size / 2) - cy

def create_p(op, yp, wp, bp):
    return [op, op + yp, op + yp + wp, op + yp + wp + bp]

def formate_stars(sfr, a, frame_rate, op, yp, wp, bp, em, ybp, time_speed):
    global stars_born, gass, mryp, o_alive, o_born, y_alive, y_born, w_alive, w_born, b_alive, b_born, s_born
    pc = create_p(op, yp, wp, bp)
    if a:
        mry = int(time.mry)
        if frame_rate != 0:
            mryp += time_speed / frame_rate
        if s_born < sfr * mry and mryp >= em:
            mryp = 0
            for a in range(sfr):
                p = random.randint(1, 100)
                if p <= pc[0] and p >= pc[0] - op and gass >= 400 and op > 0:
                    stars.append(Type("orange", (random.randint(-800, 1600), random.randint(-600, 1200))))
                    gass -= 400
                    o_alive += 1
                    o_born += 1
                elif p <= pc[1] and p >= pc[1] - yp and gass >= 500 and yp > 0:
                    if op > 0:
                        p2 = random.randint(1, 100)
                        if p2 <= ybp:
                            stars.append(Type("yellow_binary", (random.randint(-800, 1600), random.randint(-600, 1200))))
                            gass -= 500
                            y_alive += 1
                            y_born += 1
                        else:
                            stars.append(Type("yellow", (random.randint(-800, 1600), random.randint(-600, 1200))))
                            gass -= 500
                            y_alive += 1
                            y_born += 1
                elif p <= pc[2] and p >= pc[2] - wp and gass >= 900 and wp > 0:
                    stars.append(Type("white", (random.randint(-800, 1600), random.randint(-600, 1200))))
                    gass -= 900
                    w_alive += 1
                    w_born += 1
                elif p <= pc[3] and p >= pc[3] - bp and gass >= 1000 and bp > 0:
                    if random.randint(1, 10) == 1 and bp > 0:
                        stars.append(Type("darkblue", (random.randint(-800, 1600), random.randint(-600, 1200))))
                    else:
                        stars.append(Type("blue", (random.randint(-800, 1600), random.randint(-600, 1200))))
                    gass -= 1000
                    b_alive += 1
                    b_born += 1
    
def update(win, frame_rate, m1, mx, my, s, p, fqs, time_speed):
    global stars, blue, darkblue, white, yellow, red, red_yellow_binary, orange, yellow_binary, black_hole, cx, cy, q, pressed_pos, sb2, s_alive, s_born, s_died, o_alive , o_born, o_died,\
            y_alive, y_born, y_died, w_alive, w_born, w_died, b_alive, b_born, b_died, last_output, writer, file
    #CSV output#
    if fqs > 0:
        if time.mry >= last_output + fqs:
            print("New output added.")
            writer.writerow((int(time.mry), s_alive, s_born, s_died, b_alive, b_born, b_died, w_alive, w_born, w_died, y_alive, y_born, y_died, o_alive, o_born, o_died))
            file.flush()
            last_output = time.mry
    #Numbers output#
    s_alive = o_alive + y_alive + b_alive + w_alive
    s_born = o_born + y_born + b_born + w_born
    s_died = o_died + y_died + b_died + w_died
    f = font.render((str((int(frame_rate), int(time.mry), s_alive, s_born, s_died, b_alive, b_born, b_died, w_alive, w_born, w_died, y_alive, y_born, y_died, o_alive, o_born, o_died))), True, (255, 255, 255))
    win.blit(f, (20, 20))
    #Move around screen#
    if m1:
        if q == 0:
            pressed_pos = (mx * -1 - cx, my * -1 - cy)
            q += 1
        else:
            cx = mx * -1 - pressed_pos[0]
            cy = my * -1 - pressed_pos[1]
    if not m1:
        q = 0
    #Draw stars#
    a = 0
    for star in stars:
        if star.Type == "blue":
            win.blit(pygame.transform.scale(blue, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        if star.Type == "darkblue":
            win.blit(pygame.transform.scale(darkblue, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "white":
            win.blit(pygame.transform.scale(white, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "white small":
            win.blit(pygame.transform.scale(white, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "yellow":
            win.blit(pygame.transform.scale(yellow, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "yellow_binary":
            win.blit(pygame.transform.scale(yellow_binary, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "red_ag":
            win.blit(pygame.transform.scale(red, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "red_fbh":
            win.blit(pygame.transform.scale(red, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "red_ad":
            win.blit(pygame.transform.scale(red, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "red_y":
            win.blit(pygame.transform.scale(red, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "red_yb":
            win.blit(pygame.transform.scale(red_yellow_binary, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "orange":
            win.blit(pygame.transform.scale(orange, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        elif star.Type == "black_hole":
            win.blit(pygame.transform.scale(black_hole, (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
        if not frame_rate == 0 and not p:
            star.time_left -= time_speed / frame_rate
        if star.time_left <= 0:
            if star.Type == "blue" or star.Type == "white":
                if star.Type == "blue":
                    b_died += 1
                    b_alive -= 1
                if star.Type == "white":
                    w_died += 1
                    w_alive -= 1
                del stars[a]
                stars.append(Type("red_ag", (star.x, star.y)))
            elif star.Type == "darkblue":
                b_died += 1
                b_alive -= 1
                del stars[a]
                stars.append(Type("red_fbh", (star.x, star.y)))
            elif star.Type == "red_ag" or star.Type == "red_yb":
                if not star.time_left < -3:
                    if star.time_left >= -1:
                        win.blit(pygame.transform.scale(sn2[0], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                    elif star.time_left >= -2:
                        win.blit(pygame.transform.scale(sn2[1], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                    elif star.time_left >= -3:
                        win.blit(pygame.transform.scale(sn2[2], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                else:
                    del stars[a]
            elif star.Type == "yellow":
                del stars[a]
                stars.append(Type("red_y", (star.x, star.y)))
            elif star.Type == "red_y":
                if not star.time_left < -4:
                    if star.time_left >= -1:
                        win.blit(pygame.transform.scale(sny[0], (star.size * s * 3, star.size * s * 3)), (center(star.x * s, star.y * s, star.size * 3)))
                    elif star.time_left >= -2:
                        win.blit(pygame.transform.scale(sny[1], (star.size * s * 3, star.size * s * 3)), (center(star.x * s, star.y * s, star.size * 3)))
                    elif star.time_left >= -3:
                        win.blit(pygame.transform.scale(sny[2], (star.size * s * 3, star.size * s * 3)), (center(star.x * s, star.y * s, star.size * 3)))
                    elif star.time_left >= -4:
                        win.blit(pygame.transform.scale(sny[3], (star.size * s * 3, star.size * s * 3)), (center(star.x * s, star.y * s, star.size  * 3)))
                else:
                    del stars[a]
                    stars.append(Type("white small", (star.x, star.y)))
            elif star.Type == "red_fbh":
                if not star.time_left < -3:
                    if star.time_left >= -1:
                        win.blit(pygame.transform.scale(sn2[0], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                    elif star.time_left >= -2:
                        win.blit(pygame.transform.scale(sn2[1], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                    elif star.time_left >= -3:
                        win.blit(pygame.transform.scale(sn2[2], (star.size * s, star.size * s)), (center(star.x * s, star.y * s, star.size)))
                else:
                    del stars[a]
                    stars.append(Type("black_hole", (star.x, star.y)))
            elif star.Type == "yellow_binary":
                stars.append(Type("red_yb", (star.x, star.y)))
                del stars[a]
            else:
                if star.Type == "orange":
                    o_died += 1
                    o_alive -= 1
                del stars[a]
        a += 1
import pickle
import math
from network import Network
from static import*
from networkstatic import*
from player import Player
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("plane war")
 
starting_time = 0
texts = []

 
def render():
    WINDOW.fill(MAIN_COLOR)


def move(keys, player, angle):

    global x, y, active
    if keys[pygame.K_w]:
        if rect.x>0:
            player.x+=math.cos(angle) *2
            player.y+=math.sin(angle) *2
    if keys[pygame.K_SPACE]:
        active = True


def render_input(text):
    COLOR = INPUT_COLOR
    if active:
        COLOR = (255, 250, 251)
  
    pygame.draw.rect(WINDOW, COLOR, chat_rect)    
    text_surface = base_font.render(text, True, (0, 0, 0))
    chat_rect.w = max(chat_rect.w, text_surface.get_width()+10)
    chat_rect.x = WIDTH-50-text_surface.get_width()  
    WINDOW.blit(text_surface, (chat_rect.x+5, chat_rect.y+5))


def render_usertext():
    space = 0
    for text in texts:
        text_surface = upper_font.render(text.text, True, (0, 0, 0))
        WINDOW.blit(text_surface, (WIDTH-(text_surface.get_width()+10), 10+space))
        space+=20
        if pygame.time.get_ticks() -text.ctime >= 10000:
            texts.remove(text)
            break



def send_usertext(n, user_text, time):
    global active
    chat_rect.w = 30
    t = utext(user_text, time)
    texts.append(t)
    n.server.send(pickle.dumps(t))
    active = False


def get_msg(n):
    while True:
        try:
            t = n.get()
            if type(t) is utext:
                t.ctime += 2 
                texts.append(t)
        except:
            pass
def render_bullet(player):
    for bullet in player.bullets:
            bullet.tick()
            pygame.draw.circle(WINDOW, (0,0,0), (int(bullet.x), int(bullet.y)), 3, 2)

def render_players(players):
    try:
        for key, p in players.items():
            rotimage = pygame.transform.rotate(image, p.angle)
            recta = rotimage.get_rect(center=(p.x, p.y))
            WINDOW.blit(rotimage, recta) 
            render_bullet(p)
    except:
        pass

def wait():
    text_surface = upper_font.render("Waiting for players ...", True, (0, 0, 0))
    WINDOW.fill(MAIN_COLOR)
    WINDOW.blit(text_surface, ( WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
    pygame.display.update()
    
def main():
    running = True
    global active
    user_text = ''
    starting_time = pygame.time.get_ticks()
    n2 = Network(0)
    thread = threading.Thread(target=get_msg, args=(n2, ))
    thread.start()
    n = Network(1)
    player = Player(300, 400)
 
    while running:
        clock.tick(60)
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    return
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if chat_rect.collidepoint(e.pos):
                        active = True
                    else:
                        active = False
                        player.add_bullet(math.atan2(dy, dx))

                if e.type == pygame.KEYDOWN:
                    if active:
                        if(e.key == pygame.K_RETURN):
                            send_usertext(n2, user_text, (pygame.time.get_ticks() ) )

                            user_text = ''
                        else:
                            user_text += e.unicode

        try:
            p = n.sendto((player))
        except socket.error as e:
            print(e)
            break
        if type(p) is not utext:
            if not p or len(p) == 1:
                wait()
                
            else:
                pos = pygame.mouse.get_pos()
                dy = pos[1]-player.y
                dx = pos[0]-player.x
                angle = 360-math.atan2(dy, dx)*180/math.pi
                
                player.angle = angle
                rotimage = pygame.transform.rotate(image, angle)
                recta = rotimage.get_rect(center=(player.x, player.y))

                keys = pygame.key.get_pressed() 
                move(keys, player, math.atan2(dy, dx))
                render()

                WINDOW.blit(rotimage, recta) 
                render_bullet(player)
                render_input(user_text)
                render_players(p)
                render_usertext()
        pygame.display.update()
    pygame.quit()

class Button:
    def __init__(self, str, x, y):
        self.x = x
        self.y = y
        self.str = str
        self.brect = pygame.Rect(x, y, 150, 90)

    def render(self):
        pygame.draw.rect(WINDOW, (255, 0, 0), self.brect)   
        self.render_text()     

    def render_text(self):
        text_surface = upper_font.render(self.str, True, (0, 0, 0))
        WINDOW.blit(text_surface, ( self.x+75 - text_surface.get_width()/2 ,  self.y+45 - text_surface.get_height()/2) ) 
def pre_main():
    b_play = Button("PLAY", WIDTH/2-75, 150)
    b_inct = Button("Instractions", WIDTH/2-75, 350)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b_play.brect.collidepoint(e.pos):
                    main()


        

        WINDOW.fill(MAIN_COLOR)
        b_play.render()
        b_inct.render()
        pygame.display.update()
    



pre_main()



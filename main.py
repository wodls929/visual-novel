import pygame
import convert_script_to_list as parser  

# pygame 초기 설정
pygame.init()

WIN_SIZE = (1000, 600)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Good Game")
font = pygame.font.SysFont('malgungothic', 20)

# 도움 함수 정의
def render_setting_menu():
    setting_surface = pygame.Surface((400, 300))
    setting_surface.fill((255, 255, 255))
    setting_surface.set_alpha(200)

    icon_save = pygame.image.load('icon/save.png')
    setting_surface.blit(icon_save, ((20, 20)))

    icon_load = pygame.image.load('icon/load.png')
    setting_surface.blit(icon_load, ((220, 20)))

    icon_setting = pygame.image.load('icon/setting.png')
    setting_surface.blit(icon_setting, ((35, 170)))     # 그림 비율이 안맞아서 15픽셀 더 오른쪽으로 옮김

    win.blit(setting_surface, (580, 130))

def render_dialogBar():
    dialog_surface = pygame.Surface((1000, 150))
    dialog_surface.set_alpha(120)
    dialog_surface.fill((255, 255, 255))
    win.blit(dialog_surface, (0, 450))

    name_surface = pygame.Surface((100, 30))
    name_surface.set_alpha(200)
    name_surface.fill((255, 255, 255))
    win.blit(name_surface, (15, 420))

def render_bgm(bgm):
    music = pygame.mixer.music.load("sound/" + bgm + ".mp3")
    pygame.mixer.music.play(-1)

def render_char(name):
    char = pygame.image.load("image/" + name + ".png")
    char = pygame.transform.scale(char, ( 300, 510))
    win.blit(char, (350, 125))
    
def render_background(bg):
    background = pygame.image.load("image/" + bg + ".png")
    win.blit(background, (0, 0))

def render_text(text):
    text_by_font = font.render(text, True, (0, 0, 0))
    win.blit(text_by_font, (50, 480))
    pygame.display.update()

def render_name(name):
    name_by_font = font.render(name, True, (0, 0, 0))
    win.blit(name_by_font, (20, 420))

def load():
    global i
    with open('savedata/save1.sav', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            save_i = int(line)
            i = save_i

def save(i, index):
    with open('savedata/save' + str(index) + '.sav', 'w', encoding='utf-8') as file:
        file.write(str(i))


#전역 변수 선언 및 필요 작업
parser.script_parser()  # script 파싱
i = 0   # 현재 장면 번호
previous_i = 0  # 화면 바뀌기 전의 장면 번호
run = True
bgm_change = True
esc = False     # esc 버튼 활성화
music = pygame.mixer.music.load("sound/" + parser.bgm_list[i] + ".mp3")
pygame.mixer.music.play(-1)

while run:

    # event 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            # 대화창 넘기기
            if event.pos[1] > 450 and event.pos[1] < 600:
                previous_i = i
                i += 1 
                bgm_change = True
            # save 버튼
            if esc and event.pos[0] > 600 and event.pos[0] < 760:       
                if event.pos[1] > 150  and event.pos[1] < 260:
                    save(i, 1)
            # load 버튼
            if esc and event.pos[0] > 800 and event.pos[0] < 960:
                if event.pos[1] > 150 and event.pos[1] < 260:
                    previous_i = i
                    load()
                    bgm_change = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                esc =  not esc

            # 대화창 넘기기
            if event.key == pygame.K_SPACE:
                previous_i = i 
                i += 1
                bgm_change = True

    if i != 0 and parser.bgm_list[previous_i] != parser.bgm_list[i] and bgm_change:
        music = pygame.mixer.music.load("sound/" + parser.bgm_list[i] + ".mp3")
        pygame.mixer.music.play(-1)
        bgm_change = False
    
    # update
    render_background(parser.background_list[i]) 
    render_char(parser.char_list[i])
    render_dialogBar()
    render_name(parser.name_list[i])
    render_text(parser.text_list[i])
    if(esc):
        render_setting_menu()    

    pygame.display.update()

pygame.quit()
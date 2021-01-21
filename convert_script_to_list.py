# import ply.lex as lex
import sys

bgm_list = []
background_list = []
char_list = []
name_list = []
text_list = []

def script_parser():
    num_bgm = 0
    num_back = 0
    num_char = 0
    num_name = 0
    num_text = 0 
    sentence = ''
    text_change = False

    with open('script.dsl', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            parts = line.split()

            # script 에서 키워드로 분류함  
            if parts[0] == 'bgm':
                bgm_list.append(parts[1])
                num_bgm += 1
                
            elif parts[0] == 'back':
                background_list.append(parts[1])
                num_back += 1
                
            elif parts[0] == 'char':
                char_list.append(parts[1])
                num_char += 1

            elif parts[0] == 'name':
                name_list.append(parts[1])
                num_name += 1

            elif parts[0] == 'text':
                for part in parts[1:]:
                    sentence += part + ' '  # 한 문장으로 만들기
                text_list.append(sentence)
                num_text += 1
                text_change = True
                sentence = '' 

            # text가 들어올 때마다 
            if (text_change):
                while num_bgm < num_text:
                    bgm_list.append(bgm_list[num_bgm-1])
                    num_bgm += 1
                while num_back < num_text:
                    background_list.append(background_list[num_back-1])
                    num_back += 1
                while num_char < num_text:
                    char_list.append(char_list[num_char-1])
                    num_char += 1
                while num_name < num_text:
                    name_list.append(name_list[num_name-1])
                    num_name += 1
                text_change = False

    print(bgm_list)
    print(background_list)
    print(char_list)
    print(name_list)
    print(text_list)

# # 토큰 정의
# tokens = [
#     'BGM',
#     'BACKGROUDN',
#     'CHARACTER',
#     'NAME',
#     'TEXT'
# ]

# # 토큰 표현
# t_BGM = r'bgm'
# t_BACKGROUDN = r'back'
# t_CHARACTER = r'char'
# t_NAME = r'name'
# t_TEXT = r'text' 
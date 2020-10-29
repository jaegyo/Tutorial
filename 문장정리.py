'''
아이디어. 
  문장의 처음이 \" \' 로 시작하면 대사줄로 인식해서, 다음 \" \' 이 나올때까지 문장을 합친다
그럼. 문장중간에 대사가 나오면 어떻게 처리하지? 일단 나만 보면 되닌깐 그냥 편하게 처리하자.
'''

scr_file = '''
안녕하세요. 만나서 반갑습니다. 
안녕하세요. 만나서 반갑습
니다. 그리고..

"하루하루가" 이렇게 흘러가다니.
이렇게 "하루하루가 흘러가다니". 
이렇게 "하루하루가 흘러가다니". 이렇게
'''
target_file = r'C:\MyWorkSpace\00 MyLibrary\00 novel\읽을 꺼리\tmp\최인호\out.txt'

trans_file = ''
for each_text in scr_file.split('\n'):
    tmp_text = each_text.strip()
    if len(tmp_text) == 0:              # 빈줄 띄우기 처리
        tmp_text = tmp_text + '\n' 
        # continue
    if tmp_text[-1:] in '\"\'':         # 대사, 생각줄 처리
        tmp_text = tmp_text + '\n\n'
    elif tmp_text[-1:] in '.!?':        # 마침표 문장 처리
        tmp_text = tmp_text + '\n'
    else:
        tmp_text = tmp_text + ''        # 문장 합치기

    trans_file = trans_file + tmp_text

# print(trans_file)
# exit()

with open(target_file, 'wt',encoding='utf8') as f:
    f.write(trans_file)

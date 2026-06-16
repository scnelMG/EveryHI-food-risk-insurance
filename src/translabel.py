import glob
import os

def translabel(foldername, after_label):
    # 폴더 안에 있는 txt 파일 리스트
    filelist = glob.glob('{}\\*.txt'.format(foldername))

    # 변환시킨 후 넣을 폴더 생성
    if not os.path.isdir('trans_'+foldername):
        os.mkdir('trans_'+foldername)
    
    # 변환
    for filename in filelist:
        with open(filename, 'r') as f:
            txtlines = ''
            lines = f.readlines()
            for line in lines:
                # 첫번째 공백 찾기 (기존 라벨 찾아내기1)
                first_blank = line.find(' ')
                
                # 공백앞의 문자
                pre_num = line[0:first_blank]
                
                # 공백앞의 문자 제거
                rm_pre_num = line.lstrip(pre_num)

                # 바꿀 문장
                after_line = str(after_label) + rm_pre_num
                txtlines += after_line
            
            # 바뀐것 생성
            with open('trans_' + filename, 'w') as f2:
                f2.write(txtlines)
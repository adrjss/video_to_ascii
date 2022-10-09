# ativar venv ou instalar lib
# pip install to-ascii==3.5.8

from toascii import Video

vid = Video('video_name.mp4', scale=0.1, verbose=True) # trocar video_name.mp4
vid.convert()

frame_atual = 0
total_frames = len(vid.frames)

txt = open("output_file.txt", "w") # trocar output_file.txt

# cria um arquivo de texto com todos os frames do video em ascii
while frame_atual < total_frames:
    ascii = str(vid.frames[frame_atual])
    txt.write(ascii+'\n[-]')
    frame_atual += 1
    
txt.close()
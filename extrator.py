import cv2
 
video = input("Digite o nome do video (escrevendo a extensão junto, ex.: nome.mp4, nome.mkv): ")

# Abre o arquivo de video (Ele tem que estar na mesma que o arquivo extrator.py)
cap= cv2.VideoCapture(video)
i=0

print("Extraindo os FRAMES, aguarde.")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('frames/'+str(i)+'.jpg',frame) #Salva o frame na pasta "frames"
    i+=1
 
print("FIM!!")
cap.release()
cv2.destroyAllWindows()
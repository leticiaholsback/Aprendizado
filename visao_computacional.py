#eu achei interessante inserir a biblioteca matplotlib pra mostrar em gráfico o aprendizado da máquina

import cv2
import matplotlib.pyplot as plt

# Essa Função vai contar as faces de uma imagem
def contar_faces(imagem_path):
    try:
        # classificador pré-treinado para detecção de faces
        classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Carrega imagem
        imagem = cv2.imread(imagem_path)
        
        # Verificar se a imagem foi carregada corretamente, no caso do professor, precisa mudar o endereço da imagem
        if imagem is None:
            print(f"Erro ao carregar a imagem: {imagem_path}")
            return -1

        # Achei mais interessante para para a  escala de cinza para melhorar a detecção, mas no print vai sair colorido
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Iniciando contador de faces
        num_faces = 0
        tentativas = []

        # Tentativas de detecção com diferentes possibilidades
        for scaleFactor in [1.1, 1.2, 1.3]:
            for minNeighbors in [3, 5, 7]:
                # Detectar faces na imagem
                faces = classificador_face.detectMultiScale(cinza, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(30, 30))

                # com o len vai fazendo a contagem das faces
                num_faces_atual = len(faces)
                num_faces += num_faces_atual

                # Nessa etapa registra a  tentativa
                tentativas.append(num_faces_atual)

        # Plotar gráfico de tentativas
        plt.plot(tentativas)
        plt.xlabel('Tentativa')
        plt.ylabel('Número de faces detectadas')
        plt.title('Número de faces detectadas por tentativa')
        plt.show()

        # Aqui desenha retângulos ao redor das faces detectadas na última tentativa
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Mostrar a imagem com as faces + destacadas
        plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        plt.title(f"Faces Detectadas: {num_faces}")
        plt.axis('off')
        plt.show()

        # Nessa parte retorna o nº total de faces detectadas
        return num_faces
    
    except Exception as e:
        print(f"Erro ao processar a imagem {imagem_path}: {e}")
        return -1

# Caminho das minhas imagens, usadas as que estão na AVA
caminhos_imagens = [
    "C:\\Users\\leticia.santos\\Desktop\\Git\\imagensDados\\img1.jpg",
    "C:\\Users\\leticia.santos\\Desktop\\Git\\imagensDados\\img2.jpg",
    "C:\\Users\\leticia.santos\\Desktop\\Git\\imagensDados\\img3.jpg",
    "C:\\Users\\leticia.santos\\Desktop\\Git\\imagensDados\\img4.jpg"
]

# Loop sobre as imagens para contar as faces até dar certo
for caminho_imagem in caminhos_imagens:
    num_faces = contar_faces(caminho_imagem)
    if num_faces >= 0:
        print(f"A imagem {caminho_imagem} possui {num_faces} faces.")

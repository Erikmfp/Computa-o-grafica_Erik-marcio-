Resumo da Prática - Parque Geométrico
Nesta atividade, dividi o trabalho entre a interface manual e a automação via Python. Manualmente, criei o quadrado, o círculo 2D, o cubo e a esfera UV, posicionando-os no espaço global com as ferramentas de translação (G) e escala (S). A animação foi feita manualmente inserindo keyframes de translação e rotação em Z para o quadrado (2D), e de escala e rotação composta (eixos X e Y) para o cubo (3D), incluindo um keyframe intermediário no frame 60 para gerar variação temporal (bônus).
Através do Python, automatizei a criação do cilindro (3D) e do triângulo (2D). Via script, apliquei rotações usando math.radians(), além de translação (location) e escala. Para garantir o bônus de hierarquia, defini o cilindro como "parent" do triângulo no código, atrelando as transformações espaciais de ambos.

1. Explique a diferença entre translação, rotação e escala em computação gráfica.
A translação move um objeto ao longo dos eixos X, Y ou Z, alterando sua posição no espaço (coordenadas). A rotação gira o objeto em torno de um eixo específico ou pivô, alterando sua orientação angular. A escala redimensiona o objeto, multiplicando suas dimensões e alterando seu tamanho em um ou múltiplos eixos.

2. Qual é a diferença entre transformar um objeto no espaço local e no espaço global?
O espaço global (World) usa os eixos fixos e absolutos da cena; o Z aponta sempre para cima, não importando a posição do objeto. O espaço local usa os eixos inerentes do próprio objeto; se você rotacionar um objeto em 45 graus, o seu eixo Z local também irá inclinar 45 graus, acompanhando a malha.

3. Em uma cena 3D, por que rotações em eixos diferentes podem gerar resultados visuais distintos?
Porque as rotações em 3D não são comutativas. A ordem importa: rotacionar um objeto primeiro no eixo X e depois no eixo Y altera a orientação dos eixos locais, resultando em uma pose final completamente diferente do que se ele fosse rotacionado primeiro em Y e depois em X.

4. No Blender, por que usar math.radians() ao definir rotation_euler por script?
A interface de usuário do Blender exibe ângulos em graus para facilitar a leitura humana, mas a API em Python e o motor matemático interno do software calculam a trigonometria exclusivamente em radianos. A função converte o valor compreensível (ex: 90 graus) para a linguagem nativa da API (1.5708 radianos).

5. Dê um exemplo prático de quando vale mais a pena usar Python em vez de transformar manualmente pela interface.
O uso de Python é ideal para tarefas altamente repetitivas, geração procedural ou precisão matemática absoluta. Um exemplo prático seria gerar uma escada em espiral com 200 degraus: fazer isso manualmente exigiria calcular e ajustar a translação e rotação em Z de cada degrau individualmente, enquanto um script com um loop for cria e posiciona todos os degraus perfeitamente em frações de segundo.

# Criptografia de Imagem: Uma Abordagem Utilizando Mapas Caóticos
## Introdução
Este repositório contém uma implementação de criptografia de imagem utilizando técnicas baseadas em mapas caóticos. O objetivo é fornecer uma solução robusta e eficaz para proteger imagens contra acesso não autorizado, garantindo confidencialidade e integridade dos dados. A criptografia de imagens é essencial em diversas aplicações, desde a proteção de dados pessoais até a segurança em comunicações militares e comerciais.

## Metodologia
### Gerador de Números Aleatórios (BEACH)
O arquivo beach.py implementa um gerador de números aleatórios e pseudo-aleatórios para aplicações criptográficas, denominado BEACH (B-Exponential All-Chaotic map-switcH). Este gerador é baseado no princípio de alternar entre diferentes mapas caóticos para extrair números aleatórios, aumentando os períodos dos ciclos da aleatoriedade. Os mapas utilizados no algoritmo são o mapa logístico e o robusto mapa B-Exponencial. Esta alternância entre mapas proporciona uma segurança adicional, tornando os números gerados mais imprevisíveis e robustos contra ataques.

#### Comportamento dos mapas caoticos com diferentes valores para r


 <img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/mapas/mapa_logistico_3.195.png" width="600" height="500" alt="Imagem 1">
 <img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/mapas/mapa_logistico_3.99.png" width="600" height="500" alt="Imagem 2">
 <img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/mapas/mapa_logistico_4.png" width="600" height="500" alt="Imagem 2">
 
 #### Comportamento do algoritmo BEACH
  <img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/mapas/algoritmo_beach.png" width="800" height="600" alt="Imagem 2">

[Artigo sobre o algoritmo BEACH](https://arxiv.org/pdf/0811.1823v2)

### Rede Feistel
A cifra de blocos é realizada pelo script blocos.py, que divide a imagem em dois blocos: esquerda e direita. O bloco da esquerda passa pelo processo de XOR, enquanto o bloco da direita passa pela função f. Após essas operações, os blocos são invertidos, com o bloco que estava à direita sendo movido para a esquerda e vice-versa. Este processo de divisão, operação e inversão é repetido sete vezes para aumentar a complexidade e segurança da criptografia.

<img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/pseudo-codigo.png" alt="pseudo-codigo" width="500" height="500">

### Função de Criptografia Central (F-Function)
A function_f.py é o coração do sistema de criptografia. Esta função é responsável por duas etapas cruciais: substituição e permutação. Durante a etapa de substituição, os dados são modificados de acordo com os números pseudo-aleatórios gerados pela função beach. Na etapa de permutação, os dados são reorganizados para garantir uma maior difusão feita pela função cubo_rubik, aumentando a complexidade e segurança da criptografia.

### Permutação
O arquivo cubo_rubik.py implementa a permutação da imagem, que rearranja os pixels da imagem para garantir maior difusão dos dados, Neste algoritmo, a imagem é permutada através de permutações aleatórias de suas linhas e colunas, usando sementes para garantir a reprodutibilidade. As permutações são aplicadas à imagem e as permutações inversas são armazenadas para permitir a reversão da permutação, se necessário.

### Geração de Chave
Para criptografar e descriptografar a imagem, é necessário uma lista de números, que representam a chave utilizada no processo. Essa chave é gerada aleatoriamente e cifrada utilizando o algoritmo AES-256. A chave criptografada é então utilizada no processo de criptografia, garantindo a segurança e integridade dos dados.
A função gera uma chave criptográfica AES-256 aleatoria. Em seguida, ela usa uma lista de números e os serializa em uma string. Utiliza a chave AES e a lista de números serializados para criptografar os dados usando o modo de operação CBC. Durante a criptografia, é adicionado um preenchimento PKCS7 para garantir que os dados tenham o tamanho necessário para serem cifrados pelo algoritmo AES. Por fim, o vetor de inicialização (IV) e os dados cifrados são codificados em base64 e retornados como uma string.

## Análise Estatística
### Entropia
A entropia é uma medida de incerteza ou desordem em um conjunto de dados. Em sistemas de criptografia, a entropia é um indicador importante da aleatoriedade e complexidade dos dados criptografados. Quanto maior a entropia, mais imprevisíveis e difíceis de decifrar são os dados.

Nos resultados fornecidos, a entropia da imagem criptografada é de 7.9993 bits por pixel, com um máximo teórico de 8 bits por pixel. A entropia percentual é de 99.99%, sugerindo que a imagem criptografada é altamente complexa e difícil de prever.

### Observe o Histograma:
Os histogramas das imagens originais e cifradas são importantes indicadores da eficácia da criptografia. O histograma de uma imagem mostra a distribuição de intensidades de cores ou níveis de cinza. No contexto da criptografia de imagem, o histograma da imagem cifrada deve ser o mais uniforme e "reto" possível, indicando que a criptografia espalhou as informações de forma aleatória e uniforme pela imagem.
<table>
  <tr>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/lena.png" width="500" height="500" alt="Imagem 1">
    <p align="center">Imagem Lena</p></td>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/lena_cifrada.png" width="500" height="500" alt="Imagem 2">
      <p align="center">Imagem Cifrada</p>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/histograma_imagem_original.png" width="450" height="450" alt="Imagem 1">
    <p align="center">Histograma Imagem Lena</p></td>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/histograma_imagem_cifrada.png" width="450" height="450" alt="Imagem 2">
      <p align="center">Histograma Imagem Cifrada</p>
    </td>
  </tr>
</table>

### Correlação
A correlação é uma medida estatística que indica o grau de relação entre duas variáveis. No contexto da criptografia de imagem, a correlação entre a imagem original e a imagem criptografada é avaliada para determinar o quanto os dados foram dispersos e obscurecidos durante o processo de criptografia.

Os resultados mostram que a correlação entre os pixels da imagem original e criptografada é muito baixa, com valores próximos de zero. Por exemplo, as correlações horizontal, vertical e diagonal da imagem original de Lena são aproximadamente <b>0.9733, 0.9865 e 0.9603</b>, respectivamente, enquanto as correlações correspondentes na imagem criptografada são próximas de zero <b>(-0.0005, -0.0002 e -0.0023, respectivamente)</b>. Isso indica uma dispersão significativa dos dados durante o processo de criptografia, dificultando a reconstrução da imagem original a partir da imagem criptografada.
<table>
  <tr>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/dispers%C3%A3o_horizontal_original.png" width="500" height="400" alt="Imagem 1">
    <p align="center">Dispersão horizontal da imagem original</p></td>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/dispers%C3%A3o_horizontal_cifrada.png" width="500" height="400" alt="Imagem 2">
      <p align="center">Dispersão horizontal da imagem cifrada</p>
    </td>
  </tr>
</table>

### Autocorrelação de pixels adjacentes
A autocorrelação de pixels adjacentes é uma maneira de avaliar a dependência espacial entre pixels em uma imagem, o que pode ser útil para analisar a estrutura de uma imagem ou a eficácia de um algoritmo de cifragem.

O gráfico de dispersão mostra a relação entre os valores dos pixels adjacentes. Se os pontos estiverem muito próximos de uma linha diagonal (indicando que os valores dos pixels adjacentes são semelhantes), isso sugere uma alta correlação espacial. Em uma imagem cifrada de alta qualidade, esperamos ver uma dispersão mais uniforme, indicando baixa correlação entre pixels adjacentes e, portanto, maior segurança.

Observe os gráficos:
<table>
  <tr>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/Adjacent%20Pixel%20Autocorrelation%20-%20Original%20Image.png" width="500" height="400" alt="Imagem 1">
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/Adjacent%20Pixel%20Autocorrelation%20-%20Original%20encrypted.png" width="500" height="400" alt="Imagem 2">
    </td>
  </tr>
</table>

### Análise Diferencial de Ataques
A análise diferencial de ataques é uma técnica utilizada para avaliar a resistência de um sistema de criptografia a pequenas alterações nos dados originais. Calculamos o Índice de Mudança Média de Intensidade Unificado (UACI) e o Índice de Redução de Pixel Normalizado (NRPC) para determinar o impacto de uma única alteração de pixel na imagem criptografada.

Os resultados indicam que, em média, uma única alteração de pixel na imagem original resulta em um UACI de 33.45869 e um NRPC de 99.62%. Isso sugere que mesmo pequenas alterações na imagem original têm um impacto significativo na imagem criptografada, tornando-a menos suscetível a ataques diferenciais.

## Sensiblidade da Chave
Utilizamos algomas metricas para avaliar a sensibilidade de pequenas alterações nas chaves
### Mean Squared Error (MSE)
O valor de MSE que o algoritmo obteve é 4892.553455352783. O MSE mede a média dos quadrados das diferenças entre os valores dos pixels correspondentes nas duas imagens. Em termos gerais:

- MSE baixo: Indica que as duas imagens são bastante similares.
- MSE alto: Indica que as duas imagens são muito diferentes.
Um MSE de aproximadamente 4892 sugere que há uma diferença significativa entre as duas imagens. Isso é esperado se as imagens foram criptografadas com chaves diferentes, pois a criptografia tende a gerar resultados muito diferentes para pequenas variações na chave.

### Structural Similarity Index (SSIM)
O valor de SSIM que o algoritmo obteve é 0.009508408453325153. O SSIM mede a similaridade estrutural entre duas imagens, considerando luminância, contraste e estrutura. Os valores variam de -1 a 1, onde:

- SSIM próximo de 1: As imagens são muito similares.
- SSIM próximo de 0: As imagens são bastante diferentes.
- SSIM negativo: Indica uma similaridade estrutural muito baixa, com potencial inversão de contraste.
Um SSIM de aproximadamente 0.0095 indica que as duas imagens têm uma similaridade estrutural extremamente baixa. Isso também é esperado no contexto de imagens criptografadas com chaves diferentes, pois cada pequena alteração na chave pode causar grandes mudanças na estrutura da imagem resultante.

### Analise
Os valores de MSE e SSIM juntos indicam que as duas imagens criptografadas são significativamente diferentes tanto em termos de valores de pixels quanto em termos de estrutura geral. Isso sugere que a criptografia com chaves diferentes está funcionando como esperado, produzindo imagens criptografadas que são praticamente incomparáveis entre si, mesmo que a imagem original seja a mesma.

Esses resultados são típicos de algoritmos de criptografia robustos, onde a alteração mínima na chave deve resultar em uma saída completamente diferente, assegurando a segurança e a imprevisibilidade da criptografia.

### Observe imagens criptografadas com pequenas alterações nas chaves
<table>
  <tr>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/img_cifrada_chave_0.001985_0.153972.png" width="400" height="400" alt="Imagem 1">
    <p align="center">Imagem Cifrada com chaves (0.001985, 0.153972)</p></td>
    <td><img src="https://github.com/Teixeira007/image-encryption-chaotic-maps/blob/main/imagens/readme/img_cifrada_chave_0.001986_0.153973.png" width="400" height="400" alt="Imagem 2">
      <p align="center">Imagem Cifrada com chaves (0.001986, 0.153973)</p>
    </td>
  </tr>
</table>
<table>

### Observação
Todos os valores e metricas estatisticas podem ser encontrados nos seguintes algoritmos (estatisticas.py, estatisticas_map.py, ataques_diferencial.py)
### Como Executar o Projeto.


1. Clonar o Projeto
Clone este repositório em sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/Teixeira007/image-encryption-chaotic-maps
```
2. Instalar Dependências
Antes de executar o projeto, é necessário instalar as dependências. Certifique-se de ter o Python e o pip instalados em sua máquina. Em seguida, execute o seguinte comando:

```bash
pip install matplotlib opencv-python numpy cryptography math scikit-image scipy
```
3. Executar o Arquivo Python
4. Execute o script main.py, nele vc passa o caminho da imagem a ser criptografada, o algoritmo já criptografa e descriptografa pra você, no main, você pode passar a imagem criptografada e chamar a função para descriptografar.
```bash
python main.py
```
5. Utilize os demais scripts para análise e avaliação da criptografia, conforme necessário.
6. Pode executar o algoritmo testes_nist.py, para ver o resultado dos testes, nele você passa o caminho do arquivo que está com a sequencia de bits da imagem criptografada
```bash
python testes_nist.py
```
7. Para realizar os testes nist foi utilizado os codigos do repositorio do NIST Randomness Test Suite
```bash
git clone https://github.com/stevenang/randomness_testsuite.git
```
8. O resultado dos testes estão num arquivo txt chamado testes_nist
9. E os outros dados estatisticos estão bum arquivo txt chamado testes_estatisticos


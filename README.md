# BEACH
Gerador de números aleatórios e pseudo-aleatórios para aplicações criptográficas, um gerador baseado no Mapa B-Exponencial com o nome BEACH (B-Exponential All-Chaotic map-switcH). Como o nome sugere, o gerador de números pseudoaleatórios é baseado no princípio de alternar de mapa para mapa para extrair números para o gerador, os mapas utilizado no algoritmo foi o mapa logistico e o mapa robusto B-Exponencial.

[Artigo sobre o algoritmo BEACH](https://arxiv.org/pdf/0811.1823v2)



### Como Executar o Projeto
1. Clonar o Projeto
Clone este repositório em sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/Teixeira007/BEACH
```
2. Instalar Dependências
Antes de executar o projeto, é necessário instalar as dependências. Certifique-se de ter o Python e o pip instalados em sua máquina. Em seguida, execute o seguinte comando:

```bash
pip install numpy math struct
```
3. Executar o Arquivo Python
Depois de instalar as dependências, execute o arquivo Beach.py usando o seguinte comando:

```bash
python Beach.py
```
Isso gerará um arquivo de texto chamado numeros_binarios_v0.txt contendo os números aleatórios gerados em formato binário.

### Testando a Aleatoriedade
Para testar a aleatoriedade dos números gerados, você pode usar o NIST Randomness Test Suite.

1. Clonar o Repositório do Test Suite
Clone o repositório do NIST Randomness Test Suite em sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/stevenang/randomness_testsuite.git
```
2. Instalar Dependências do Test Suite
Antes de executar os testes, instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip3 install numpy scipy
```
3. Executar os Testes
Depois de instalar as dependências, execute os testes usando o seguinte comando:

```bash
python3 Main.py
```
Isso abrirá uma interface onde você pode selecionar o arquivo numeros_binarios_v0.txt gerado anteriormente. Selecione todos os testes disponíveis e clique no botão "Executar Testes" para iniciar os testes de aleatoriedade.

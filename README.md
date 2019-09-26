# Problema dos Missionários e Canibais

Trabalho de I.A. UFJF 2019/3 

## Configurar e rodar

Execute os comandos abaixo:

```bash
## instalar python e PIP
apt-get install python3 python3-pip

# instalar graphviz para gerar os grafos
apt-get install libgraphviz-dev graphviz

# instalar dependencias python do projeto
pip3 install -r requirements.txt

# Executar o projeto
python3 main.py
```

## O problema

O problema dos missionários e canibais é um problema famoso de IA, usuamente definico como se segue.

Três missionários e três canibais estão em um lado do rio, junto com um bote que tem capacidade de no máximo duas pessoas. O objetivo é atravessar para a outra margem do rio os seis integrantes do grupo atendendo as seguintes restrições:

* o bote não pode ter mais de duas ou menos de uma pessoa ao trafegar;
* Não pode ter em qualquer margem um número maior de canibais do que de missionários, senão os missionários serão atacados.

Tendo esse problema como base, o objetivo deste trabalho será resolver uma versão ampliada desse problema (ex.: 5 missionários e 5 canibais).


## Modelagem do Problema

Para representar o estado atual do problema será utilizado um vetor [m, c, b], em que os elementos representam respectivamente o número de missionários, canibais e barcos no lado errado do rio. As ações tomadas serão representadas usando adição e subtração de vetor para manipular o vetor estado.

Consideramos como ações todas as possibilidades que um bote tem de fazer a travessia. Seja a menor instância que será considerada para o problema [3, 3, 1], as ações de travessia são:[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1] e [1, 1, 1].

* Espaço de estados: 0 <= m, c, b <= N, onde N = |c| = |m|
* Estado inicial:[m, c, b]
* Estado Final: [0, 0, 0]
* Custo do caminho: 1 por travessia
* Função de sucessores:

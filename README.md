# Missionaries_and_Cannibals_Problem

"# Problema dos Missionários e Canibais\n",
    "\n",
    "O problema dos missionários e canibais é um problema famoso de IA, usuamente definico como se segue.\n",
    "\n",
    "Três missionários e três canibais estão em um lado do rio, junto com um bote que tem capacidade de no máximo duas pessoas. O objetivo é atravessar para a outra margem do rio os seis integrantes do grupo atendendo as seguintes restrições:\n",
    "* o bote não pode ter mais de duas ou menos de uma pessoa ao trafegar\n",
    "* Não pode ter em qualquer margem um número maior de canibais do que de missionários, senão os missionários serão atacados.\n",
    "\n",
    "Tendo esse problema como base, o objetivo deste trabalho será resolver uma versão ampliada desse problema (ex.: 5 missionários e 5 canibais).

"## Modelagem do Problema\n",
    "\n",
    "Para representar o estado atual do problema será utilizado um vetor [m, c, b], em que os elementos representam respectivamente o número de missionários, canibais e barcos no lado errado do rio. As ações tomadas serão representadas usando adição e subtração de vetor para manipular o vetor estado.\n",
    "\n",
    "Consideramos como ações todas as possibilidades que um bote tem de fazer a travessia. Seja a menor instância que será considerada para o problema [3, 3, 1], as ações de travessia são:[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1] e [1, 1, 1].\n",
    "\n",
    "* **Espaço de estados:** 0 <= m, c, b <= N, onde N = |c| = |m|\n",
    "* **Estado inicial:** [m, c, b]\n",
    "* **Estado Final:** [0, 0, 0]\n",
    "* **Custo do caminho:** 1 por travessia\n",
    "* **Função de sucessores:**"

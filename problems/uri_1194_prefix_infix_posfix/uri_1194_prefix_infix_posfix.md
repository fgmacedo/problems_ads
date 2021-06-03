
# Prefixa, Infixa e Posfixa

Problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/1194

Um problema comum em estrutura de dados é determinar o percurso transversal de uma árvore binária.

Há tres formas clássicas de fazer isto:
Prefixa: Você deve visitar a raiz, sub-árvore esquerda e sub-árvore direita.
Infixa: Você deve visitar a sub-árvore esquerda, a raiz e a sub-árvore direita.
Posfixa: Você deve visitar a sub-árvore esquerda, a sub-árvore direita e a raiz.

Veja a figura abaixo:





O percurso prefixo, infixo e posfixo são, respectivamente ABCDEF, CBAEDF and CBEFDA. Neste problema, você deve computar a forma posfixa da árvore dados os percursos infixo e prefixo

## Entrada
A primeira linha de entrada contém um número positivo C (C ≤ 2000), que indica o número de casos de teste. Seguem C linhas, uma para cada caso de teste. Cada caso de teste inicia com um número N (1 ≤ N ≤ 52), o número de nodos da árvore binária. Depois haverá duas strings S1 e S2 que descrevem o percurso prefixo e infixo da árvore. Os nodos da árvore são nomeados com diferentes caracteres dentro do intervalo a..z e A..Z. O valor de N, S1 e S2 são separados por um espaço em branco.

## Saída
Para cada conjunto de entrada, você deve imprimir uma linha contendo o percurso posfixo da corrente árvore.

## Exemplo de Entrada

```
3
3 xYz Yxz
3 abc cba
6 ABCDEF CBAEDF
```

## Exemplo de Saída

```
Yzx
cba
CBEFDA
```

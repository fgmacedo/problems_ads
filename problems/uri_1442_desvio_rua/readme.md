# Desvio de Rua

https://www.urionlinejudge.com.br/judge/pt/problems/view/1442

A prefeitura de uma grande cidade da Nlogônia iniciou um programa de recuperação do asfalto de suas ruas. Na Nlogônia, cada rua liga diretamente dois cruzamentos, e pode ter mão única ou mão dupla. Por determinação de um antigo decreto real, sempre existe ao menos um caminho entre dois pontos quaisquer da cidade.

No programa de recuperação, uma única rua será recuperada por vez, e para isso a rua será fechada para o tráfego. Esse fechamento pode causar caos no trânsito local ao violar o decreto real, impedindo vários cidadãos de voltarem para casa dos seus trabalhos e vice-versa. A prefeitura pode converter algumas das ruas de mão única em mão dupla, mas prefere evitá-lo pois ruas de mão dupla tendem a causar acidentes mais graves; a prefeitura prefere criar desvios apenas invertendo as mãos das ruas de mão única já existentes.

O Rei da Nlogônia solicitou seus préstimos para escrever um programa que, dada a descrição das ruas de uma cidade, determine se, quando uma dada rua é interditada para recuperação, continua existindo um caminho entre quaisquer dois pontos da cidade, mesmo que seja necessário alterar as mãos de direção de outras ruas.

## Entrada
A entrada é composta por diversos casos de teste. A primeira linha de um caso de teste contém dois inteiros N (1 ≤ N ≤ 103) e M (1 ≤ M ≤ 105), representando respectivamente o número de cruzamentos e o número de ruas da cidade. Os cruzamentos são identificados por inteiros de 1 a N e as ruas são identificadas por números inteiros de 1 a M. Cada uma das M linhas seguintes descreve uma rua e contém três inteiros A (1 ≤ A), B (B ≤ N) e T (1 ≤ T ≤ 2), onde A e B são os cruzamentos que a rua liga diretamente, e T indica a mão de direção da rua: se T = 1 a rua tem mão única na direção de A para B; se T = 2 a rua tem mão dupla. A primeira rua descrita será interditada para recuperação.

## Saída
Para cada caso de teste seu programa deve imprimir uma linha contendo um caractere que descreve o que a prefeitura deve fazer para respeitar o decreto real após o fechamento da rua para reformas:

- '-': não é necessário qualquer tipo de alteração nas outras ruas.
- '*': é impossível respeitar o decreto real, independente de quaisquer mudanças nas outras ruas.
- '1': é possível cumprir o decreto real apenas invertendo as mãos de algumas das ruas de mão única.
- '2': é possível cumprir o decreto real, mas é necessário converter algumas ruas de mão única para mão dupla.

## Exemplo

In:
```
3 3
1 2 2
2 3 2
3 1 2
3 3
1 2 1
2 3 1
3 1 1
2 1
1 2 2
5 6
3 4 1
1 3 2
2 4 2
3 5 2
2 1 1
4 1 1
```

Out:
```
-
2
*
1
```


# Olimpíadas

https://olimpiada.ic.unicamp.br/pratique/p1/2009/f2/olimp/

O Comitê Olímpico Internacional (COI) está visitando as cidades candidatas a sediar as Olimpíadas de 2016. O Rio de Janeiro é uma das cidades concorrentes, mas a competição é muito acirrada.

O COI tem um conjunto de exigências que devem ser obedecidas pelas cidades candidatas, como boas arenas para os jogos (ginásios, campos de futebol, pistas de atletismo, parque aquático,…), bons alojamentos, um plano para o tráfego de veículos durante os jogos, etc. Durante sua visita ao Rio de Janeiro, o COI colocou ainda mais uma exigência: a demonstração da qualidade dos sistemas de informática. Especificamente, o COI quer que a organização local demonstre a sua capacidade em informática produzindo um programa que gere a classificação final dos países, considerando o número de medalhas recebidas pelos atletas de cada país.

##Tarefa
Sua tarefa é escrever um programa que, dada a informação dos países que receberam medalhas de ouro, prata e bronze em cada modalidade, gere a lista de classificação dos países na competição. Nesta tarefa, os países serão identificados por números inteiros. O melhor colocado deve ser o país que conseguiu o maior número de medalhas de ouro. Se houver empate entre países no número de medalhas de ouro, o melhor colocado entre esses é o país que conseguiu o maior número de medalhas de prata. Se houver empate também no número de medalhas de prata, o melhor colocado entre esses é o país que recebeu o maior número de medalhas de bronze. Se ainda assim houver empate entre dois países, o melhor classificado é o que tem o menor número de identificação.

## Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).

A primeira linha da entrada contém dois números inteiros N e M , separados por um espaço em branco, indicando respectivamente o número de países (1 ≤ N ≤ 100) e número de modalidades esportivas envolvidas na competição (1 ≤ M ≤ 100). Os países são identificados por números inteiros de 1 a N .

Cada uma das M linhas seguintes contém três números inteiros O, P e B, separados por um espaço em branco, representando os países cujos atletas receberam respectivamente medalhas de ouro (1 ≤ O ≤ N ), prata (1 ≤ P ≤ N ) e bronze (1 ≤ B ≤ N ). Assim, se uma das M linhas contém os números 3 2 1, significa que nessa modalidade a medalha de outro foi ganha pelo país 3, a de prata pelo país 2 e a de bronze pelo país 1.

## Saída
Seu programa deve imprimir, na saída padrão, uma linha contendo N números, separados por um espaço em branco, representando os países na ordem decrescente de classificação (o primeiro número representa o país que é o primeiro colocado, o segundo número representa o país que é o segundo colocado, e assim por diante).

Informações sobre a pontuação
Em um conjunto de casos de teste que totaliza 30 pontos, N ≤ 10 e M ≤ 10
Em um conjunto de casos de teste que totaliza 70 pontos, N ≤ 50 e M ≤ 50.

## Exemplos

Entrada:

```
2 2
2 1 2
1 2 2
```

Saída:

```
2 1
```

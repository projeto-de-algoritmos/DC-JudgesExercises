# Integrantes

|                         Nome                         | Matrícula |
| :--------------------------------------------------: | :-------: |
|  [Pedro Torreão](https://github.com/PedroTorreao21)  | 190036761 |
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421 |

# Introdução

Este repositório foi criado para o desenvolvimento do módulo Dividir e Conquistar da disciplina Projeto de Algoritmos do Professor Maurício Serrano.

# Apresentação

[Link para a apresentação da dupla]()

# Foram feitos os exercícios no LeetCode

## [215. Kth Largest Element in an Array (Medium)](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

Determinar o K-ésimo maior elemento em um array não ordenado pode ser abordado de maneira eficiente utilizando a técnica de seleção. Essa abordagem envolve a divisão do array em grupos menores usando a Média das medianas para, posteriormente, encontrar a posição apropriada do K-ésimo elemento.

![Kth Largest Element in an Array](/images/215.jpeg)

## [493. Reverse Pairs (Hard)](https://leetcode.com/problems/reverse-pairs/description/)

Neste exercício, ao ser fornecido um array de números inteiros, é necessário calcular o número de pares de índices (i, j), onde i < j, e nums[i] > 2 \* nums[j]. Por exemplo, considerando a entrada [1, 3, 2, 3, 1], existem 2 pares invertidos: (3, 1) e (3, 1). Assim, a saída esperada é 2. A solução para esse exercício envolve a aplicação do algoritmo de Contagem de inversão para identificar e contar os pares de elementos que satisfazem a condição de inversão.

![Reverse Pairs](/images/493.jpeg)

## [2391. Minimum Amount of Time to Collect Garbage(Medium)](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/)

Você recebe uma matriz indexada em 0 de strings trash, onde trash[i] representa a variedade de lixo na i-ésima casa. lixo[i] consiste apenas nos caracteres 'M', 'P' e 'G' representando uma unidade de lixo de metal, papel e vidro respectivamente. Recolher uma unidade de qualquer tipo de lixo leva 1 minuto.

Você também recebe uma viagem de matriz inteira indexada em 0, onde viagem[i] é o número de minutos necessários para ir da casa i à casa i + 1.

Existem três caminhões de lixo na cidade, cada um responsável por recolher um tipo de lixo. Cada caminhão de lixo começa na casa 0 e deve visitar cada casa na ordem; no entanto, eles não precisam visitar todas as casas.

Apenas um caminhão de lixo poderá ser utilizado por vez. Enquanto um caminhão está dirigindo ou recolhendo lixo, os outros dois caminhões não podem fazer nada.

Devolva o número mínimo de minutos necessários para recolher todo o lixo.

![Minimum Amount of Time to Collect Garbage](/images/2391.jpg)

## [218. The Skyline Problem (Hard)](https://leetcode.com/problems/the-skyline-problem/)

O horizonte de uma cidade é o contorno externo da silhueta formada por todos os edifícios daquela cidade quando vistos à distância. Dadas as localizações e alturas de todos os edifícios, retorne o horizonte formado por esses edifícios coletivamente.

A informação geométrica de cada edifício é dada na matriz edifícios onde edifícios[i] = [esquerda, direita, alturai]:

lefti é a coordenada x da borda esquerda do i-ésimo edifício.
righti é a coordenada x da borda direita do i-ésimo edifício.
heighti é a altura do i-ésimo edifício.
Você pode assumir que todos os edifícios são retângulos perfeitos apoiados em uma superfície absolutamente plana na altura 0.

O horizonte deve ser representado como uma lista de "pontos-chave" classificados por sua coordenada x na forma [[x1,y1],[x2,y2],...]. Cada ponto-chave é o extremo esquerdo de algum segmento horizontal no horizonte, exceto o último ponto da lista, que sempre tem uma coordenada y 0 e é usado para marcar o término do horizonte onde termina o edifício mais à direita. Qualquer terreno entre os edifícios mais à esquerda e à direita deve fazer parte do contorno do horizonte.

Nota: Não deve haver linhas horizontais consecutivas de igual altura no horizonte de saída. Por exemplo, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] não é aceitável; as três linhas de altura 5 devem ser mescladas em uma na saída final como tal: [...,[2 3],[4 5],[12 7],...]

![The Skyline Problem](/images/218.jpg)

# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do Leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.

# Uso

## Passo 1: Copiar o código

Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício

Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão.

## Passo 3: Alterar linguagem

Selecione a linguagem.

## Passo 4: Colar o código

Cole o código copiado no editor.

## Passo 5: Rodar o código

Abaixo do editor de código, clique em Run para executar o código.

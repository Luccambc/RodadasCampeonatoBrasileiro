
# Projeto 3 - Teoria e Aplicação de Grafos

### Lucca Magalhães Boselli Couto - 222011552

## Sobre o projeto

Nesse projeto, os conceitos de grafos foram utilizados para montar as 38 rodadas do campeonato brasileiro, de forma que se aplicaram algumas restrições para cada uma das rodadas. Nesse sentido, times do mesmo estado (ex: Vasco, Botafogo, Fluminense e Flamengo) não poderiam jogar como mandantes na mesma rodada, ou seja, enquanto um deles é mandante, os outros devem ser visitantes.

Durante a execução do projeto, percebe-se que não é possível que as 38 rodadas sejam realizadas seguindo à risca as restrições de mando de campo, portanto times de mesmo estado acabam jogando como mandante na mesma rodada em alguns casos.

Ao final do código obtemos a visualização do grafo em seu estado inicial e também o grafo com sua coloração. Além disso, no arquivo "cronograma.txt" podemos visualizar as 38 rodadas completas com os mandos de campo (é possível visualizar como ficaram as 3 primeiras rodadas ao final do readme)

## Código

1) Abaixo temos as bibliotecas utilizadas no código, tal como os times e suas correspondências (siglas e nomes) e as restrições
![Bibliotecas e Dicinário de times e restrições](URL_da_Imagem)

2. Foi utilizado o algoritmo round robin para definir o cronograma de jogos de equipes. Esse algorimo é bastante utilizado nesse cenário de esportes e definição de confrontos
![Função round_robin_schedule](URL_da_Imagem)

3. A função adjust_schedule mostrada na imagem abaixo tem o intuito de tentar ajustar o cronograma de partidas para obedecer às restrições impostas (times de mesmo estado não podem ser mandantes na mesma rodada)
![Função adjust_schedule](URL_da_Imagem)

4. Abaixo temos a função validate_schedule que verifica se é possível montar as 38 rodadas seguindo a restrição imposta para a formação dos jogos em cada rodada. Essa função retorna um boolean False, indicando que não é possível realizar as 38 rodadas do campeonato seguindo nossa restrição
![Função validate_schedule](URL_da_Imagem)

5. O pedaço de código abaixo salva em um arquivo .txt as rodadas do campeonato brasileiro, de forma que podemos visualizar as 38 rodadas com 10 jogos em cada uma delas e verificar os mandantes e visitantes
![Função save_schedule_to_file](URL_da_Imagem)

6. Podemos visualizar abaixo o código referente à criação do grafo para as rodadas do campeonato brasileiro. O retorno dessa função (grafo inicial desenhado) poderá ser visualizado logo após o snippet de código abaixo
![Função create_graph_from_schedule](URL_da_Imagem)
![Grafo inicial](URL_da_Imagem)

7. Por fim, podemos observar abaixo o código utilizado para achar a coloração ótima do grafo. Além disso, abaixo do código podemos ver o resultado final da coloração
![Função find_optimal_coloring](URL_da_Imagem)
![Grafo colorado final](URL_da_Imagem)

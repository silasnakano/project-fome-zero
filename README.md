# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. 

Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados!

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero.

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez:

## Geral

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país? 

## Cidade

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

# 2. Premissas assumidas para a análise

1. A análise foi realizada com os dados disponíveis pelo site Kaggle.
2. Marketplace foi o modelo de negócio assumido.
3. As 4 principais visões de negócio foram: Visão Países, Visão Cidades, Visão Restaurantes e Visão Tipos de Culinária.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões do modelo de negócio da empresa:

1. Visão do crescimento da empresa de acordo com os países
2. Visão do crescimento da empresa de acordo com as cidades
3. Visão do crescimento da empresa de acordo com os restaurantes
4. Visão do crescimento da empresa de acordo com os tipos de culinária

Cada visão é representada pelos seguintes conjuntos de métricas:

1. Visão do crescimento da empresa de acordo com os países
    1. Nome do país que possui mais cidades registradas.
    2. Nome do país que possui mais restaurantes registrados.
    3. Nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados.
    4. Nome do país que possui a maior quantidade de tipos de culinária distintos.
    5. Nome do país que possui a maior quantidade de avaliações feitas.
    6. Nome do país que possui a maior quantidade de restaurantes que fazem entrega.
    7. Nome do país que possui a maior quantidade de restaurantes que aceitam reservas.
    8. Nome do país que possui, na média, a maior quantidade de avaliações registrada.
    9. Nome do país que possui, na média, a maior nota média registrada.
    10. Nome do país que possui, na média, a menor nota média registrada.
    11. Média de preço de um prato para dois por país.

2. Visão do crescimento da empresa de acordo com as cidades
    1. Nome da cidade que possui mais restaurantes registrados.
    2. Nome da cidade que possui mais restaurantes com nota média acima de 4.
    3. Nome da cidade que possui mais restaurantes com nota média abaixo de 2.5.
    4. Nome da cidade que possui o maior valor médio de um prato para dois.
    5. Nome da cidade que possui a maior quantidade de tipos de culinária distintas.
    6. Nome da cidade que possui a maior quantidade de restaurantes que fazem reservas.
    7. Nome da cidade que possui a maior quantidade de restaurantes que fazem entregas.
    8. Nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online.

3. Visão do crescimento da empresa de acordo com os restaurantes
    1. Nome do restaurante que possui a maior quantidade de avaliações.
    2. Nome do restaurante com a maior nota média.
    3. Nome do restaurante que possui o maior valor de uma prato para duas pessoas.
    4. Nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação.
    5. Nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação.
    6. Restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas.
    7. Restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas.
    8. Restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ).

4. Visão do crescimento da empresa de acordo com os tipos de culinária
    1. Restaurantes que possuem o tipo de culinária italiana, o nome do restaurante com a maior média de avaliação.
    2. Restaurantes que possuem o tipo de culinária italiana, o nome do restaurante com a menor média de avaliação.
    3. Restaurantes que possuem o tipo de culinária americana, o nome do restaurante com a maior média de avaliação.
    4. Restaurantes que possuem o tipo de culinária americana, o nome do restaurante com a menor média de avaliação.
    5. Restaurantes que possuem o tipo de culinária árabe, o nome do restaurante com a maior média de avaliação.
    6. Restaurantes que possuem o tipo de culinária árabe, o nome do restaurante com a menor média de avaliação.
    7. Restaurantes que possuem o tipo de culinária japonesa, o nome do restaurante com a maior média de avaliação.
    8. Restaurantes que possuem o tipo de culinária japonesa, o nome do restaurante com a menor média de avaliação.
    9. Restaurantes que possuem o tipo de culinária caseira, o nome do restaurante com a maior média de avaliação.
    10. Restaurantes que possuem o tipo de culinária caseira, o nome do restaurante com a menor média de avaliação.
    11. Tipo de culinária que possui o maior valor médio de um prato para duas pessoas.
    12. Tipo de culinária que possui a maior nota média.
    13. Tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas.

# 4. Top 4 insights de dados

1. Emirados Árabes é o país com maior quantidade de restaurantes registrados.
2. A cidade Pasay é a cidade com maior valor médio de um prato para duas pessoas.
3. AB's Absolute Barbecues é o restaurante com maior registro de avaliações. 
4. A culinária japonesa é a culinária com maior média de nota.

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através deste link: https://silasnakano-project-fome-zero.streamlit.app

# 6. Conclusão

O objetivo foi utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.

Da visão países, podemos concluir que Filipinas foi o país teve o maior número de cidades registradas, resultando na maior média de avaliações feitas e também possuindo a maior média de preço para um prato para duas pessoas.

Da visão cidades, São Paulo é uma das cidades com maior registro de restaurantes e também com a maior variedade de tipos de culinária.

Da visão restaurantes, Sushi Leblon é um dos restaurantes que possuem a maior nota e também Sambo Kojin é o restaurante com maior valor médio de um prato para duas pessoas.

Da visão culinária, a comida indiana é a culinária com maior número de registro de avaliações e também com a maior média de avaliações sem possuir pedidos online.

# 7. Próximos passos

1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócio.

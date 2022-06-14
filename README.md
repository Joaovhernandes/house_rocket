## Introdução

A House Rocket é uma empresa situada nos Estados Unidos, na cidade de Seattle e atua no setor imobiliário. Atualmente, é responsável por empregar mais de 100 pessoas em seu escritório e seu negócio é baseado na compra e venda de imóveis.

O setor imobiliário é um dos mais lucrativos e exige um conhecimento e conjunto de técnicas avançadas para que se possa obter lucro em suas vendas e descontos em nas compras. No último ano, a empresa teve um faturamento de U$ 142.560.000,00, tendo uma venda média de uma casa por dia (22 dias por mês ou 264 dias por ano) a um preço médio de U$ 540.083,52. Nesse ano, a House Rocket deseja manter uma mesma quantidade média de casas vendidas, porém, aumentar o lucro, sendo assim, deseja comprar e vender a casa no momento certo. Para isso, um estudo de Ciência de Dados foi solicitado.

## O Problema de Negócio

De acordo com a base de dados, há mais de 16000 registros, o que torna necessário ter à disposição um conjunto de técnicas e ferramentas de Ciência de Dados para a solução do problema.

Em reunião com a diretoria e conselheiros, foi definido que o preço ideal para compra é 10% menor que o valor registrado na base de dados do imóvel e o preço ideal para venda é de 10% maior do que o registrado na base de dados.

Para isso, a diretoria desejava poder avaliar as casas de forma fácil, rápida e intuitiva, podendo ser selecionadas as características mais relevantes que desejassem avaliar no momento para tomar uma decisão. Portanto, era necessário um produto que auxiliasse na decisão estratégica.

## Planejamento da Solução

Para solucionar o problema de negócio o qual a empresa estava enfrentando, foi utilizado o método SAPE (saída, processo e entrada), podendo, dessa forma, encontrar os melhores processos e mapear a fonte dos dados.

### Saída

Criação de um aplicativo para a visualização dos dados e os preços de compra e venda.

Ferramentas utilizadas:

- Streamlit
- Cloud Heroku

### Processo

Realizar uma EDA dos dados coletados, buscando identificar dados relevantes, bem como realizar o tratamento e manipulação para que tragam uma informação estratégica e insights para o time de negócio.

Ferramentas utilizadas:

- Python 3.9
- Jupyter Notebook
- PyCharm

### Entrada

Fonte de dados: [https://www.kaggle.com/datasets/shivachandel/kc-house-data](https://www.kaggle.com/datasets/shivachandel/kc-house-data)

## Insights

Durante a execução do projeto, alguns pontos foram levantados e respondidos conforme abaixo:

### Variação do preço ao longo dos anos:

Ao longo dos anos, observa-se que o preço das casas permanecem em um uma faixa, porém, é interessante observar que durante os meses 10 e 11 do ano de 2014 houve um pico no preço médio das casas.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/816328f1-332f-436c-b950-575472271f0d/Untitled.png)

Além disso, o preço médio das cassas vem aumentando durante as últimas semanas do ano de 2015, o que indica uma valorização e oportunidade para venda dos imóveis.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f58da132-81fa-4cea-ac65-d9448dafa4d8/Untitled.png)

### Variação do preço de acordo com os meses do ano

Observou-se que a mediana dos preços, quando separada em meses, tende a ser maior entre os meses de abril e julho (período das estações quentes), enquanto os menores preços são nos meses de janeiro, fevereiro, novembro e dezembro (período das estações mais frias).

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b628bd55-f16f-4dd2-b51b-816995206383/Untitled.png)

### Localização dos imóveis de acordo com o nível

No mapa abaixo estão localizados os imóveis e sua cor de acordo com a legenda, indica o nível. É interessante observar que a maioria dos imóveis com um nível maior estão localizados na parte central e norte do mapa e estão predominantemente próximos a água.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1fc8735-300a-4d6d-b432-81b39ef97d66/Untitled.png)

Sendo assim, torna-se interessante avaliar algumas características sobre os imóveis com vista para água.

### Casas com vista para água e suas características

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0233a5c4-c4a1-403e-ad37-e7659f93175c/Untitled.png)

De acordo com os dados, os imóveis que possuem vista para água possuem um preço total 3 vezes maior do que as casas que não possuem.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0897cec-6e2a-445e-92e2-8156219219a9/Untitled.png)

Além disso, cerca de 83% das casas com vista para água são nível 3 (maior da base de dados).

## Criação do app

O aplicativo foi criado visando dar aos diretores e time de vendas, uma forma mais acessível de consultar a base de dados, que possa filtrar as características que acharem interessante e ainda filtrar o imóvel desejado pelo id.

Por isso, ele foi pensado em ser algo simples, que facilitasse a experiência do usuário e trouxesse também as informações de preço, mapa e o overview geral do dataset.

## Resultados Financeiros

Os estudos indicaram que vender as casas durante o momento certo, ou seja, com valorização de 10%, irá manter um preço médio de U$ 594.091,87 por casa.

Se for mantida a mesma quantidade de casas vendidas por dia, o faturamento será de U$ 156.840.253,68, tendo um lucro de U$14.280.253,68.

## Conclusão

O resultado financeiro foi baseado apenas na valorização dos imóveis, contudo, o projeto entrega também insights que podem impulsionar vendas e criar novas estratégias de publicidade e segmentos de público alvo para a empresa.

Portanto, o projeto entregue garantiu o aumento da eficiência da empresa e uma solução simples e assertiva para seu negócio.

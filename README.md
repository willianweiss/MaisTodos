# Projeto MaisTodos API

  

Este projeto é uma API FastAPI para gerenciar informações de cartões de credito. Ele fornece endpoints para criar, e buscar dados de cartões. 

## Arquitetura

A API foi construída usando FastAPI e utiliza SQLAlchemy como ORM para interagir com o banco de dados. O projeto segue o padrão de arquitetura em camadas, separando claramente as rotas, os modelos e a lógica de negócios.

### Camadas

- Routes: Define os endpoints da API e suas funções relacionadas.

- Models: Define os modelos de dados e as tabelas do banco de dados.

- Schemas: Define os modelos de entrada/saída para a API.

- Database: Gerencia conexões e configurações do banco de dados.

  

### Melhores práticas utilizadas

  

- O projeto utiliza Alembic para migrações de banco de dados, facilitando a evolução da estrutura de dados.

- A aplicação está encapsulada em um container Docker, facilitando a implantação e garantindo a consistência do ambiente.

- O projeto utiliza Pytest para testes unitários e de integração.

- O código segue a padronização PEP8 e utiliza type hints para melhorar a legibilidade e auxiliar na detecção de erros.

- O código utiliza JWT para autenticação.

- O código possui 82% de cobertura de testes .  

## Pré-requisitos

- Docker

- Docker Compose

  

## Instalação

1. Clone este repositório:

`git clone https://github.com/willianweiss/MaisTodos

cd MaisTodos`


2. Construa a imagem Docker :
  
`make build`

3. Inicie os serviços:

`make up`

  

A API estará disponível na porta 8000: [http://localhost:8000/docs](http://localhost:8000/docs), lembrando de usar a rota login/ com username e password da .env para receber o token jwt de uso nas outras rotas.

## Uso

A API fornece os seguintes endpoints:


- POST /credit-card/: Cria um novo cartão de crédito.

- GET /credit-card/: Pega todos os cartões de crédito 

- GET /credit-card/{credit-card_id}: Pega o cartão de crédito pelo id.
  

## Testes

Para executar os testes, execute o seguinte comando no terminal:

`make test`


## Linting e formatação de código


Para verificar a formatação de código com black e isort, execute o seguinte comando no terminal:


`make lint`
  

## Verificar a cobertura de testes


Para verificar a cobertura de testes, execute o seguinte comando no terminal:


`make test-cov`
  

  

## Pipeline de Integração Contínua

  

Este projeto utiliza uma pipeline de Integração Contínua (CI) com Github Actions para executar as seguintes tarefas automaticamente a cada push:

  

- Execução de testes unitários e de integração com Pytest.

- Verificação de cobertura de testes com uma exigência mínima de 80%.

- Linting com black e isort.

- Verificações de segurança com bandit e safety.


## Licença

 
Este projeto está licenciado sob a licença MIT.
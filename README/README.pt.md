# Gerenciamento de Eventos API

Esta é uma aplicação em Python que permite o cadastro e gerenciamento de eventos e seus inscritos. A API foi construída com Flask e utiliza o SQLAlchemy para manipulação de dados no banco de dados. A aplicação segue boas práticas de desenvolvimento de APIs REST, utilizando o padrão de projeto com repository, interface e controller. Além disso, inclui validação de dados com Cerberus e testes automatizados com Pytest.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Flask**: Framework para criação da API REST
- **SQLAlchemy**: ORM para manipulação de banco de dados
- **Cerberus**: Biblioteca para validação de dados
- **Pytest**: Framework para testes automatizados
- **Postman**: Ferramenta para testar e validar rotas da API

## Funcionalidades

- Cadastro de eventos
- Atualização de dados de eventos
- Gerenciamento de inscritos
- Validação de dados de entrada
- Testes automatizados

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Rode o banco de dados (se necessário):
   ```bash
   python manage.py db upgrade
4. Inicie o servidor Flask:
   ```bash
   python app.py
5. Acesse a API no navegador ou no Postman:
   ```bash
   http://127.0.0.1:5000

## Testes
Os testes automatizados podem ser executados com Pytest:
```bash
pytest
```

### Contribuindo
Se você gostaria de contribuir para o desenvolvimento deste projeto, sinta-se à vontade para abrir issues ou pull requests.

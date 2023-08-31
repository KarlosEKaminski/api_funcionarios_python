<h1 align="center">API de Gerenciamento de Funcionários</h1>
<p align="center">Esta é uma simples API em Python para gerenciamento de funcionários, com suporte para operações CRUD (Create, Read, Update, Delete). A API permite que você adicione, leia, atualize e exclua informações de funcionários.</p>
<br>

## 🛠️ Funcionalidades

- **GET /funcionarios:** Retorna a lista de todos os funcionários.
- **GET /funcionarios/{id}:** Retorna os detalhes de um funcionário específico.
- **POST /funcionarios:** Adiciona um novo funcionário.
- **PUT /funcionarios/{id}:** Atualiza os detalhes de um funcionário existente.
- **DELETE /funcionarios/{id}:** Remove um funcionário.

## ⚙ Requisitos

- Python 3.x instalado em seu sistema.
- Biblioteca Flask instalada. Você pode instalar usando `pip install Flask`.

## 🏃‍♂️ Executando a API

1. Clone este repositório para o seu sistema, usando:
   ```git clone https://github.com/KarlosEKaminski/api_funcionarios_python.git```
3. Navegue até a pasta do repositório:
4. Execute o arquivo `app.py`:
5. A API estará acessível em `http://localhost:8080`.

## Exemplo de Uso

- **GET /funcionarios**
  - Retorna a lista de funcionários.
```
curl http://localhost:8080/funcionarios
```
- **GET /funcionarios/{id}:**
  - Retorna um funcionário pelo id.
```
curl http://localhost:8080/funcionarios/1
```
- **POST /funcionarios:**
  - Adiciona um funcionário.
```
curl -X POST -H "Content-Type: application/json" -d '{"id": 5, "nome": "Novo Funcionário", "email": "novo@example.com", "telefone": "1234567890"}' http://localhost:8080/funcionarios
```
- **PUT /funcionarios/{id}:**
  - Atualiza um funcionário pelo id.
```
curl -X PUT -H "Content-Type: application/json" -d '{"id": 5, "nome": "Funcionário Atualizado", "email": "atualizado@example.com", "telefone": "9876543210"}' http://localhost:8080/funcionarios/1
```
- **DELETE /funcionarios/{id}:**
  - Deleta um funcionário pelo id.
```
curl -X DELETE http://localhost:8080/funcionarios/1
```
## 📄 LICENÇA
Este projeto está sob a licença [MIT]()<br>
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
    

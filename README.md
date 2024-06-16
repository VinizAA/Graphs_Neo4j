# Neo4j Graph 

Script Python que interage com o banco de dados em grafo Neo4j

## Requisitos

- **Python 3+**
- **Conta no Neo4j Aura:** Crie uma instância gratuita no [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=nav-get-started-cta) para hospedar seu banco de dados
    - **IMPORTANTE: Faça download do arquivo .txt com as configurações do seu banco de dados**

  

## Instalação e execução

1. Clone o repositório
    ```bash
    git clone https://github.com/VinizAA/Graphs_Neo4j.git
    cd Graphs_Neo4j
    ```

2. Instale as dependências:
    ```bash
    pip install neo4j
    ```

3. Configure o banco de dados: Coloque o documento .txt baixado na pasta 'Graphs_Neo4j'
4. Altere o nome do arquivo de configuração no programa
    ```python
    file_path = "<file_name.txt>"
    ```

5. Execute o programa
    ```bash
    python3 connect_neo4j.py
    ```

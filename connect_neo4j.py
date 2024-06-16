from neo4j import GraphDatabase

def read_auth (file_path):  
    with open(file_path, 'r') as file:
        lines = file.readlines()

    uri = username = password = None

    for line in lines:
        if 'NEO4J_URI=' in line:
            uri = line.split('=')[1].strip()
        elif 'NEO4J_USERNAME=' in line:
            username = line.split('=')[1].strip()
        elif 'NEO4J_PASSWORD=' in line:
            password = line.split('=')[1].strip()
    
    return uri, username, password

def create_node(title, **properties):
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session(database="neo4j") as session:
                query = f"CREATE (:{title} {{"
                args = {}

                for key, value in properties.items():
                    query += f"{key}: ${key}, "
                    args[key] = value

                query = query.rstrip(", ") + "})"

                session.run(query, **args)

                print(f"NODE CREATED: {title}({properties})")
    except Exception as e:
        print(f"Error creating node: {e}")

def create_relationship(title, node1_name, node2_name, relation_type, direc):
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session(database="neo4j") as session:
                if direc == 1:              
                    query = f"MATCH ({title[0].lower()}1:{title} {{name: '{node1_name}'}})" \
                            f"MATCH ({title[0].lower()}2:{title} {{name: '{node2_name}'}})" \
                            f"CREATE ({title[0].lower()}1)-[{relation_type[0].lower()}:{relation_type}]->({title[0].lower()}2)" \
                            f"RETURN {title[0].lower()}1, {title[0].lower()}2"
                elif direc == 0:
                    query = f"MATCH ({title[0].lower()}1:{title} {{name: '{node1_name}'}})" \
                            f"MATCH ({title[0].lower()}2:{title} {{name: '{node2_name}'}})" \
                            f"CREATE ({title[0].lower()}1)-[{relation_type[0].lower()}1:{relation_type}]->({title[0].lower()}2)" \
                            f"CREATE ({title[0].lower()}2)-[{relation_type[0].lower()}2:{relation_type}]->({title[0].lower()}1)" \
                            f"RETURN {title[0].lower()}1, {title[0].lower()}2"
                session.run(query)
                print(f"RELATIONSHIP CREATED: {node1_name} - {node2_name} ({relation_type})")
    except Exception as e:
        print(f"Error creating relationship: {e}")

def delete_all_nodes():
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session(database="neo4j") as session:
                session.run("MATCH (n) DETACH DELETE n")
                print("ALL NODES AND RELATIONSHIPS DELETED!")
    except Exception as e:
        print(f"Error deleting all nodes: {e}")

def delete_nodes(title, node1_name, node2_name):
    try:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session(database="neo4j") as session:
                query = f"MATCH ({title[0].lower()}1:{title} {{name: '{node1_name}'}})" \
                        f"MATCH ({title[0].lower()}2:{title} {{name: '{node2_name}'}})" \
                        f"DETACH DELETE {title[0].lower()}1, {title[0].lower()}2"
                session.run(query)
                print(f"NODES ({node1_name.upper()}) AND ({node2_name.upper()}) AND YOUR RELATIONSHIPS WERE DELETED!")
    except Exception as e:
        print(f"Error deleting nodes: {e}")


file_path = "Neo4j-528321e5.txt" #altere para o nome do arquivo .txt que foi baixado
URI, USERNAME, PASSWORD = read_auth(file_path)
AUTH = (USERNAME, PASSWORD)





from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_partidas.sql") as f:
            self.query_relatorio_partidas = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_scouts_partida.sql") as f:
            self.query_relatorio_scouts_partida = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_atletas.sql") as f:
            self.query_relatorio_atletas = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_time.sql") as f:
            self.query_relatorio_time = f.read()

    def get_relatorio_partidas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_partidas))
        input("Pressione Enter para Sair do Relatório de Partidas")

    def get_relatorio_scouts_partida(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_scouts_partida))
        input("Pressione Enter para Sair do Relatório de Scouts Partida")

    def get_relatorio_atletas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_atletas))
        input("Pressione Enter para Sair do Relatório de Atletas")

    def get_relatorio_time(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_time))
        input("Pressione Enter para Sair do Relatório de Times")
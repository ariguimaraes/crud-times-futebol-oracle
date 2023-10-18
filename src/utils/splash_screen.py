from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_scouts_partida = config.QUERY_COUNT.format(tabela="scouts_partida")
        self.qry_total_atletas = config.QUERY_COUNT.format(tabela="atletas")
        self.qry_total_partidas = config.QUERY_COUNT.format(tabela="partidas")
        self.qry_total_time = config.QUERY_COUNT.format(tabela="time")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Ari Guimarães, Gabriel Fischer, João Victor Trarbach e Pedro Arthur Kuster"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_scouts_partida(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_scouts_partida)["total_scouts_partida"].values[0]

    def get_total_atletas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_atletas)["total_atletas"].values[0]

    def get_time(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_time)["total_time"].values[0]

    def get_total_partidas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_partidas)["total_partidas"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE GERENCIAMENTO FUTEBOL                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - SCOUTS PARTIDA:      {str(self.get_total_scouts_partida()).rjust(5)}
        #      2 - ATLETAS:             {str(self.get_total_atletas()).rjust(5)}
        #      3 - PARTIDAS:            {str(self.get_total_partidas()).rjust(5)}
        #      4 - TIMES:               {str(self.get_total_time()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
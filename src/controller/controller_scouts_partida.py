from model.scouts_partidas import Scouts_Partida
from conexion.oracle_queries import OracleQueries

class Controller_Scouts_Partida:
    def __init__(self):
        pass
        
    def inserir_scouts_partida(self) -> Scouts_Partida:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sk_partida = input("SK_Partida (Novo): ")

        if self.verifica_existencia_partida(oracle, sk_partida):
            quantidade = input("Quantidade (Nova): ")
            cartao_vermelho = input("Cartões Vermelhos (Novo): ")
            cartao_amarelo = input("Cartões Amarelos (Novo): ")
            faltas = input("Faltas (Novo): ")
            laterais = input("Laterais (Novo): ")
            escanteios = input("Escanteios (Novo): ")
            gols = input("Gols (Novo): ")
            assistencias = input("Assistências (Novo): ")
            oracle.write(f"insert into scouts_partida values ('{sk_partida}, '{quantidade}', '{cartao_vermelho}', '{cartao_amarelo}', '{faltas}', '{laterais}', '{escanteios}', '{gols}', '{assistencias}')")
            df_scouts_partida = oracle.sqlToDataFrame(f"select sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias from scouts_partida where sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias ='{sk_partida}', '{quantidade}', '{cartao_vermelho}', '{cartao_amarelo}', '{faltas}', '{laterais}', '{escanteios}', '{gols}', '{assistencias}'")
            novo_scouts_partida = Scouts_Partida(df_scouts_partida.sk_partida.values[0], df_scouts_partida.quantidade.values[0], df_scouts_partida.cartao_vermelho.values[0], df_scouts_partida.cartao_amarelo.values[0], df_scouts_partida.faltas.values[0], df_scouts_partida.laterais.values[0], df_scouts_partida.escanteios.values[0], df_scouts_partida.gols.values[0], df_scouts_partida.assistencias.values[0])
            print(novo_scouts_partida.to_string())
            return novo_scouts_partida
        else:
            print(f"O SK_Partida {sk_partida} já está cadastrado.")
            return None

    def atualizar_scouts_partida(self) -> Scouts_Partida:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sk_partida = int(input("SK_Partida que deseja alterar: "))

        if not self.verifica_existencia_partida(oracle, sk_partida):
            novo_quantidade = input("Quantidade (Nova): ")
            novo_cartao_vermelho = input("Cartões Vermelhos (Novo): ")
            novo_cartao_amarelo = input("Cartões Amarelos (Novo): ")
            novo_faltas = input("Faltas (Novo): ")
            novo_laterais = input("Laterais (Novo): ")
            novo_escanteios = input("Escanteios (Novo): ")
            novo_gols = input("Gols (Novo): ")
            novo_assistencias = input("Assistências (Novo): ")
            oracle.write(f"update scouts_partida set quantidade = '{novo_quantidade}', cartao_vermelho = '{novo_cartao_vermelho}', cartao_amarelo = '{novo_cartao_amarelo}', faltas = '{novo_faltas}', laterais = '{novo_laterais}', escanteios = '{novo_escanteios}', gols = '{novo_gols}', assistencias = '{novo_assistencias}', where sk_partida = {sk_partida}")
            df_scouts_partida = oracle.sqlToDataFrame(f"select sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias from scouts_partida where sk_partida = {sk_partida}")
            scouts_partida_atualizado = Scouts_Partida(df_scouts_partida.sk_partida.values[0], df_scouts_partida.quantidade.values[0], df_scouts_partida.cartao_vermelho.values[0], df_scouts_partida.cartao_amarelo.values[0], df_scouts_partida.faltas.values[0], df_scouts_partida.laterais.values[0], df_scouts_partida.escanteios.values[0], df_scouts_partida.gols.values[0], df_scouts_partida.assistencias.values[0])
            print(scouts_partida_atualizado.to_string())
            return scouts_partida_atualizado
        else:
            print(f"O SK_Partida {sk_partida} não existe.")
            return None

    def excluir_scouts_partida(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sk_partida = int(input("SK_Partida que irá excluir: "))        

        if not self.verifica_existencia_partida(oracle, sk_partida):            
            df_scouts_partida = oracle.sqlToDataFrame(f"select sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias from scouts_partida where sk_partida = {sk_partida}")
            oracle.write(f"delete from scouts_partida where sk_partida = {sk_partida}")            
            scouts_partida_excluido = Scouts_Partida(df_scouts_partida.sk_partida.values[0], df_scouts_partida.quantidade.values[0], df_scouts_partida.cartao_vermelho.values[0], df_scouts_partida.cartao_amarelo.values[0], df_scouts_partida.faltas.values[0], df_scouts_partida.laterais.values[0], df_scouts_partida.escanteios.values[0], df_scouts_partida.gols.values[0], df_scouts_partida.assistencias.values[0])
            print("SK_Partida Removido com Sucesso!")
            print(scouts_partida_excluido.to_string())
        else:
            print(f"O SK_Partida {sk_partida} não existe.")

    def verifica_existencia_scouts_partida(self, oracle:OracleQueries, sk_partida:int=None) -> bool:
        df_scouts_partida = oracle.sqlToDataFrame(f"select sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias, from scouts_partida where sk_partida = {sk_partida}")
        return df_scouts_partida.empty
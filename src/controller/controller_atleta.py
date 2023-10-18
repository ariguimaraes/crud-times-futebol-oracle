from pydoc import cli
from model.atletas import Atleta
from model.scouts_partidas import Scouts_Partida
from controller.controller_scouts_partida import Controller_Scouts_Partida
from conexion.oracle_queries import OracleQueries
from model.scouts_partidas import get_sk_partida

class Controller_Atleta:
    def __init__(self):
        self.ctrl_scouts_partida = Controller_Scouts_Partida()
        
    def inserir_partida(self) -> Atleta:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        oracle = OracleQueries()
        
        self.listar_scouts_partida(oracle, need_connect=True)
        sk_partida = int(input("Digite o número do SK_Partida: "))
        scouts_partida = self.valida_scouts_partida(oracle, sk_partida)
        if scouts_partida == None:
            return None

        cursor = oracle.connect()
        output_value = cursor.var(int)

        atleta = dict(codigo_atleta=output_value, sk_atletas=atletas.get_sk_atletas, nome=atletas.get_nome, numero=atletas.get_numero, posicao=atletas.get_posicao, cartao_amarelo=atletas.get_cartao_amarelo, cartao_vermelho=atletas.get_cartao_vermelho, descricao=atletas.get_descricao, sk_times=atletas.get_sk_times, sk_partida=scouts_partida.get_sk_partida())
        cursor.execute("""
        begin
            :codigo_atleta := ATLETAS_CODIGO_ATLETA_SEQ.NEXTVAL;
            insert into atletas values(:sk_atletas, :nome, :numero, :posicao, :cartao_amarelo, :cartao_vermelho, :descricao, :sk_times, :sk_partida);
        end;
        """, atleta)
        codigo_atleta = output_value.getvalue()
        oracle.conn.commit()
        df_atleta = oracle.sqlToDataFrame(f"select codigo_atleta, sk_atletas, nome, numero, posicao, cartao_amarelo, cartao_vermelho, descricao, sk_times, sk_partida from atletas where codigo_atleta = '{codigo_atleta}', '{sk_atleta}', '{nome}', '{numero}', '{posicao}', '{cartao_amarelo}', '{cartao_vermelho}', '{descricao}', '{sk_times}', '{sk_partida}'")
        novo_atleta = Atleta(df_atleta.codigo_atleta.values[0], df_atleta.sk_atletas.values[0], df_atleta.nome.values[0], df_atleta.numero.values[0], df_atleta.posicao.values[0], df_atleta.cartao_amarelo.values[0], df_atleta.cartao_vermelho.values[0], df_atleta.descricao.values[0], df_atleta.sk_times.values[0], scouts_partida)
        print(novo_atleta.to_string())
        return novo_atleta

    def atualizar_atleta(self) -> Atleta:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_atleta = int(input("Código do atleta que irá alterar: "))        

        if not self.verifica_existencia_atleta(oracle, codigo_atleta):

            self.listar_scouts_partida(oracle)
            sk_partida = int(input("Digite o número do SK_Partida: "))
            scouts_partida = self.valida_scouts_partida(oracle, sk_partida)
            if scouts_partida == None:
                return None

            oracle.write(f"update atletas set sk_partida = '{scouts_partida.get_sk_partida()}', sk_atletas = '{atletas.get_sk_atletas()}', nome = '{atletas.get_nome()}',  numero = '{atletas.get_numero()}',  posicao = '{atletas.get_posicao()}',  cartao_amarelo = '{atletas.get_cartao_amarelo()}',  cartao_vermelho = '{atletas.get_cartao_vermelho()}',  descricao = '{atletas.get_descricao()}',  sk_times = '{atletas.get_sk_times()}',  sk_partida = '{scouts_partida.get_sk_partida()}') where codigo_atleta = {codigo_atleta}")
            df_atleta = oracle.sqlToDataFrame(f"select codigo_atleta, sk_atletas, nome, numero, posicao, cartao_amarelo, cartao_vermelho, descricao, sk_times, sk_partida from atletas where codigo_atleta = '{codigo_atleta}', '{sk_atleta}', '{nome}', '{numero}', '{posicao}', '{cartao_amarelo}', '{cartao_vermelho}', '{descricao}', '{sk_times}', '{sk_partida}'")
            atleta_atualizado = Atleta(df_atleta.codigo_atleta.values[0], df_atleta.sk_atletas.values[0], df_atleta.nome.values[0], df_atleta.numero.values[0], df_atleta.posicao.values[0], df_atleta.cartao_amarelo.values[0], df_atleta.cartao_vermelho.values[0], df_atleta.descricao.values[0], df_atleta.sk_times.values[0], scouts_partida)
            print(atleta_atualizado.to_string())
            return atleta_atualizado
        else:
            print(f"O código {codigo_atleta} não existe.")
            return None

    def excluir_atleta(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_atleta = int(input("Código do atleta que irá excluir: "))        

        if not self.verifica_existencia_atleta(oracle, codigo_atleta):            
            df_atleta = oracle.sqlToDataFrame(f"select codigo_atleta, sk_atletas, nome, numero, posicao, cartao_amarelo, cartao_vermelho, descricao, sk_times, sk_partida from atletas where codigo_atleta = '{codigo_atleta}', '{sk_atleta}', '{nome}', '{numero}', '{posicao}', '{cartao_amarelo}', '{cartao_vermelho}', '{descricao}', '{sk_times}', '{sk_partida}'")
            scouts_partida = self.valida_scouts_partida(oracle, df_atleta.sk_partida.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o código do atleta {codigo_atleta} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o atleta possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir a partida {codigo_atleta} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                    oracle.write(f"delete from scouts_partida where codigo_atleta = {codigo_atleta}")
                    print("Itens do atleta removidos com sucesso!")
                    oracle.write(f"delete from atletas where codigo_atleta = {codigo_atleta}")
                    atleta_excluido = Atleta(df_atleta.codigo_atleta.values[0], df_atleta.sk_atletas.values[0], df_atleta.nome.values[0], df_atleta.numero.values[0], df_atleta.posicao.values[0], df_atleta.cartao_amarelo.values[0], df_atleta.cartao_vermelho.values[0], df_atleta.descricao.values[0], df_atleta.sk_times.values[0], scouts_partida)
                    print("Atleta Removido com Sucesso!")
                    print(atleta_excluido.to_string())
        else:
            print(f"O código {codigo_atleta} não existe.")

    def verifica_existencia_atleta(self, oracle:OracleQueries, codigo:int=None) -> bool:
        df_atleta = oracle.sqlToDataFrame(f"select codigo_atleta, sk_atletas, nome, numero, posicao, cartao_amarelo, cartao_vermelho, descricao, sk_times, sk_partida from atletas where codigo_atleta = '{codigo_atleta}', '{sk_atleta}', '{nome}', '{numero}', '{posicao}', '{cartao_amarelo}', '{cartao_vermelho}', '{descricao}', '{sk_times}', '{sk_partida}'")
        return df_atleta.empty

    def listar_scouts_partida(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select s.sk_partida
                    , s.quantidade
                    , s.cartao_vermelho
                    , s.cartao_amarelo
                    , s.faltas
                    , s.laterais
                    , s.escanteios
                    , s.gols
                    , s.assistencias
                from scouts_partida s
                order by s.quantidade
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))


    def valida_scouts_partida(self, oracle:OracleQueries, sk_partida:int=None) -> Scouts_Partida:
        if self.ctrl_scouts_partida.verifica_existencia_scouts_partida(oracle, sk_partida):
            print(f"O SK_Partida {sk_partida} informado não existe na base.")
            return None
        else:
            oracle.connect()
            df_scouts_partida = oracle.sqlToDataFrame(f"select sk_partida, quantidade, cartao_vermelho, cartao_amarelo, faltas, laterais, escanteios, gols, assistencias, from scouts_partida where sk_partida = {sk_partida}")
            scouts_partida = Scouts_Partida(df_scouts_partida.sk_partida.values[0], df_scouts_partida.quantidade.values[0], df_scouts_partida.cartao_vermelho.values[0], df_scouts_partida.cartao_amarelo.values[0], df_scouts_partida.faltas.values[0], df_scouts_partida.laterais.values[0], df_scouts_partida.escanteios.values[0], df_scouts_partida.gols.values[0], df_scouts_partida.assistencias.values[0])
            return scouts_partida
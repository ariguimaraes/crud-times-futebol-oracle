from pydoc import cli
from model.partidas import Partida
from model.scouts_partidas import Scouts_Partida
from controller.controller_partida import Controller_Partida
from model.atletas import Atleta
from controller.controller_atleta import Controller_Atleta
from model.times import Time
from conexion.oracle_queries import OracleQueries

class Controller_Time:
    def __init__(self):
        self.ctrl_partida = Controller_Partida()
        self.ctrl_atleta = Controller_Atleta()
        
    def inserir_time(self) -> Time:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        oracle = OracleQueries()
        
        self.listar_partidas(oracle, need_connect=True)
        sk_partida = int(input("Digite o número da partida: "))
        partidas = self.valida_partida(oracle, sk_partida)
        if partidas == None:
            return None

        self.listar_atletas(oracle, need_connect=True)
        sk_atletas = int(input("Digite o número do atleta: "))
        atletas = self.valida_fornecedor(oracle, sk_atletas)
        if atletas == None:
            return None

        cursor = oracle.connect()
        output_value = cursor.var(int)

        time = dict(codigo_time=output_value, nome=time.get_nome, cores=time.get_cores, treinador=time.get_treinador, sk_partida=partidas.get_sk_partida(), sk_times=atletas.get_sk_times())
        cursor.execute("""
        begin
            :codigo_time := TIME_CODIGO_TIME_SEQ.NEXTVAL;
            insert into time values(:nome, :cores, :treinador, :sk_partida, :sk_times);
        end;
        """, time)
        codigo_time = output_value.getvalue()
        oracle.conn.commit()
        df_time = oracle.sqlToDataFrame(f"select codigo_time, nome, cores, treinador, sk_partida, sk_times from times where codigo_time = {codigo_time}, {nome}, {cores}, {treinador}, {sk_partida}, {sk_times},")
        novo_time = Time(df_time.codigo_time.values[0], df_time.nome.values[0], df_time.cores.values[0], df_time.treinador.values[0], partidas, atletas)
        print(novo_time.to_string())
        return novo_time

    def atualizar_time(self) -> Time:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_time = int(input("Código do time que irá alterar: "))        

        if not self.verifica_existencia_time(oracle, codigo_time):

            self.listar_partidas(oracle)
            sk_partida = int(input("Digite o número da partida: "))
            partidas = self.valida_partida(oracle, sk_partida)
            if partidas == None:
                return None

            self.listar_atletas(oracle)
            sk_atletas = int(input("Digite o número do atleta: "))
            atletas = self.valida_fornecedor(oracle, sk_atletas)
            if atletas == None:
                return None

            oracle.write(f"update times set sk_partida = '{partidas.get_sk_partida()}', sk_atletas = '{atletas.get_sk_atletas()}', nome = '{times.get_nome()}', cores = '{times.get_cores()}', treinador = '{times.get_treinador()}' where codigo_time = {codigo_time}")
            df_time = oracle.sqlToDataFrame(f"select codigo_time, nome, cores, treinador, sk_partida, sk_times from times where codigo_time = {codigo_time}, {nome}, {cores}, {treinador}, {sk_partida}, {sk_times},")
            time_atualizado = Time(df_time.codigo_time.values[0], df_time.nome.values[0], df_time.cores.values[0], df_time.treinador.values[0], partidas, atletas)
            print(time_atualizado.to_string())
            return time_atualizado
        else:
            print(f"O código {codigo_time} não existe.")
            return None

    def excluir_time(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_time = int(input("Código do time que irá excluir: "))        

        if not self.verifica_existencia_time(oracle, codigo_time):            
            df_time = oracle.sqlToDataFrame(f"select codigo_time, nome, cores, treinador, sk_partida, sk_times from times where codigo_time = {codigo_time}, {nome}, {cores}, {treinador}, {sk_partida}, {sk_times},")
            partida = self.valida_partida(oracle, df_time.sk_partida.values[0])
            atleta = self.valida_atleta(oracle, df_time.sk_atletas.values[0])
            
            opcao_excluir = input(f"Tem certeza que deseja excluir o time {codigo_time} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                print("Atenção, caso o time possua itens, também serão excluídos!")
                opcao_excluir = input(f"Tem certeza que deseja excluir o time {codigo_time} [S ou N]: ")
                if opcao_excluir.lower() == "s":
                    oracle.write(f"delete from time where codigo_time = {codigo_time}")
                    print("Itens do time removidos com sucesso!")
                    oracle.write(f"delete from partidas where codigo_time = {codigo_time}")
                    time_excluido = Time(df_time.codigo_time.values[0], df_time.nome.values[0], df_time.cores.values[0], df_time.treinador.values[0], partidas, atletas)
                    print("Time Removido com Sucesso!")
                    print(time_excluido.to_string())
        else:
            print(f"O código {codigo_time} não existe.")

    def verifica_existencia_time(self, oracle:OracleQueries, codigo_time:int=None) -> bool:
        df_time = oracle.sqlToDataFrame(f"select codigo_time, nome, cores, treinador, sk_partida, sk_times from times where codigo_time = {codigo_time}, {nome}, {cores}, {treinador}, {sk_partida}, {sk_times},")
        return df_time.empty

    def listar_partidas(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select p.sk_partida
                    , p.time_casa 
                    , p.time_visitante
                    , p.gols_pro
                    , p.gols_contra
                    , p.arbitro
                    , p.estadio
                from partidas p
                order by p.time_casa
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_atletas(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select a.sk_atletas
                    , a.nome
                    , a.numero
                    , a.posicao
                    , a.cartao_amarelo
                    , a.cartao_vermelho
                    , a.descricao
                    , a.sk_partida
                    , a.sk_times
                from atletas a
                order by a.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_partida(self, oracle:OracleQueries, sk_partida:int=None) -> Partida:
        if self.ctrl_partida.verifica_existencia_partida(oracle, sk_partida):
            print(f"O SK_Partida {sk_partida} informado não existe na base.")
            return None
        else:
            oracle.connect()
            df_partida = oracle.sqlToDataFrame(f"select codigo_partida, time_casa, time_visitante, gols_pro, gols_contra, arbitro, estadio, sk_partida from partidas where codigo_partida = '{codigo_partida}', '{time_casa}', '{time_visitante}', '{gols_pro}', '{gols_contra}', '{arbitro}', '{estadio}', '{sk_partida}'")
            partida = Partida(df_partida.codigo_partida.values[0], df_partida.time_casa.values[0], df_partida.time_visitante.values[0], df_partida.gols_pro.values[0], df_partida.gols_contra.values[0], df_partida.arbitro.values[0], df_partida.estadio.values[0], scouts_partida)
            return partida

    def valida_atleta(self, oracle:OracleQueries, sk_atletas:int=None) -> Atleta:
        if self.ctrl_atleta.verifica_existencia_fornecedor(oracle, sk_atletas):
            print(f"O código de atleta {sk_atletas} informado não existe na base.")
            return None
        else:
            oracle.connect()
            df_atleta = oracle.sqlToDataFrame(f"select codigo_atleta, sk_atletas, nome, numero, posicao, cartao_amarelo, cartao_vermelho, descricao, sk_times, sk_partida from atletas where codigo_atleta = '{codigo_atleta}', '{sk_atleta}', '{nome}', '{numero}', '{posicao}', '{cartao_amarelo}', '{cartao_vermelho}', '{descricao}', '{sk_times}', '{sk_partida}'")
            atleta = Atleta(df_atleta.codigo_atleta.values[0], df_atleta.sk_atletas.values[0], df_atleta.nome.values[0], df_atleta.numero.values[0], df_atleta.posicao.values[0], df_atleta.cartao_amarelo.values[0], df_atleta.cartao_vermelho.values[0], df_atleta.descricao.values[0], df_atleta.sk_times.values[0], scouts_partida)
            return atleta
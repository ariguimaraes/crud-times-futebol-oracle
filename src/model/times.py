from model.partidas import Partida

class Time:
  def __init__(self,
               sk_times: int=None,
               nome: str=None,
               cores: int=None,
               treinador: str=None,
               sk_partida: Partida=None
               ):
    self.set_sk_times(sk_times)
    self.set_nome(nome)
    self.set_cores(cores)
    self.set_treinador(treinador)
    self.set_sk_partida(sk_partida)

  def set_sk_times(self, sk_times:int):
    self.sk_times = sk_times

  def set_nome(self, nome:str):
    self.nome = nome

  def set_cores(self, cores:int):
    self.cores = cores

  def set_treinador(self, treinador:str):
    self.treinador = treinador

  def set_sk_partida(self, sk_partida:Partida):
    self.sk_partida = sk_partida

  def get_sk_times(self) -> int:
    return self.sk_times

  def get_nome(self) -> str:
    return self.nome

  def get_cores(self) -> int:
    return self.cores

  def get_treinador(self) -> str:
    return self.treinador

  def get_sk_partida(self) -> Partida:
    return self.sk_partida

  def to_string(self):
    return f'Time: {self.get_sk_times()} | Nome: {self.get_nome()} | Cores: {self.get_cores()} | Treinador: {self.get_treinador()} | Partida: {self.get_sk_partida(),get_sk_partida()}'

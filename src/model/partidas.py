from model.scouts_partidas import Scouts_Partida
from model.scouts_partida import get_sk_atleta

class Partida:
  def __init__(self, 
                sk_partida:int=None,
                time_casa:int=None,
                time_visitante:int=None,
                gols_pro:int=None,
                gols_contra:int=None,
                arbitro:str=None,
                estadio:str=None,
                sk_partidas:Scouts_Partida=None,
                sk_atleta:Scouts_Partida=None
                ):
    self.set_sk_partida(sk_partida)
    self.set_time_casa(time_casa)
    self.set_time_visitante(time_visitante)
    self.set_gols_pro(gols_pro)
    self.set_gols_contra(gols_contra)
    self.set_arbitro(arbitro)
    self.set_estadio(estadio)
    self.set_sk_partidas(sk_partidas)
    self.set_sk_atleta(sk_atleta)

  def set_sk_partida(self, sk_partida:int):
    self.sk_partida = sk_partida

  def set_time_casa(self, time_casa:int):  
    self.time_casa = time_casa

  def set_time_visitante(self, time_visitante:int):
    self.time_visitante = time_visitante

  def set_gols_pro(self, gols_pro:int):
    self.gols_pro = gols_pro

  def set_gols_contra(self, gols_contra:int):
    self.gols_contra = gols_contra

  def set_arbitro(self, arbitro:str):
    self.arbitro = arbitro

  def set_estadio(self, estadio:str):
    self.estadio = estadio

  def set_sk_atleta(self, sk_atleta:Scouts_Partida):
    self.sk_atleta = sk_atleta

  def set_sk_partidas(self, sk_partidas:Scouts_Partida):
    self.sk_partidas = sk_partidas

  def get_sk_partida(self) -> int:
    return self.sk_partida

  def get_time_casa(self) -> int:
    return self.time_casa

  def get_time_visitante(self) -> int:
    return self.time_visitante

  def get_gols_pro(self) -> int:
    return self.gols_pro

  def get_gols_contra(self) -> int:
    return self.gols_contra

  def get_arbitro(self) -> str:
    return self.arbitro

  def get_estadio(self) -> str:
    return self.estadio

  def get_sk_atleta(self) -> Scouts_Partida:
    return self.sk_atleta

  def get_sk_partidas(self) -> Scouts_Partida:
    return self.sk_partidas

  def to_strig(self):
    return f'Partida: {self.get_sk_partida()} | Time Casa: {self.get_time_casa()} | Time Visitante: {self.get_time_visitante()} | Gols Pro: {self.get_gols_pro()} | Gols Contra: {self.get_gols_contra()} | Arbitro: {self.get_arbitro()} | Estádio: {self.get_estadio()} | Atletas: {self.get_sk_atleta(),get_sk_atleta()} | Partida: {self.get_sk_partidas().get_sk_partida()}'


from model.scouts_partida import Scouts_Partida

class Partida:
  def __init__(self, 
                sk_partida:int= None,
                time_casa:int= None,
                time_visitante:int= None,
                gols_pro:int= None,
                gols_contra:int= None,
                arbitro:str= None,
                estadio:str= None,
                scouts_partida:Scouts_Partida= None
                ):
    self.set_sk_partida(sk_partida)
    self.set_time_casa(time_casa)
    self.set_time_visitante(time_visitante)
    self.set_gols_pro(gols_pro)
    self.set_gols_contra(gols_contra)
    self.set_arbitro(arbitro)
    self.set_estadio(estadio)
    self.set_scouts_partida(scouts_partida)

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

  def set_scouts_partida(self, scouts_partida:Scouts_Partida):
    self.scouts_partida = scouts_partida

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

  def get_scouts_partida(self) -> Scouts_Partida:
    return self.scouts_partida

  def to_strig(self):
    return f"Partida: {self.get_sk_partida()} | Time Casa: {self.get_time_casa()} | Time Visitante: {self.get_time_visitante()} | Gols Pro: {self.get_gols_pro()} | Gols Contra: {self.get_gols_contra()} | Arbitro: {self.get_arbitro()} | Estádio: {self.get_estadio()} |Partida: {self.get_scouts_partida().get_sk_partida()}"

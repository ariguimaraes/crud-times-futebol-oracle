class Scouts_Partida:

  def __init__(self,
               sk_partida: int = None,
               quantidade: int = None,
               cartao_vermelho: int = None,
               cartao_amarelo: int = None,
               faltas: int = None,
               laterias: int = None,
               escanteios: int = None,
               gols: int = None,
               assistencias: int = None):
    self.set_sk_partida(sk_partida)
    self.set_quantidade(quantidade)
    self.set_cartao_vermelho(cartao_vermelho)
    self.set_cartao_amarelo(cartao_amarelo)
    self.set_faltas(faltas)
    self.set_laterais(laterais)
    self.set_escanteios(escanteios)
    self.set_gols(gols)
    self.set_assistencia(assistencias)


def set_sk_partida(self, sk_partida: int):
  self.sk_partida = sk_partida


def set_quantidade(self, quantidade: int):
  self.quantidade = quantidade


def set_cartao_vermelho(self, cartao_vermelho: int):
  self.cartao_vermelho = cartao_vermelho


def set_cartao_amarelo(self, cartao_amarelo: int):
  self.cartao_amarelo = cartao_amarelo


def set_faltas(self, faltas: int):
  self.faltas = faltas


def set_laterais(self, laterias: int):
  self.laterias = laterias


def set_escanteios(self, escanteios: int):
  self.escanteios = escanteios


def set_gols(self, gols: int):
  self.gols = gols


def set_assistencia(self, assistencias: int):
  self.assistencias = assistencias


def get_sk_partida(self) -> int:
  return self.sk_partida


def get_sk_atleta(self) -> str:
  return self.sk_atleta


def get_quantidade(self) -> int:
  return self.quantidade


def get_cartao_vermelho(self) -> int:
  return self.cartao_vermelho


def get_cartao_amarelo(self) -> int:
  return self.cartao_amarelo


def get_faltas(self) -> int:
  return self.faltas


def get_laterais(self) -> int:
  return self.laterias


def get_escanteios(self) -> int:
  return self.escanteios


def get_gols(self) -> int:
  return self.gols


def get_assistencia(self) -> int:
  return self.assistencias


def to_string(self):
  return f'Partida: {self.get_sk_partida()} | Atleta: {self.get_sk_atleta()} | Quant: {self.get_quantidade()} | Vermelho: {self.get_cartao_vermelho()} | Amarelo: {self.get_cartao_amarelo()} | Faltas: {self.get_faltas()} | Laterais: {self.get_laterais()} | Escanteios: {self.get_escanteios()} | Gols: {self.get_gols()} | Ass: {self.get_assistencia()}'

from model.scouts_partidas import Scouts_Partida

class Atleta:
  def __init__(self,
              sk_atletas: int=None,
              nome: str=None,
              numero: int=None,
              posicao: str=None,
              cartao_amarelo: int=None,
              cartao_vermelho: int=None,
              descricao: str=None,
              scouts_partida:Scouts_Partida= None,
              sk_times: int=None
              ):
    self.set_sk_atletas(sk_atletas)
    self.set_nome(nome)
    self.set_numero(numero)
    self.set_posicao(posicao)
    self.set_cartao_amarelo(cartao_amarelo)
    self.set_cartao_vermelho(cartao_vermelho)
    self.set_descricao(descricao)
    self.set_scouts_partida(scouts_partida)
    self.set_sk_times(sk_times)

  def set_sk_atletas(self, sk_atletas: int):
    self.sk_atletas = sk_atletas

  def set_nome(self, nome: str):
    self.nome = nome

  def set_numero(self, numero: int):
    self.numero = numero

  def set_posicao(self, posicao: str):
    self.posicao = posicao

  def set_cartao_amarelo(self, cartao_amarelo: int):
    self.cartao_amarelo = cartao_amarelo

  def set_cartao_vermelho(self, cartao_vermelho: int):
    self.cartao_vermelho = cartao_vermelho

  def set_descricao(self, descricao: str):
    self.descricao = descricao

  def set_scouts_partida(self, scouts_partida:Scouts_Partida):
    self.scouts_partida = scouts_partida

  def set_sk_times(self, sk_times: int):
    self.sk_times = sk_times

  def get_sk_atletas(self) -> int:
    return self.sk_atletas

  def get_nome(self) -> str:
    return self.nome

  def get_numero(self) -> int:
    return self.numero

  def get_posicao(self) -> str:
    return self.posicao

  def get_cartao_amarelo(self) -> int:
    return self.cartao_amarelo

  def get_cartao_vermelho(self) -> int:
    return self.cartao_vermelho

  def get_descricao(self) -> str:
    return self.descricao

  def get_scouts_partida(self) -> Scouts_Partida:
    return self.scouts_partida

  def get_sk_times(self) -> int:
    return self.sk_times

  def to_string(self):
    return f"Id Atleta: {self.get_sk_atletas()} | Nome: {self.get_nome()} | Número: {self.get_numero()} | Posição: {self.get_posicao()} | Cartões Amarelos: {self.get_cartao_amarelo()} | Cartões Vermelhos: {self.get_cartao_vermelho()} | Descrição: {self.get_descricao()} | Id Partida: {self.get_scouts_partida().get_sk_partida()} | Id Time: {self.get_sk_times().get_sk_times()}"

from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_scouts_partida import Controller_Scouts_Partida
from controller.controller_atleta import Controller_Atleta
from controller.controller_partidas import Controller_Partida
from controller.controller_time import Controller_Time

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_scouts_partida = Controller_Scouts_Partida()
ctrl_atleta = Controller_Atleta()
ctrl_scouts_partidas = Controller_Partida()
ctrl_time = Controller_Time()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_partidas()          
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_scouts_partida()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_atletas()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_time()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_scouts_partida = ctrl_scouts_partida.inserir_scouts_partida()
    elif opcao_inserir == 2:
        novo_atleta = ctrl_atleta.inserir_atleta()
    elif opcao_inserir == 3:
        nova_partida = ctrl_partida.inserir_partida()
    elif opcao_inserir == 4:
        novo_time = ctrl_time.inserir_time()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_scouts_partida()
        scouts_partida_atualizado = ctrl_scouts_partida.atualizar_scouts_partida()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_atletas()
        fornecedor_atualizado = ctrl_atleta.atualizar_atleta()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_partidas()
        pedido_atualizado = ctrl_partida.atualizar_partida()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_time()
        item_pedido_atualizado = ctrl_time.atualizar_time()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_scouts_partida()
        ctrl_scouts_partida.excluir_scouts_partida()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_atletas()
        ctrl_atleta.excluir_atleta()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_partidas()
        ctrl_partida.excluir_partida()
    elif opcao_excluir == 4:
        relatorio.get_relatorio_time()
        ctrl_time.excluir_time()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
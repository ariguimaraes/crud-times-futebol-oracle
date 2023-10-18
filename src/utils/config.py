MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Partidas
2 - Relatório de Scouts Partida
3 - Relatório de Atletas
4 - Relatório de Times
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - Scouts Partida
2 - Atletas
3 - Partidas
4 - Times
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")
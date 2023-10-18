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
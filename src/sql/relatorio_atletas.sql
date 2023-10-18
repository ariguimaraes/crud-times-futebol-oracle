select a.sk_atletas
                    , a.nome
                    , a.numero
                    , a.posicao
                    , a.cartao_amarelo
                    , a.cartao_vermelho
                    , a.descricao
                    , a.sk_partida
                    , a.sk_times
                    , s.sk_partidas as scouts_partida
                from atletas a
                inner join scouts_partida s
                on a.sk_partida = s.sk_partida
                order by s.scouts_partida
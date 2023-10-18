select p.sk_partida
                    , p.time_casa 
                    , p.time_visitante
                    , p.gols_pro
                    , p.gols_contra
                    , p.arbitro
                    , p.estadio
                    , s.sk_partida as scouts_partida
                from partidas p
                inner join scouts_partida s
                on p.sk_partida = s.sk_partida
                order by s.scouts_partida
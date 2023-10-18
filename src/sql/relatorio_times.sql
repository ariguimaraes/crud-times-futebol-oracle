select t.sk_times
     , t.nome
     , t.cores
     , t.treinador
     , p.sk_partida as partidas
     , a.sk_times as atletas
     from time t
     inner join atletas a
     on t.sk_times = a.sk_times
     inner join partidas p
     on t.sk_partida = p.sk_partida
     order by p.sk_partida
/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.PARTIDAS DROP CONSTRAINT SCOUTS_PARTIDAS_FK;
ALTER TABLE LABDATABASE.TIMES DROP CONSTRAINT PARTIDAS_TIMES_FK;
ALTER TABLE LABDATABASE.ATLETAS DROP CONSTRAINT PARTIDAS_ATLETAS_FK;
ALTER TABLE LABDATABASE.ATLETAS DROP CONSTRAINT ATLETA_TIMES_FK;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.SCOUTS_PARTIDA;
DROP TABLE LABDATABASE.PARTIDAS;
DROP TABLE LABDATABASE.TIMES;
DROP TABLE LABDATABASE.ATLETAS;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.SCOUTS_PARTIDA_SK_PARTIDA_SEQ;
DROP SEQUENCE LABDATABASE.SCOUTS_PARTIDA_SK_ATLETA_SEQ;
DROP SEQUENCE LABDATABASE.PARTIDAS_SK_PARTIDA_SEQ;
DROP SEQUENCE LABDATABASE.ATLETAS_SK_ATLETAS_SEQ;
DROP SEQUENCE LABDATABASE.TIMES_SK_TIMES_SEQ;

/*Cria as tabelas*/
CREATE TABLE LABDATABASE.SCOUTS_PARTIDA (
  SK_PARTIDA NUMBER NOT NULL,
  QUANTIDADE NUMBER NOT NULL,
  CARTAO_VERMELHO NUMBER NOT NULL,
  CARTAO_AMARELO NUMBER NOT NULL,
  FALTAS NUMBER NOT NULL,
  LATERAIS NUMBER NOT NULL,
  ESCANTEIOS NUMBER NOT NULL,
  GOLS NUMBER NOT NULL,
  ASSISTENCIA NUMBER NOT NULL,
  CONSTRAINT SCOUTS_PK PRIMARY KEY (SK_PARTIDA)
);

CREATE TABLE LABDATABASE.PARTIDAS (
  SK_PARTIDA NUMBER NOT NULL,
  TIME_CASA VARCHAR2(30) NOT NULL,
  TIME_VISITANTE VARCHAR2(30) NOT NULL,
  GOLS_PRO NUMBER NOT NULL,
  GOLS_CONTRA NUMBER NOT NULL,
  ARBITRO VARCHAR2(30) NOT NULL,
  ESTADIO VARCHAR2(30) NOT NULL,
  SK_PARTIDA NUMBER NOT NULL,
  CONSTRAINT PARTIDAS_PK PRIMARY KEY (SK_PARTIDA)
);

CREATE TABLE LABDATABASE.TIMES (
  SK_TIMES NUMBER NOT NULL,
  NOME VARCHAR2(30) NOT NULL,
  CORES NUMBER NOT NULL,
  TREINADOR VARCHAR2(30) NOT NULL,
  SK_PARTIDA NUMBER NOT NULL,
  CONSTRAINT TIMES_PK PRIMARY KEY (SK_TIMES)
);

CREATE TABLE LABDATABASE.ATLETAS (
  SK_ATLETAS NUMBER NOT NULL,
  NOME VARCHAR2(30) NOT NULL,
  NUMERO NUMBER NOT NULL,
  POSICAO VARCHAR2(30) NOT NULL,
  CARTAO_AMARELO NUMBER NOT NULL,
  CARTAO_VERMELHO NUMBER NOT NULL,
  DESCRICAO VARCHAR2(30) NOT NULL,
  SK_PARTIDA NUMBER NOT NULL,
  SK_TIMES NUMBER NOT NULL,
  CONSTRAINT ATLETAS_PK PRIMARY KEY (SK_ATLETAS)
);

/*Cria as sequencias*/
CREATE SEQUENCE LABDATABASE.SCOUTS_PARTIDA_SK_PARTIDA_SEQ;
CREATE SEQUENCE LABDATABASE.PARTIDAS_SK_PARTIDA_SEQ;
CREATE SEQUENCE LABDATABASE.ATLETAS_SK_ATLETAS_SEQ;
CREATE SEQUENCE LABDATABASE.TIMES_SK_TIMES_SEQ;

/*Cria os relacionamentos*/
ALTER TABLE LABDATABASE.PARTIDAS ADD CONSTRAINT SCOUTS_PARTIDAS_FK
FOREIGN KEY (SK_PARTIDA, SK_ATLETA)
REFERENCES LABDATABASE.SCOUTS_PARTIDA (SK_PARTIDA)
NOT DEFERRABLE;

ALTER TABLE LABDATABASE.TIMES ADD CONSTRAINT PARTIDAS_TIMES_FK
FOREIGN KEY (SK_PARTIDA)
REFERENCES LABDATABASE.PARTIDAS (SK_PARTIDA)
NOT DEFERRABLE;

ALTER TABLE LABDATABASE.ATLETAS ADD CONSTRAINT PARTIDAS_ATLETAS_FK
FOREIGN KEY (SK_PARTIDA)
REFERENCES LABDATABASE.SCOUTS_PARTIDA (SK_PARTIDA)
NOT DEFERRABLE;

ALTER TABLE LABDATABASE.ATLETAS ADD CONSTRAINT ATLETA_TIMES_FK
FOREIGN KEY (SK_TIMES)
REFERENCES LABDATABASE.TIMES (SK_TIMES)
NOT DEFERRABLE;

/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.ATLETAS TO LABDATABASE;
GRANT ALL ON LABDATABASE.TIMES TO LABDATABASE;
GRANT ALL ON LABDATABASE.PARTIDAS TO LABDATABASE;
GRANT ALL ON LABDATABASE.SCOUTS_PARTIDA TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;
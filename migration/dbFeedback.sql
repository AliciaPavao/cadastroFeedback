create database dbComentarios;

use dbComentarios;

create table tbComentarios(
	nome VARCHAR(80) not null,
    data_hora datetime not null, 
    comentario text not null,
    cod_comentario int auto_increment primary key
    );
    
drop table tbComentarios;
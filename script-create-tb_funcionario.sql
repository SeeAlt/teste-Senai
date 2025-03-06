
CREATE TABLE tb_funcionario(
	idFunc INT NOT NULL AUTO_INCREMENT,
    nm_nomeFunc VARCHAR(60) NOT NULL,
    usuario VARCHAR(60),
    senha VARCHAR(45) NOT NULL,
    idCargo INT NOT NULL,
    
    CONSTRAINT pk_funcionario PRIMARY KEY(idFunc),
    CONSTRAINT fk_funcionario_cargo FOREIGN KEY(idCargo)
    REFERENCES tb_cargo(idCargo)
)
    
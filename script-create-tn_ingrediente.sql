CREATE TABLE tb_ingrediente(
	idIng INT NOT NULL AUTO_INCREMENT,
    nm_nomeIng VARCHAR(60) NOT NULL,
    idForne INT NOT NULL,
    medida VARCHAR(30) NOT NULL,
    quantidade INT NOT NULL,
    
    CONSTRAINT pk_ingrediente PRIMARY KEY(idIng),
    CONSTRAINT fk_ingrediente_fornecedor FOREIGN KEY(idForne)
    REFERENCES tb_fornecedor(idForne)
)
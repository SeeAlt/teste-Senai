CREATE TABLE tb_prato(
	idPrato INT NOT NULL,
    nm_nomePrato VARCHAR(60) NOT NULL,
    idIng INT NOT NULL,
    preco DECIMAL NOT NULL,
    
    CONSTRAINT pk_prato PRIMARY KEY(idPrato),
    CONSTRAINT fk_prato_ingrediente FOREIGN KEY(idIng)
    REFERENCES tb_ingrediente(idIng)
)
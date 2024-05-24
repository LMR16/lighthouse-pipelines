CREATE TABLE IF NOT EXISTS pricing_information (
    id INT NOT NULL PRIMARY KEY,
    municipio VARCHAR(200),
    regiao VARCHAR(2),
    estado VARCHAR(2),
    produto VARCHAR(20),
    posto VARCHAR(200),
    data_registro VARCHAR(10),
    produto INT NOT NULL,
    localizacao INT NOT NULL
);
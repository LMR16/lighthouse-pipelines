CREATE TABLE IF NOT EXISTS localizations (
    id INT NOT NULL PRIMARY KEY,
    municipio VARCHAR(200),
    regiao VARCHAR(2),
    estado VARCHAR(2)
);

CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL PRIMARY KEY,
    produto VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS prices (
    id INT NOT NULL PRIMARY KEY,
    posto VARCHAR(200),
    data_registro VARCHAR(10),
    produto INT NOT NULL,
    localizacao INT NOT NULL
);

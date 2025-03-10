-- Criação da tabela Endereco (deve vir primeiro por ser referenciada)
CREATE TABLE Endereco (
    id VARCHAR PRIMARY KEY,
    estado VARCHAR NOT NULL,
    cep VARCHAR NOT NULL,
    cidade VARCHAR NOT NULL,
    bairro VARCHAR NOT NULL,
    rua VARCHAR NOT NULL,
    numero INTEGER NOT NULL,
    complemento VARCHAR
);

-- Criação da tabela Tutor
CREATE TABLE Tutor (
    id VARCHAR PRIMARY KEY,
    endereco_id VARCHAR NOT NULL UNIQUE,  -- UNIQUE para relação 1:1
    nome VARCHAR NOT NULL,
    documentos VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    FOREIGN KEY (endereco_id) REFERENCES Endereco(id) ON DELETE CASCADE
);

-- Criação da tabela Animal
CREATE TABLE Animal (
    id VARCHAR PRIMARY KEY,
    tutor_id VARCHAR NOT NULL,
    nome VARCHAR NOT NULL,
    dataNascimento DATE NOT NULL,
    especie VARCHAR NOT NULL,
    raca VARCHAR NOT NULL,
    peso DECIMAL(6, 2) NOT NULL, -- Armazena até 9999.99 (peso de até 9999 unidades com 2 casas decimais)
    porte VARCHAR NOT NULL,
    pelagem VARCHAR NOT NULL,
    cadastro VARCHAR NOT NULL,
    foto VARCHAR NOT NULL,
    FOREIGN KEY (tutor_id) REFERENCES Tutor(id) ON DELETE CASCADE
);

-- Tabelas relacionadas à saúde do animal
CREATE TABLE Vermifugacao (
    id VARCHAR PRIMARY KEY,
    animal_id VARCHAR NOT NULL,
    nome_produto VARCHAR NOT NULL,
    data_aplicacao DATE NOT NULL,
    proxima_dose DATE NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(id) ON DELETE CASCADE
);

CREATE TABLE Saude (
    id VARCHAR PRIMARY KEY,
    animal_id VARCHAR NOT NULL,
    alergias TEXT,
    medicamentos TEXT,
    observacoes TEXT,
    FOREIGN KEY (animal_id) REFERENCES Animal(id) ON DELETE CASCADE
);

CREATE TABLE Vacina (
    id VARCHAR PRIMARY KEY,
    animal_id VARCHAR NOT NULL,
    nome_vacina VARCHAR NOT NULL,
    data_aplicacao DATE NOT NULL,
    proxima_dose DATE NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(id) ON DELETE CASCADE
);

CREATE TABLE Doenca (
    id VARCHAR PRIMARY KEY,
    animal_id VARCHAR NOT NULL,
    nome_doenca VARCHAR NOT NULL,
    data_diagnostico DATE NOT NULL,
    tratamento TEXT NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(id) ON DELETE CASCADE
);

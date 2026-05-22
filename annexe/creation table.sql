CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE etudiants (
    id SERIAL PRIMARY KEY,

    code VARCHAR(10) NOT NULL,

    numero VARCHAR(50) UNIQUE NOT NULL,

    prenom VARCHAR(100),

    nom VARCHAR(100),

    date_naissance DATE,

    classe_id INTEGER REFERENCES classes(id),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    archived BOOLEAN DEFAULT false,

    est_valide BOOLEAN DEFAULT true,

    source VARCHAR(10) DEFAULT 'DB',

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE matieres (
    id SERIAL PRIMARY KEY,

    nom VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE etudiant_matieres (
    id SERIAL PRIMARY KEY,
    
    etudiant_id INTEGER REFERENCES etudiants(id),
    
    matiere_id INTEGER REFERENCES matieres(id),
    
    note_examen NUMERIC(5,2)
);


CREATE TABLE devoir_notes (
    id SERIAL PRIMARY KEY,

    etudiant_matiere_id INTEGER REFERENCES etudiant_matieres(id),

    note NUMERIC(5,2)
);
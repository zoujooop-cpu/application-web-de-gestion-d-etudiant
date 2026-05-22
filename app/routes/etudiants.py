from fastapi import APIRouter
from app.db.database import connection
from app.schemas.etudiants_schema import EtudiantsSchema

router = APIRouter()


@router.get("/etudiants")
def get_etudiants():

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM etudiants")

    etudiants = cursor.fetchall()

    return etudiants


# AJOUTER UN ETUDIANT 

@router.post("/etudiants")
def ajouter_etudiant(etudiant: EtudiantsSchema):

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO etudiants
        (
            code,
            numero,
            prenom,
            nom,
            date_naissance,
            classe_id
        )

        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        etudiant.code,
        etudiant.numero,
        etudiant.prenom,
        etudiant.nom,
        etudiant.date_naissance,
        etudiant.classe_id
    ))

    connection.commit()

    return {
        "message": "Etudiant ajouté"
    }

# DETAIL SUR UN ETUDIANT 

@router.get("/etudiants/{id}")
def get_etudiant(id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM etudiants WHERE id = %s",
        (id,)
    )

    etudiant = cursor.fetchone()

    return etudiant

# MODIFIER UN ETUDIANT 

@router.put("/etudiants/{id}")
def modifier_etudiant(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE etudiants
        SET prenom = %s
        WHERE id = %s
    """, ("NouveauPrenom", id))

    connection.commit()

    return {"message": "Etudiant modifié"}

# SUPPRIMER UN ETUDIANT 

@router.delete("/etudiants/{id}")
def supprimer_etudiant(id: int):

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM etudiants WHERE id = %s",
        (id,)
    )

    connection.commit()

    return {"message": "Etudiant supprimé"}
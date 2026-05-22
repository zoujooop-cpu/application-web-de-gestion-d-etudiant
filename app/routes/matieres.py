from fastapi import APIRouter
from app.db.database import connection
from app.schemas.matieres_schema import MatiereSchema

router = APIRouter()


# LISTE DES MATIERES

@router.get("/matieres")
def get_matieres():

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM matieres")

    matieres = cursor.fetchall()

    return matieres


# AJOUTER MATIERE

@router.post("/matieres")
def ajouter_matiere(matieres:MatiereSchema):

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO matieres (nom)
        VALUES (%s)
    """, (matieres.nom,))

    connection.commit()

    return {"message": "Matiere ajoutée"}


# DETAIL MATIERE

@router.get("/matieres/{id}")
def get_matiere(id: int):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM matieres WHERE id = %s",
        (id,)
    )

    matiere = cursor.fetchone()

    return matiere


# MODIFIER MATIERE

@router.put("/matieres/{id}")
def modifier_matiere(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE matieres
        SET nom = %s
        WHERE id = %s
    """, ("Python", id))

    connection.commit()

    return {"message": "Matiere modifiée"}


# SUPPRIMER MATIERE

@router.delete("/matieres/{id}")
def supprimer_matiere(id: int):

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM matieres WHERE id = %s",
        (id,)
    )

    connection.commit()

    return {"message": "Matiere supprimée"}
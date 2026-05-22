from fastapi import APIRouter
from app.db.database import connection
from app.schemas.classe_schema import ClasseSchema

router = APIRouter()


# LISTE DES CLASSES

@router.get("/classes")
def get_classes():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM classes
        ORDER BY nom
    """)

    classes = cursor.fetchall()

    data = []

    for row in classes:

        data.append({
            "id": row[0],
            "nom": row[1]
        })

    return data


# DETAIL D'UNE CLASSE

@router.get("/classes/{id}")
def get_classe(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM classes
        WHERE id = %s
    """, (id,))

    row = cursor.fetchone()

    if row is None:

        return {
            "message": "Classe introuvable"
        }

    return {
        "id": row[0],
        "nom": row[1]
    }


# AJOUTER UNE CLASSE

@router.post("/classes")
def ajouter_classe(classe:ClasseSchema):

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO classes (nom)
        VALUES (%s)
    """, (classe.nom,))

    connection.commit()

    return {
        "message": "Classe ajoutée"
    }


# MODIFIER UNE CLASSE

@router.put("/classes/{id}")
def modifier_classe(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE classes
        SET nom = %s
        WHERE id = %s
    """, ("L2 GLRS", id))

    connection.commit()

    return {
        "message": "Classe modifiée"
    }


# SUPPRIMER UNE CLASSE

@router.delete("/classes/{id}")
def supprimer_classe(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM classes
        WHERE id = %s
    """, (id,))

    connection.commit()

    return {
        "message": "Classe supprimée"
    }


# ETUDIANTS D'UNE CLASSE

@router.get("/classes/{id}/etudiants")
def etudiants_classe(id: int):

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            etudiants.id,
            etudiants.code,
            etudiants.numero,
            etudiants.prenom,
            etudiants.nom

        FROM etudiants

        WHERE etudiants.classe_id = %s

        ORDER BY etudiants.nom
    """, (id,))

    resultats = cursor.fetchall()

    data = []

    for row in resultats:

        data.append({
            "id": row[0],
            "code": row[1],
            "numero": row[2],
            "prenom": row[3],
            "nom": row[4]
        })

    return data
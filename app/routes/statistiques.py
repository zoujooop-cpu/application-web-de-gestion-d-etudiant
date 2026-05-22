from fastapi import APIRouter
from app.db.database import connection

router = APIRouter()


# TOTAL DES ETUDIANTS

@router.get("/statistiques/total-etudiants")
def total_etudiants():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM etudiants
    """)

    total = cursor.fetchone()

    return {
        "total_etudiants": total[0]
    }


# NOMBRE D'ETUDIANTS PAR CLASSE
@router.get("/statistiques/etudiants-par-classe")
def etudiants_par_classe():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            classes.nom,
            COUNT(etudiants.id)

        FROM etudiants

        JOIN classes
        ON classes.id = etudiants.classe_id

        GROUP BY classes.nom

        ORDER BY classes.nom
    """)

    resultats = cursor.fetchall()

    data = []

    for row in resultats:

        data.append({
            "classe": row[0],
            "nombre_etudiants": row[1]
        })

    return data


# MOYENNE PAR MATIERE
@router.get("/statistiques/moyenne-matieres")
def moyenne_matieres():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            matieres.nom,
            ROUND(AVG(etudiant_matieres.note_examen), 2)

        FROM etudiant_matieres

        JOIN matieres
        ON matieres.id = etudiant_matieres.matiere_id

        GROUP BY matieres.nom

        ORDER BY matieres.nom
    """)

    resultats = cursor.fetchall()

    data = []

    for row in resultats:

        data.append({
            "matiere": row[0],
            "moyenne": float(row[1])
        })

    return data


# MEILLEUR ETUDIANT

@router.get("/statistiques/meilleur-etudiant")
def meilleur_etudiant():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            etudiants.prenom,
            etudiants.nom,
            ROUND(AVG(etudiant_matieres.note_examen), 2) AS moyenne

        FROM etudiant_matieres

        JOIN etudiants
        ON etudiants.id = etudiant_matieres.etudiant_id

        GROUP BY
            etudiants.id,
            etudiants.prenom,
            etudiants.nom

        ORDER BY moyenne DESC

        LIMIT 1
    """)

    row = cursor.fetchone()

    return {
        "prenom": row[0],
        "nom": row[1],
        "moyenne": float(row[2])
    }


# MATIERE AVEC MEILLEURE MOYENNE

@router.get("/statistiques/meilleure-matiere")
def meilleure_matiere():

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            matieres.nom,
            ROUND(AVG(etudiant_matieres.note_examen), 2) AS moyenne

        FROM etudiant_matieres

        JOIN matieres
        ON matieres.id = etudiant_matieres.matiere_id

        GROUP BY matieres.nom

        ORDER BY moyenne DESC

        LIMIT 1
    """)

    row = cursor.fetchone()

    return {
        "matiere": row[0],
        "moyenne": float(row[1])
    }



# NOTES D'UN ETUDIANT

@router.get("/statistiques/notes-etudiant/{etudiant_id}")
def notes_etudiant(etudiant_id: int):

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            matieres.nom,
            etudiant_matieres.note_examen

        FROM etudiant_matieres

        JOIN matieres
        ON matieres.id = etudiant_matieres.matiere_id

        WHERE etudiant_matieres.etudiant_id = %s
    """, (etudiant_id,))

    resultats = cursor.fetchall()

    data = []

    for row in resultats:

        data.append({
            "matiere": row[0],
            "note_examen": float(row[1])
        })

    return data
import csv

from app.db.database import connection

chemin=("data/données_propres.csv")

def importer_csv():

    cursor = connection.cursor()


    with open(chemin, newline='', encoding='utf-8') as fichier:

        lecteur = csv.DictReader(fichier)

        for row in lecteur:

            # AJOUT CLASSE

            cursor.execute("""
                INSERT INTO classes (nom)

                VALUES (%s)

                ON CONFLICT (nom)
                DO NOTHING
            """, (row["classe"],))

            connection.commit()

            # Recuperer id classe
            cursor.execute("""
                SELECT id FROM classes
                WHERE nom = %s
            """, (row["classe"],))

            classe_id = cursor.fetchone()[0]

            # AJOUT ETUDIANT

            cursor.execute("""
                INSERT INTO etudiants
                (code, numero, prenom, nom, classe_id)

                VALUES (%s, %s, %s, %s, %s)

                ON CONFLICT (numero)
                DO NOTHING
            """, (
                row["code"],
                row["numero"],
                row["prenom"],
                row["nom"],
                classe_id
            ))

            connection.commit()

            # Recuperer id etudiant
            cursor.execute("""
                SELECT id FROM etudiants
                WHERE numero = %s
            """, (row["numero"],))

            etudiant_id = cursor.fetchone()[0]

            # AJOUT MATIERE

            cursor.execute("""
                INSERT INTO matieres (nom)

                VALUES (%s)

                ON CONFLICT (nom)
                DO NOTHING
            """, (row["matiere"],))

            connection.commit()

            # Recuperer id matiere
            cursor.execute("""
                SELECT id FROM matieres
                WHERE nom = %s
            """, (row["matiere"],))

            matiere_id = cursor.fetchone()[0]

            # AJOUT ETUDIANT MATIERE

            cursor.execute("""
                INSERT INTO etudiant_matieres
                (etudiant_id, matiere_id, note_examen)

                VALUES (%s, %s, %s)
            """, (
                etudiant_id,
                matiere_id,
                row["note_examen"]
            ))

            connection.commit()

    cursor.close()

    return "Importation CSV terminée"
import sqlite3

DB_NAME = "database.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        company TEXT,

        difficulty TEXT,

        ats_score INTEGER,

        report TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_report(
    filename,
    company,
    difficulty,
    ats_score,
    report
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports
        (
            filename,
            company,
            difficulty,
            ats_score,
            report
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            filename,
            company,
            difficulty,
            ats_score,
            report
        )
    )

    conn.commit()
    conn.close()


def get_reports():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        filename,
        company,
        difficulty,
        ats_score,
        created_at

    FROM reports

    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
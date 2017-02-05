import indicoio
import matching
import sqlite3
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
form_number=2


def main(str):
    client = indicoio.emotion(str)
    anger = client['anger']
    fear = client['fear']
    sad = client['sadness']
    sql = """UPDATE bb_ajfss SET anger = ?, fear = ?, sadness = ?"""
    c.execute(sql, (anger, fear, sad,))
    matching.main(form_number)

if __name__ == "__main__": main()

import sqlite3
import numpy as np

sqlite_file = 'C:/Users/Alexandre/BlueBuddies/testingPYfiles/db.sqlite3'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


def main(form_number):
    # c.execute('SELECT * FROM bb_general')
    # general = (c.fetchone())
    # c.execute('SELECT * FROM bb_ajfss')
    # ajfss = (c.fetchone())

    dweight = np.array([2, 7, 7, 5, 3, 2, 3, 6], dtype=float)
    aweight = np.array([5, 5, 5], dtype=float)
    eweight = np.array([4, 5, 7, 6], dtype=float)

    if form_number is 1:    # if depression form was used (1)
        # depression[1] = depression[1]+depression[2]
        # depression[1] = np.divide(depression[1],2)
        c.execute('SELECT * FROM bb_depression')
        depression = (c.fetchone())
        depression = np.asarray(depression, dtype=float)
        depression = np.delete(depression, obj=0, axis=0)
        tot = np.dot(depression, dweight)
        totdep = tot/(np.sum(dweight))

    elif form_number is 2:    # if anxiety form was used (2)
        c.execute('SELECT * FROM bb_anxiety')
        anxiety = (c.fetchone())
        anxiety = np.asarray(anxiety, dtype=float)
        anxiety = np.delete(anxiety, obj=0, axis=0)
        tot = np.dot(anxiety, aweight)
        totanx = tot/(np.sum(eweight))

    elif form_number is 3:    # if eating disorder form was used (3)
        c.execute('SELECT * FROM bb_eating')
        eating = (c.fetchone())
        eating = np.asarray(eating, dtype=float)
        eating = np.delete(eating, obj=0, axis=0)
        tot = np.dot(eating, eweight)
        toteat = tot/(np.sum(eweight))


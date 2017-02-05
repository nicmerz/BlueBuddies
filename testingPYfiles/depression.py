import time
import indicoio
import sqlite3
import ajfss
import matching

sqlite_file = 'C:/Users/Alexandre/BlueBuddies/testingPYfiles/db.sqlite3'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'

# c.execute('SELECT * FROM bb_depression')
# depression = (c.fetchone())
# c.execute('SELECT * FROM bb_general')
# general = (c.fetchone())
# c.execute('SELECT * FROM bb_ajfss')
# ajfss = (c.fetchone())
form_number = 1 #depression form is 1 -> this is used in the matching alg

def main(str1, str2, str3, str4, str5, str6):
    # how is the client feeling

    # how well is the client sleeping, start with checking time
    strings = time.strftime("%Y,%m,%d,%H,%M,%S")
    t = strings.split(',')
    numbers = [int(x) for x in t]
    sql = """UPDATE bb_depression SET time_insomnia = ?"""
    c.execute(sql, (numbers,))

    client = [strings]  # client element 0 is current hour (assume 24-hr clock)
    # clock date and time to see if client is coming back recurrently - implemented after!
    if (numbers[3] < 4 & numbers[3] > 0):
        t = 0
        sql = """UPDATE bb_depression SET time_insomnia = ?"""
        c.execute(sql, (t,))
    else:
        # element 1 is potential insomnia, 0.4 = maybe (pulls average down
        t = 1
        sql = """UPDATE bb_depression SET time_insomnia = ?"""
        c.execute(sql, (t,))  # element 1 is potential insomnia, 1 = no

    diag = indicoio.sentiment_hq(str1)
    diagthresh = 0.5
    if (diag > diagthresh):
        # myinput = input('Have you tried getting some sleep? \n')
        # yesno = indicoio.sentiment_hq(myinput)
        # assume diagnostics are run
        t = diag
        sql = """UPDATE bb_depression SET insomnia = ?"""
        c.execute(sql, (t,))  # this suggests the client has insomnia

    emotions = indicoio.emotion(str2)
    emotions = ajfsshandler(emotions)
    sql = """UPDATE bb_depression SET relation_value"""
    c.execute(sql, (emotions,))  # ajfss was weighted and mathed out to one value

    # assume hq
    comfort = indicoio.sentiment_hq(str3)
    sql = """UPDATE bb_depression SET comfort = ?"""
    c.execute(sql, (comfort,))

    hobbies = indicoio.sentiment_hq(srt4)  # hq
    sql = """UPDATE bb_depression SET focus_hobbies = ?"""
    c.execute(sql, (hobbies,))

    focus_general = indicoio.sentiment_hq(str5)
    sql = """UPDATE bb_depression SET focus = ?"""
    c.execute(sql, (focus_general,))
    matching.main(form_number)

def ajfsshandler(ajfssdict):
    a = ajfssdict['anger']
    b = ajfssdict['joy']
    c2 = ajfssdict['fear']
    d = ajfssdict['surprise']
    e = ajfssdict['sadness']
    # maybe I have to pass through premade database so here this is:
    # sql = """UPDATE bb_ajfss SET anger = ?, joy = ?, fear = ?, sadness = ?, surprise = ?"""
    # c.execute(sql, (a, b, c2, d, e,))

    res = [a, b, c2, d, e]
    finres = ajfss.main(res)
    return finres


if __name__ == "__main__": main()

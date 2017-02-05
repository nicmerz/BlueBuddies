import indicoio
import matching
import ajfss
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'
form_number = 3


def main(str1, str2, str3):
    client = [indicoio.sentiment_hq(str1)]
    # client += [indicoio.sentiment_hq()]
    emo = indicoio.emotion(str2)
    emo = ajfsshandler(emo)
    client += [emo]

    # client += [indicoio.sentiment_hq(myinput)]
    emo1 = indicoio.emotion(str3)
    emo1 = ajfsshandler(emo)
    client += [emo1]
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
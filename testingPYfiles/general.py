import indicoio
import depression
import eatingdisorder
import anxiety
import ajfss
import numpy as np

indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'


def decisionmake(outp):
    if outp is 1:
        depression.main()
    if outp is 2:
        anxiety.main()
    if outp is 3:
        eatingdisorder.main()


def main(string1, string2, string3):
    dep = indicoio.sentiment_hq(string1)  # element 1 is first hq
    client = [dep]
    out1feelings = indicoio.emotion(string1)
    out1feelings = ajfsshandler(out1feelings)
    out1feelings = (out1feelings+dep)/2
    client += [out1feelings]  # we also keep the feelings

    anxious = indicoio.sentiment_hq(string2)
    client += [anxious]  # a sufficiently high number will trigger the anxiety scripts but keep this value for later
    meal = indicoio.sentiment_hq(string3)
    client += [meal]
# now we have to do decision-making based on testing. F U C K Y E A H L E T S G O O O
    if (dep < 0.75) and (anxious > 0.2) and (meal > 0.2):
        outp = 1  # 1 corresponds to almost exclusively depressed
    elif (dep > 0.2) and (anxious < 0.75) and (meal > 0.2):
        outp = 2  # 2 corresponds to a strong probability of an exclusive anxiety problem
    elif (dep > 0.2) and (anxious > 0.2) and (meal < 0.75):
        outp = 3  # 3 corresponds to a strong probability of exclusive bulemia/anorexia
    #     commented out for simplicity
    # elif (dep < anxious) and (dep < meal):
    #     if anxious < meal:
    #         outp = 4  # 4 corresponds to depression being the dominant and anxiety the next dominant
    #     else:
    #         outp = 5  # 5 corresponds to depression being the dominant and meal the next dominant
    # elif(anxious < dep) and (anxious < meal):
    #     if dep < meal:
    #         outp = 6  # 6 corresponds to anxiety being the dominant and depression the next dominant
    #     else:
    #         outp = 7  # 7 corresponds to anxiety being the dominant and meal the next dominant
    # elif(meal < dep) and (meal < anxious):
    #     if dep < anxious:
    #         outp = 8  # 8 corresponds to bulemia/anorexia being a dominant and depression the next dominant
    #     else:
    #         outp = 9  # 9 corresponds to bulemia/anorexia being the dominant and anxiety the next dominant
    decisionmake(outp)

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



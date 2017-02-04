import indicoio
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'

def main():
# how is the client feeling
    cllient = {'unique_id':{'General':{'feeling':0,'really_feeling':'0'},'depression':{'time':0,'insomnia':0,
                                                                                       'friends':{},'comfort':0,
                                                                                       'engaged':0, 'hobby_focus':0,
                                                                                       'general_focus':0}
        ,'anxiety':{'something_emotions':{}},'eating':{'energetic':0,'weight':0,'social_image':{}}}}
    myinput = input('How are you feeling right now? Tell me all the details! \n') # can use hq sentiment
    out1 = indicoio.sentiment_hq(myinput) # element 1 is first hq
    client = [out1]
    out1feelings = indicoio.emotion(myinput)
    client += [out1feelings] # we also keep the feelings

    if(out1 > 0.85):
        myinput = input('How are you really feeling? This is a save environment! \n') #element 2 is either 2 (illegal from indicoio), or second hq response
        out2 = indicoio.sentiment_hq(myinput)
        client += [out2]
    else:
        client += [2]

    myinput = input('Do you feel anxious about /something/ at the moment?')
    client += [indicoio.sentimenthq(myinput)] # a sufficiently high number will trigger the anxiety scripts but keep this value for later
if __name__ == "__main__": main()

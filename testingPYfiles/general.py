import indicoio
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'

def main():
# how is the client feeling
    cllient = {'unique_id':{'General':{'feeling':0,'feeling_emotions':{},
                                       'really_feeling_emotions':{},'specific_anxiety':0,'meal':0},
                            'depression':{'time':0,'insomnia':0,
                                          'friends':{},'comfort':0,
                                          'engaged':0, 'hobby_focus':0,
                                          'general_focus':0}
        ,'anxiety':{'something_emotions':{}},
                            'eating':{'energetic':0,'weight':0,'social_image':{}}}} # not to be implemented but kept as a key for documentation
    myinput = input('How are you feeling right now? Tell me all the details! \n') # can use hq sentiment
    out1 = indicoio.sentiment_hq(myinput) # element 1 is first hq
    client = [out1]
    out1feelings = indicoio.emotion(myinput)
    client += [out1feelings] # we also keep the feelings

    if(out1 > 0.85):
        myinput = input('How are you really feeling? This is a safe environment! \n') #element 2 is either 2 (illegal from indicoio), or second hq response
        client += [indicoio.emotion(myinput)]
    else:
        client += [2]
        client += [{}]

    myinput = input('Do you feel anxious about /something/ at the moment?')
    client += [indicoio.sentiment_hq(myinput)] # a sufficiently high number will trigger the anxiety scripts but keep this value for later

    myinput = input('How do you feel about having a nice meal? \n')
    client += [indicoio.sentiment_hq(myinput)]
if __name__ == "__main__": main()

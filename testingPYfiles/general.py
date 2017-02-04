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
    dep = indicoio.sentiment_hq(myinput) # element 1 is first hq
    client = [dep]
    out1feelings = indicoio.emotion(myinput)
    client += [out1feelings] # we also keep the feelings
    print(dep)
    if(dep > 0.85):
        myinput = input('How are you really feeling? This is a safe environment! \n') #element 2 is either 2 (illegal from indicoio), or second hq response
        client += [indicoio.emotion(myinput)]
    else:
        client += [2]
        client += [{}]

    myinput = input('Do you feel anxious about /something/ at the moment?')
    anxious =indicoio.sentiment_hq(myinput)
    client += [anxious] # a sufficiently high number will trigger the anxiety scripts but keep this value for later
    print(anxious)
    myinput = input('How do you feel about having a nice meal? \n')
    meal = indicoio.sentiment_hq(myinput)
    client += [meal]
    print(meal)
# now we have to do decision-making based on testing. F U C K Y E A H L E T S G O O O
    if((dep < 0.75) & (anxious > 0.2) & (meal > 0.2)):
        outp = 1 #1 corresponds to almost exclusively depressed
    elif((dep > 0.2) & (anxious < 0.75) & (meal > 0.2)):
        outp = 2 #2 corresponds to a strong probability of an exclusive anxiety problem
    elif((dep > 0.2) & (anxious > 0.2) & (meal < 0.75)):
        outp = 3 #3 corresponds to a strong probability of exclusive bulemia/anorexia
    elif((dep < anxious) & (dep < meal)):
        outp = 4 #4 corresponds to depression being the dominant but not exclusive problem
    elif((anxious < dep) & (anxious < meal)):
        outp = 5 #5 corresponds to anxiety being the dominant but not exclusive problem
    elif((meal < dep) & (meal < anxious)):
        outp = 6 #6 corresponds to bulemia/anorexia being a dominant but not exclusive problem
    print(outp)
if __name__ == "__main__": main()

import time
import indicoio
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'
def main():
# how is the client feeling

    # how well is the client sleeping, start with checking time
    strings = time.strftime("%Y,%m,%d,%H,%M,%S")
    t = strings.split(',')
    numbers = [ int(x) for x in t ]

    client = [strings] # client element 0 is current hour (assume 24-hr clock)
    if(numbers[3] < 4 & numbers[3] > 0):
        client += [1] #element 1 is potential insomnia, 1 = maybe
    else:
        client += [0] # element 1 is potential insomnia, 0 = no

    myinput = input('Are you feeling tired? \n')
    # assume diagnostics are run, be careful with diag/diagthresh
    diag = indicoio.sentiment_hq(myinput)
    diagthresh = 0.5
    if(diag > diagthresh):
        myinput = input('Have you tried resting or sleep? \n')
        # assume diagnostics are run
        if(diag > diagthresh):
            client[1] = 2 # this suggests the client has insomnia
        else:
            client[1] = 0 # not likely to have insomnia
    else:
        print('That is interesting... good to know you are well rested!')

    myinput = input('How are your friends doing recently? \n')
    # assume we have an emotions scan
    emotions = indicoio.emotion(myinput)
    client += [emotions] # element 2 is a number on emotions

    myinput = input('Is there a friend you would feel comfortable right now? \n')
    # assume hq
    comfort = indicoio.sentiment_hq(myinput)
    client += [comfort] # client element 3 is number on friend comfort

    myinput = input('What do you normally do for fun? \n') # do nothing with input
    myinput = input('Cool! Are you still as engaged with your hobbies? \n')
    hobbies = indicoio.sentiment_hq(myinput) # hq
    client += [hobbies] # client element 4 is number on hobby engagement

    myinput = input('I see, and are you as capable of focusing on them as you used to be? \n')
    focus_hobby = indicoio.sentiment_hq(myinput)
    client += [focus_hobby] # client element 5 is the number on hobby focus

    myinput = input('What about your focus in day-to-day tasks? \n')
    focus_general = indicoio.sentiment_hq(myinput)
    client += [focus_general] # client element 6 is the number on general focus, more important than hobby focus
    print(client)
if __name__ == "__main__":main()
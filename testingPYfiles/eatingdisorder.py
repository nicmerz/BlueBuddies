import indicoio
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'
def main():
    myinput = input('How energetic do you feel right now? \n')
    client = [indicoio.sentiment_hq(myinput)]
    myinput = input('//How do you feel about gaining weight?//') # question phrasing subject to change
    client += [indicoio.sentiment_hq(myinput)]
    client += [indicoio.emotion(myinput)]

    myinput = input('//How do you feel about your image socially?//') # question phrasing subject to change
    client += [indicoio.sentiment_hq(myinput)]
    client += [indicoio.emotion(myinput)]
if __name__ == "__main__": main()
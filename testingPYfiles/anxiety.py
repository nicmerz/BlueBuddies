import indicoio
indicoio.config.api_key = '3e3f2adccd348bdf2408f8c539a77b8b'
def main():
    myinput = input('How does /something/ make you feel? \n')
    client = indicoio.emotion(myinput)
    print(client)

if __name__ == "__main__": main()

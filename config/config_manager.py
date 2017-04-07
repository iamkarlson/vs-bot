import configparser,os

class config_man:
    def __init__(self,config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        section = config['DEFAULT']
        self.TOKEN=section['token']
        self.URL=section['url']
        self.COLLECTION=section['collection']

if __name__=='__main__':
    #config_path=os.environ['BOT_CONFIG']
    config = config_man("bot.ini")
    print(config.TOKEN)
    print(config.URL)
    print(config.COLLECTION)

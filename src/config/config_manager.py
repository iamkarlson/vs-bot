import configparser


class ConfigManager:
    def __init__(self, config_path):
        try :
            config = configparser.ConfigParser()
            config.read(config_path)
            section = config['DEFAULT']
            self.TOKEN = section['token']
            self.URL = section['url']
            self.COLLECTION = section['collection']
            section = config['BOT']
            self.BOT_ID = section['bot_id']
            self.SLACK_BOT_TOKEN = section['slack_bot_token']
        except:
            print("config is not initialized")
            pass



if __name__ == '__main__':
    # config_path=os.environ['BOT_CONFIG']
    testconfig = ConfigManager("bot.ini")
    print(testconfig.TOKEN)
    print(testconfig.URL)
    print(testconfig.COLLECTION)
    print(testconfig.BOT_ID)
    print(testconfig.SLACK_BOT_TOKEN)

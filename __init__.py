from mycroft import MycroftSkill, intent_file_handler


class Jeedom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jeedom.intent')
    def handle_jeedom(self, message):
        self.speak_dialog('jeedom')


def create_skill():
    return Jeedom()


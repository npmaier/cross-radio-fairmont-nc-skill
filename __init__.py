from mycroft import MycroftSkill, intent_file_handler


class CrossRadioFairmontNc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nc.fairmont.radio.cross.intent')
    def handle_nc_fairmont_radio_cross(self, message):
        self.speak_dialog('nc.fairmont.radio.cross')


def create_skill():
    return CrossRadioFairmontNc()


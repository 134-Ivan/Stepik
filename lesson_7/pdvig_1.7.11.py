


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        key = id(msg)
        if key in cls.msgs:
            cls.msgs.pop(key)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, number):
        for m in tuple(cls.msgs.values())[-number:]:
         print(m)

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.show_last_message(1)
Viber.total_messages()
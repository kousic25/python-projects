from pyclbr import Function


class Email:
    def send(self):
        print("Email Sent")
class SMS:
    def send(self):
        print("SMS Sent")
class WhatsApp:
    def send(self):
        print("WhatsApp Message Sent")
notifications = [Email(),SMS(),WhatsApp()]
for n in notifications:
    n.send()
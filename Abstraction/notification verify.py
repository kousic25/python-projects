from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class Email(Notification):
    def send(self, message):
        print("Email:", message)
class SMS(Notification):
    def send(self, message):
        print("SMS:", message)
n1 = Email()
n2 = SMS()
n1.send("Welcome")
n2.send("OTP Sent")
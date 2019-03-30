import abc
from rest_framework.authentication import BaseAuthentication

# class Person(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
#
# class China(Person):
#     def talk(self):
#         pass
#
#
# China()

class Person():
    
    def talk(self):
        raise NotImplementedError('talk() must be Implemented ')
    

class China(Person):
    pass


China().talk()
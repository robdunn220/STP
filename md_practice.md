# **Ch. 13: The Four Pillars of OOP**
## **Four Pillars**
- Encapsulation
- Abstraction
- Polymorphic
- Inheritance
## **Encapsulation**
- Object variables and methods are located within the class the object is defined in
- This allows for clients using the code to create instances of the objects without modifying the actual variables and methods of the class
- In Python, there are no private variables or methods. You can only use naming conventions to warn the client to use at their own discretion

```
class PublicPrivateExample
    def __init__(self):
        self.public = 'safe'
        self._unsafe = 'unsafe'

    def public_method(self):
        # Clients can use This
        pass

    def _unsafe_method(self):
        # Clients shouldn't use this
        pass
```

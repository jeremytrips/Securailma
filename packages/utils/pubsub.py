
class Subscriber:
    def __init__(self):
        pass

    def update(self, type, message):
        raise NotImplementedError("Subscribers have to implement the update method.")


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, instance):
        self.subscribers.add(instance)

    def unregister(self, instance):
        self.subscribers.discard(instance)

    def _dispatch(self, type, message):
        for subscriber in self.subscribers:
            subscriber.update(type, message)

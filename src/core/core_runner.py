class CoreRunner():
    def __init__(self, name):
        self.cloud = None
        self.resource = None
        self.link = None
        self.name = name
        self.context = None
        self.checks = []

    def scan(self):
        for check in self.checks:
            check.scan()

    def results(self):
        results = {}
        for check in self.checks:
            print(check.name)
            print(check.result)

    def stats(self):
        pass

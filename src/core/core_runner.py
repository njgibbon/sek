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

    def output_results(self):
        for check in self.checks:
            print(check.name + ": " + check.result)
            print()

    def output_stats(self):
        pass

    def all_passed(self):
        pass

    def output_time(self):
        print(self.time)
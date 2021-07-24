class CoreRunner():
    def __init__(self, name):
        print("Core Runner")
        self.cloud = None
        self.resource = None
        self.name = name
        self.context = None
        self.checks = []

    def scan(self):
        for check in self.checks:
            check.scan()

    def output_results():
        for check in self.checks:
            print(check.name + ": " + check.result)
            print()

    def output_stats():
        pass

    def all_passed():
        pass

class CoreRunner(): 
    def __init__(self, cloud, resource, name):
        print("Runner")
        self.cloud = cloud
        self.resource = resource
        self.name = name
        self.context = None
        self.checks = []

    def scan(self):
        for check in self.checks:
            check.scan()

    def output_results():
        for check in checks:
            print(check.name + ": " + check.result)
            print()

    def output_stats():
        pass

    def all_passed():
        pass


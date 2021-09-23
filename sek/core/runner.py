from .enums import CheckResult


class CoreRunner():
    def __init__(self, name, skip):
        self.link = None
        self.name = name
        self.skip = skip
        self.context = None
        self.checks = []
        self.time = None

    def scan(self):
        for check in self.checks:
            check.scan()

    def results(self):
        result_list = []
        for check in self.checks:
            result_map = {}
            result_map["name"] = check.name
            result_map["result"] = check.result
            result_map["message"] = check.message
            result_list.append(result_map)
        return result_list

    def format_results(self):
        result_string = ""
        results = self.results()
        for result in results:
            result_string += result["name"] + ": " + result["result"] + "\n"
            if result["message"] is not None:
                result_string += result["message"] + "\n\n"
        return result_string

    def stats(self):
        stats_map = {}
        check_total = len(self.checks)
        stats_map["checks"] = check_total
        stats_map["time"] = self.time
        passed = 0
        failed = 0
        skipped = 0
        error = 0
        for check in self.checks:
            if check.result == CheckResult.PASS:
                passed += 1
            if check.result == CheckResult.FAIL:
                failed += 1
            if check.result == CheckResult.SKIP:
                skipped += 1
            if check.result == CheckResult.ERROR:
                error += 1
        stats_map["passed"] = passed
        stats_map["failed"] = failed
        stats_map["skipped"] = skipped
        stats_map["error"] = error
        passed_percent = (passed / check_total) * 100
        failed_percent = (failed / check_total) * 100
        skipped_percent = (skipped / check_total) * 100
        error_percent = (error / check_total) * 100
        stats_map["passed_percent"] = passed_percent
        stats_map["failed_percent"] = failed_percent
        stats_map["skipped_percent"] = skipped_percent
        stats_map["error_percent"] = error_percent
        return stats_map

    def format_stats(self):
        stats = self.stats()
        time_string = "Time: " + str(stats["time"]) + "s\n"
        check_string = "Checks: " + str(stats["checks"]) + "\n"
        pass_string = "Pass: " + str(stats["passed"]) + " - (" + str(stats["passed_percent"]) + "%)\n"
        fail_string = "Fail: " + str(stats["failed"]) + " - (" + str(stats["failed_percent"]) + "%)\n"
        skip_string = "Skip: " + str(stats["skipped"]) + " - (" + str(stats["skipped_percent"]) + "%)\n"
        err_string = "Error: " + str(stats["error"]) + " - (" + str(stats["error_percent"]) + "%)\n"
        stats_string = time_string + check_string + pass_string + fail_string + skip_string + err_string
        return stats_string

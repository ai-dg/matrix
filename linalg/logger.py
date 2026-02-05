class Logger:
    RESET = "\033[0m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

    def info(self, *args, **kwargs):
        print(f"{self.BLUE}[INFO]{self.RESET}", *args, **kwargs)

    def warn(self, *args, **kwargs):
        print(f"{self.YELLOW}[WARN]{self.RESET}", *args, **kwargs)

    def error(self, *args, **kwargs):
        print(f"{self.RED}[ERROR]{self.RESET}", *args, **kwargs)

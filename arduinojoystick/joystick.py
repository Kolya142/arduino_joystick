class joystick:
    def __init__(self, device):
        self.device = device
    def input(self, n):
        if type(self.device[n]) == float:
            return self.device[n]
        return 0
from pyfirmata import Arduino, util
class device:
    def __init__(self, file, vrx, vry, sw):
        self.it = None
        self.data = Arduino(file)
        self.ports = [vrx, vry, sw]
    def init(self):
        self.it = util.Iterator(self.data)
        self.it.start()
        for i in self.ports:
            self.data.analog[i].enable_reporting()
    def __getitem__(self, item):
        return self.data.analog[self.ports[item]].read()
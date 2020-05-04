class DummyAgent(object):

    def __init__(self):
        # use fake attribute
        self.optimal = False
        self.partialoptimal = False
        self.debug = False
        self.gamma = 1.0
        self.Q = {}

    def init(self, *args):
        pass

    def set_action_names(self, *args):
        pass


def get_locals_no_self(cur_locals):
    cur_locals.pop("self")
    return cur_locals

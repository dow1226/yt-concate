from .step import Step


class Preflight(Step):
    def process(self, data, input, utils):
        print('in Preflight')
        utils.create_dir()

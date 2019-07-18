import openpyxl


class Populate(object):
    # TODO: formatting of text

    def __init__(self, cfg):
        self.cfg = cfg
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

    def write(self, data):
        for row, val in enumerate(data, start=1):
            for col, v in enumerate(val, start=1):
                self.ws.cell(row, col, v)

    def save(self, file):
        self.wb.save(file)

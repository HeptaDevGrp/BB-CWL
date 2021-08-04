class data_cleaner:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data
        self.temp_data = ''
        self.clean_data = ''

    def delete_blank_lines(self):
        for line in self.raw_data.splitlines():
            if line != '':
                self.temp_data += line + '\n'
        return

    def add_blank_lines(self):
        for line in self.temp_data.splitlines():
            if 'Posted to:' in line:
                self.clean_data += line + '\n\n'
            else:
                self.clean_data += line + '\n'
        return

    def data_cleaner_process(self):
        self.delete_blank_lines()
        self.add_blank_lines()

        return self.clean_data

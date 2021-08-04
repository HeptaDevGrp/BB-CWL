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

    def add_titles(self):
        self.temp_data = ''
        counter = 0
        for line in self.clean_data.splitlines():
            if counter == 0:
                self.temp_data += 'Title: ' + line + '\n'
            else:
                if line == '':
                    self.temp_data += '\nTitle: ' + line
                else:
                    self.temp_data += line + '\n'
            counter += 1
        self.clean_data = self.temp_data

    def data_cleaner_process(self):
        self.delete_blank_lines()
        self.add_blank_lines()
        self.add_titles()

        return self.clean_data

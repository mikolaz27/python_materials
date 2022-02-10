# Single responsibility principe

class FileSaver:

    def __init__(self, filename):
        self._filename = filename

    def save_file(self, raw_data):
        with open(self._filename, 'w', encoding='UTF8') as f:
            f.write(raw_data)


class FileFormatter:
    def __init__(self, raw_data):
        self.data = raw_data

    def change_text_format(self):
        result = ''
        for item in self.data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result


data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
        'occupation': 'private detective'
    },
    {
        'name': 'John',
        'surname': 'Watson',
        'occupation': 'doctor'
    }
]
exporter = FileFormatter(data)
file_saver = FileSaver('out.csv')

file_saver.save_file(exporter.change_text_format())

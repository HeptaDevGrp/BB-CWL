import json

def format_data(data):
    # transform the data from .txt to .json
    result_dict = {'Title': [], 'Posted On': [], 'Posted By': [], 'Posted To': [],
                   'Stipulate': []}
    for line in data.splitlines():
        if 'Title: ' in line:
            result_dict['Title'].append(line)
        elif 'Posted On: ' in line:
            result_dict['Posted On'].append(line)
        elif 'Posted By: ' in line:
            result_dict['Posted On'].append(line)
        elif 'Posted To: ' in line:
            result_dict['Posted On'].append(line)
        else:
            result_dict['Stipulate'].append(line)

    return result_dict

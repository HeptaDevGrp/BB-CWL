def time_reformat(line):
    """
    If you don't want to reformat the data, just ignore this function.
    :param line: "Friday, May 28, 2021 7:37:31 PM CST"
    :return: line: "YYYY-MM-DD HH:mm:ss"
    """
    cutoff = line.replace(',', '').split(' ')
    line = list([cutoff[3], cutoff[1], cutoff[2], cutoff[4], cutoff[5]])
    return line


def format_data(data):
    # transform the data from .txt to .json
    result_dict = {'Title': [], 'Posted On': [], 'Posted By': [], 'Posted To': [],
                   'Stipulate': []}
    counter = 0
    stipulate_ending_flag = False
    for line in data.splitlines():
        if 'Title: ' in line:
            stipulate_ending_flag = False
            result_dict['Title'].append(line.replace('Title: ', ''))
        elif 'Posted on: ' in line:
            line = line.replace('Posted On: ', '')  # strip prefix
            line = time_reformat(line)
            result_dict['Posted On'].append(line)
        elif 'Posted by: ' in line:
            stipulate_ending_flag = True
            result_dict['Posted By'].append(line.replace('Posted By: ', ''))
        elif 'Posted to: ' in line:
            result_dict['Posted To'].append(line.replace('Posted To: ', ''))
        else:
            # arrive the stipulate part of the file
            counter += 1
            if counter == 1 or stipulate_ending_flag:
                result_dict['Stipulate'].append(line)
            else:
                result_dict['Stipulate'][-1] += line + '\n'

    # delete redundancies
    result_dict['Title'].pop()
    result_dict['Stipulate'].pop()

    # # unit tests
    # print()
    # print(len(result_dict['Title']))
    # print(len(result_dict['Posted On']))
    # print(len(result_dict['Posted By']))
    # print(len(result_dict['Posted To']))
    # print(len(result_dict['Stipulate']))

    return result_dict

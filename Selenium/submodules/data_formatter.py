def format_data(data):
    # transform the data from .txt to .json
    result_dict = {'Title': [], 'Posted On': [], 'Posted By': [], 'Posted To': [],
                   'Stipulate': []}
    counter = 0
    stipulate_ending_flag = False
    for line in data.splitlines():
        if 'Title: ' in line:
            stipulate_ending_flag = False
            result_dict['Title'].append(line.strip('Title: '))
        elif 'Posted on: ' in line:
            result_dict['Posted On'].append(line.strip('Posted On: '))
        elif 'Posted by: ' in line:
            stipulate_ending_flag = True
            result_dict['Posted By'].append(line.strip('Posted By: '))
        elif 'Posted to: ' in line:
            result_dict['Posted To'].append(line.strip('Posted To: '))
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

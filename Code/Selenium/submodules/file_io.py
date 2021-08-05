import json


def write_file(filename="default.txt", content=None, m_type='txt'):
    if m_type == 'txt':
        with open(filename, 'w') as f:
            f.write(content)
    if m_type == 'json':
        with open(filename, "w") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
    return


def read_file(filename="default.txt", m_type='txt'):
    if m_type == 'txt':
        with open(filename, 'r') as f:
            content = f.read()
    return content

def read_json_file(filename,m_type='json'):
    if m_type == 'json':
        with open(filename,'r',encoding='utf8') as fp:
            content = json.load(fp)
    return content
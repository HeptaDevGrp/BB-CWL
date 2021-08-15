import json


def write_file(filename="default.txt", content=None, m_type='txt'):
    if m_type == 'txt':
        with open(filename, 'w') as f:
            f.write(content)
    if m_type == 'json':
        with open(filename, "w") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
    if m_type == 'js':
        with open(filename, "w") as f:
            formatted_content = \
                "const data = [\n" + json.dumps(content, indent=4, ensure_ascii=False) + "\n]" \
                + "\nmodule.exports={\n\tdata:data\n}"
            f.write(formatted_content)
    return


def read_file(filename="default.txt", m_type='txt'):
    if m_type == 'txt':
        with open(filename, 'r') as f:
            content = f.read()
    if m_type == 'json':
        with open(filename, 'r', encoding='utf8') as fp:
            content = json.load(fp)
    return content

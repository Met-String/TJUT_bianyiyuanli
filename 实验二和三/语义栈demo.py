import ast
# 将从词法分析器中输出的文件读取并转换为一个列表
def parse_txt_to_tuple(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        # 将读取的字符串转化为列表
        tuple_list = ast.literal_eval(content)
    return tuple_list

# 读取identifier文件并转换为一个列表
def parse_identifier(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        identifier_list = ast.literal_eval(content)
    return identifier_list

# 替换tokens中的'i'为真实标识符
def get_tokens_And_identifier():
    identifier_list = parse_identifier('identifier.txt')
    tokens = parse_txt_to_tuple('word_list.txt')
    return tokens, identifier_list



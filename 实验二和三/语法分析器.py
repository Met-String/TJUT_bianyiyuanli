priority = {
    '#': {'i': '<', '+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '(': '<', ')': '=', '#': ' '},
    '+': {'+': '=', '-': '=', '*': '<', '/': '<', '^': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '-': {'+': '=', '-': '=', '*': '<', '/': '<', '^': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '*': {'+': '>', '-': '>', '*': '=', '/': '=', '^': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '/': {'+': '>', '-': '>', '*': '=', '/': '=', '^': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '^': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '(': {'+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '(': '<', ')': '<', 'i': '<', '#': '>'},
    ')': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': '>', ')': ' ', 'i': ' ', '#': '>'},
    'i': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '(': '>', ')': '>', 'i': ' ', '#': '>'},
}

def compare_priority(op1, op2):
    return priority[op1][op2]


def compare_priority(op1, op2):
    return priority[op1][op2]

import ast

# 将从词法分析器中输出的文件读取并转换为一个列表
def parse_txt_to_tuple(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        # 将读取的字符串转化为列表
        tuple_list = ast.literal_eval(content)
    return tuple_list

def get_top_terminal(stack):
    # 从栈顶向下，找到第一个终结符
    for item in reversed(stack):
        if item[0] in priority:  # 判断是否是终结符
            return item
    return None

def get_reduction(string):
    # 根据文法进行规约
    if string in ['P+P', 'P-P', 'P*P', 'P/P', 'P^P', '(P)', 'i']:
        return {'P+P': 'P', 'P-P': 'P', 'P*P': 'P', 'P/P': 'P', 'P^P': 'P', '(P)': 'P', 'i': 'P'}[string]
    else:
        return None

def operator_precedence_parsing(tokens):
    stack = [('#', '_')]
    tokens.append(('#', '_'))
    while tokens:
        top_terminal = get_top_terminal(stack)[0]
        current_token = tokens[0][0]

        print('当前栈内容:', [x[0] for x in stack])

        if priority[top_terminal][current_token] in ['<', '=']:
            if priority[top_terminal][current_token] == '=':
                # 规约
                print( '读取的终结符:', current_token, ' 优先级:', priority[top_terminal][current_token], ' 决定: 规约\n')
                reduction_string = stack.pop()[0]
                reduction_result = get_reduction(reduction_string)
                while reduction_result is None and stack:
                    reduction_string = stack.pop()[0] + reduction_string
                    # print('reduction_string:', reduction_string)
                    reduction_result = get_reduction(reduction_string)
                if reduction_result:
                    stack.append((reduction_result, '_'))
                    print('当前栈内容:', [x[0] for x in stack])
                else:
                    break
            # 移进
            print('读取的终结符:', current_token, ' 优先级:', priority[top_terminal][current_token], ' 决定: 移进\n')
            stack.append(tokens.pop(0))
        else:
            # 规约
            reduction_string = stack.pop()[0]
            reduction_result = get_reduction(reduction_string)
            while reduction_result is None and stack:
                reduction_string = stack.pop()[0] + reduction_string
                reduction_result = get_reduction(reduction_string)
            if reduction_result:
                print('读取的终结符:', current_token, ' 优先级:', priority[top_terminal][current_token], ' 决定: 规约\n')
                stack.append((reduction_result, '_'))
            else:
                break
    if current_token == '#':
        return True
    else:
        return False

# 读取词法分析器的输出
word_list = parse_txt_to_tuple('word_list.txt')
print(word_list)
tokens = [('i', 1), ('+', '_'), ('i', 2), ('-', '_'), ('i', 3), ('/', '_'), ('(', '_'), ('i', 4), ('+', '_'), ('i', 5), (')', '_'), ('^', '_'), ('i', 6)]
print(operator_precedence_parsing(tokens))

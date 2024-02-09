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
from 语义栈demo import get_tokens_And_identifier

def compare_priority(op1, op2):
    return priority[op1][op2]


def compare_priority(op1, op2):
    return priority[op1][op2]

import ast



# 这里假设我们已经有了优先级表 priority
# 我们先写出两个辅助函数

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
i = 0;

# 四元式列表
quadruples = []
def emit(op, arg1, arg2, result):
    global quadruples
    quadruple = (op, arg1, arg2, result)
    quadruples.append(quadruple)
    print('({}, {}, {}, {})'.format(op, arg1, arg2, result))


def newtemp():
    global i;
    i = i + 1
    return "T"+str(i)

def lookup(name):
    return True

def Search_fun(str):
    global semantic_stack
    if str == 'P+P':
        T = newtemp()
        emit('+', semantic_stack[-3], semantic_stack[-1], T)
        semantic_stack[-3:] = [T]
    elif str == 'P-P':
        T = newtemp()
        emit('-', semantic_stack[-3], semantic_stack[-1], T)
        semantic_stack[-3:] = [T]
    elif str == 'P*P':
        T = newtemp()
        emit('*', semantic_stack[-3], semantic_stack[-1], T)
        semantic_stack[-3:] = [T]
    elif str == 'P/P':
        T = newtemp()
        emit('/', semantic_stack[-3], semantic_stack[-1], T)
        semantic_stack[-3:] = [T]
    elif str == 'P^P':
        T = newtemp()
        emit('^', semantic_stack[-3], semantic_stack[-1], T)
        semantic_stack[-3:] = [T]
    elif str == '(P)':
        semantic_stack[-3:] = [semantic_stack[-2]]

# 语义栈
semantic_stack = ['#']

def operator_precedence_parsing(tokens, identifier):
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
                    Search_fun(reduction_string)
                    stack.append((reduction_result, '_'))
                    print('当前栈内容:', [x[0] for x in stack])
                else:
                    break
            # 移进
            print('读取的终结符:', current_token, ' 优先级:', priority[top_terminal][current_token], ' 决定: 移进\n')
            stack.append(tokens.pop(0))
            if current_token == 'i':
                semantic_stack.append(identifier.pop(0)[1])  # 在移进的时候将标识符原始符号添加到语义栈
            else:
                semantic_stack.append("_")  # 对于其他符号，添加 "_"
        else:
            # 规约
            reduction_string = stack.pop()[0]
            reduction_result = get_reduction(reduction_string)
            while reduction_result is None and stack:
                reduction_string = stack.pop()[0] + reduction_string
                reduction_result = get_reduction(reduction_string)
            if reduction_result:
                Search_fun(reduction_string)
                print('读取的终结符:', current_token, ' 优先级:', priority[top_terminal][current_token], ' 决定: 规约\n')
                stack.append((reduction_result, '_'))
            else:
                break
    if current_token == '#':
        return True
    else:
        return False

# 读取词法分析器的输出
tokens , identifier = get_tokens_And_identifier()
print(tokens,identifier)
print(operator_precedence_parsing(tokens, identifier))

with open('quadruples.txt', 'w') as f:
    for quadruple in quadruples:
        print(quadruple)
        f.write('({}, {}, {}, {})\n'.format(quadruple[0], quadruple[1], quadruple[2], quadruple[3]))
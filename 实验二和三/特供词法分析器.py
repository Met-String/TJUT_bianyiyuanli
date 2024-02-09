# 本代码的意义是按照字节读取
# 使用示例
# 种别编码表：
symbol_dict = {
    "(": 1,
    ")": 2,
    "+": 3,
    "-": 4,
    "*": 5,
    "/": 6,
    "^": 7,
    "常量": 8
}

# 运算符由于其特殊性单独开辟一个区域
symbol_dict2 = {

}

# 标识符表：
identifier = []
iden = 0


def buildlist(i):
    global identifier
    global iden
    identifier = identifier + [(iden, i)]
    iden = iden + 1
    return [('i', iden)]


# 常数表：
numlist = []
idenum = 0


def bulidnumlist(i):
    global numlist
    global idenum
    numlist = numlist + [(idenum, i)]
    idenum = idenum + 1
    return [(i, idenum)]


# 单词序列：
word_list = []


def selector(code):
    global word_list
    token = ''
    for i in code:
        if i == ' ' or i == '\n' or i in symbol_dict:
            if i in symbol_dict2 and token in symbol_dict2:
                token = token + i
                i = ''
            if token != '':
                if token in symbol_dict:
                    print("当前token为：{:<10}".format(token) + "匹配种别：保留字  {}  {:<20}".format(symbol_dict[token], '存入单词表'))
                    word_list = word_list + [(token, '_')]
                elif token.isdigit():
                    print(
                        "当前token为：{:<10}".format(token) + "匹配种别：常量        {:<20}".format('存入单词表、常量表'))
                    word_list = word_list + bulidnumlist(token)
                else:
                    print(
                        "当前token为：{:<10}".format(token) + "匹配种别：标识符      {:<20}".format('存入单词表、符号表'))
                    word_list = word_list + buildlist(token)
            if i in symbol_dict:
                if i in symbol_dict2:
                    token = i
                    print("当前token为：{:<10}".format(token) + '疑似为双目运算符，暂时存留')
                    continue
                print(
                    "当前token为：{:<10}".format(i) + "匹配种别：保留字  {}  {:<20}".format(symbol_dict[i], '存入单词表'))
                word_list = word_list + [(i, '_')]
            token = ''
            continue
        elif token in symbol_dict2:
            print("当前token为：{:<10}".format(token) + "匹配种别：保留字  {}  {:<20}".format(symbol_dict[token], '存入单词表'))
            word_list = word_list + [(token, '_')]
            token = i
            continue
        token = token + i
        if token.isdigit():
            print("当前token为：{:<10}".format(token) + '疑似为常量，暂时存留')
        else:
            print("当前token为：{:<10}".format(token) + '疑似为标识符，暂时存留')
    if len(token) > 0:
        print(
            "当前token为：{:<10}".format(token) + "匹配种别：标识符      {:<20}".format('存入单词表、符号表'))
        word_list = word_list + buildlist(token)

file_path = 'C2.txt'
myfile = data = open(file_path, 'r')
code = myfile.read()
print(code)
selector(code)
print('最终结果:', word_list)
myfile = open('./word_list.txt', 'w')
myfile.write(str(word_list))
myfile = open('./identifier.txt', 'w')
myfile.write(str(identifier))
myfile = open('./numlist.txt', 'w')
myfile.write(str(numlist))
print('标识符表：', identifier)
print('常量表：', numlist)

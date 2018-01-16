# 导入数据
import yaml

def init_yaml(out_file, categories):
    """初始化yaml头部
    @param categories, 列表
    """
    with open(out_file, 'w') as fh:
        fh.write('categories:'+'\n')
        for category in categories:
            fh.write('- '+category+'\n')
        fh.write('conversations:'+'\n')

def export_as_yaml(in_file, out_file, categories):
    """
    导出数据为yml
    """
    if not out_file.endswith('.yml'):
        out_file = out_file = '.yml'
    init_yaml(out_file, categories)
    diglogs = []
    with open(in_file, 'r') as fh:
        for line in fh:
            ymls = []
            data = eval(line)
            answer = data.get('answer')
            question = data.get('question')
            suggest = data.get('suggest')
            inner_suggest = data.get('inner_suggest')
            if answer:
                ymls.append(answer)
            if question:
                ymls.append(question)
            if suggest:
                ymls.append(suggest)
            if inner_suggest:
                ymls.append(inner_suggest)
            diglogs.append(ymls)
    with open(out_file, 'a') as fh:
        fh.write(yaml.dump(diglogs, default_flow_style=False, allow_unicode=True))


def main():
    print(yaml.dump([['你好IP','a']], default_flow_style=False, allow_unicode=True))
    #export_as_yaml('raw_data/bocdata', 'data/boc.yml', ['questions'])
    #a = [{'c':'d'}, [1], [2], [3, 4]]
    #print(yaml.dump(a, default_flow_style=False))
    #print(yaml.dump(a, explicit_start=True))
    #print(yaml.dump(Hero("Galain Ysseleg", hp=-3, sp=2)))
    #print(yaml.dump(Monster(
     #name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT'])))

if __name__ == '__main__':
    main()

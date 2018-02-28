import re

def SearchIndex(test_list):
    liststr = str(test_list)
    targetstr = liststr[0:liststr.find('Success')]
    targetstr = re.sub(r'[^\[\]\,]', '', targetstr)
    targetstr = re.sub(r'\[[^\[\]]*?\]', '', targetstr)
    indexes = list(map(len, targetstr.split('[')[1:]))
    print(indexes)

if __name__ == '__main__':
    test_list=['Fail',['Fail',['Fail',['Fail','Fail'],['Fail'],['Fail',['Success','Fail']],'Fail',['Fail',['Fail']]]]]
    SearchIndex(test_list)

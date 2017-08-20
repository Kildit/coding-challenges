import re
import os
import datetime

from bs4 import BeautifulSoup
import requests

problem = {
    'id' : None,
    'title' : {
        'desc' : '문제 제목',
        'val' : ''
    },
    'info' : {
        'desc' : [],
        'val' : []
    },
    'description' : {
        'desc' : '문제',
        'val' : ''
    },
    'input' : {
        'desc' : '입력',
        'val' : ''
    },
    'output' : {
        'desc' : '출력',
        'val' : ''
    },
    'tags' : {
        'desc' : '알고리즘 분류',
        'val' : []
    }
}

# get/analyze problem info
problem['id'] = input('문제 번호: ')
url = 'https://www.acmicpc.net/problem/' + problem['id']

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
data = ''

for item in ['title', 'description', 'input', 'output']:
    problem[item]['val'] = soup.select('#problem_'+item)[0].text


for item in soup.select('#problem-info th'):
    problem['info']['desc'].append(item.text)
for item in soup.select('#problem-info td'):
    problem['info']['val'].append(item.text)


for tag in soup.select('#problem_tags li a'):
    problem['tags']['val'].append(tag.text)

# create markdown
md = 'lastupdated: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n'
md += '[문제 바로가기](' + url + ')\n\n'
md += '# ' + problem['title']['val'] + '\n\n'

for key in ['desc', '---', 'val']:
    if (key == '---'):
        md += '|'

        for i in range(0, len(problem['info']['desc'])):
            md += ' --- |'

        md += '\n'
        continue

    else:
        md += '|'

        for item in problem['info'][key]:
            md += ' ' + re.sub('^[\s+]*', '', item) + ' |'

        md += '\n'

md += '\n\n'
    
for key in ['description', 'input', 'output', 'tags']:
    md += '## ' + problem[key]['desc'] + '\n'

    if type(problem[key]['val']) == list:
        for item in problem[key]['val']:
            md += '- ' +  re.sub('^[\s+]*', '', item) + '\n'
        md += '\n'

    else:
        item = problem[key]['val']
        md += re.sub('^[\s+]*', '', item) + '\n\n'

# create problem folder
filename = problem['id'] + ' - ' + problem['title']['val']
 # 폴더이름으로 못 쓰는 특수문자들 제거
filename = re.sub('[\\|\/|:|\*|\?|"|<|>|\|]+', ' ', filename)
filename += '/readme.md'


# 이 부분은 잘 모르겠어서 스택오버플로우에서 찾아 씀. 미래에 자세히 알아볼 것!  https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(md)

f.close()
import sys, os
import shutil
import requests
from bs4 import BeautifulSoup

LOGIN_INFO = {
    'uname': 'id',
    'pw': 'pw'
}

solved_only = False

total = 0
with open('temp.java', 'r', encoding='UTF8') as f:
    temp = f.read()

with requests.Session() as s:
    login_req = s.post('https://codingbat.com/login', data=LOGIN_INFO)

    if login_req.status_code != 200:
        raise Exception('Login Error! Check your ID and PW.')
    
    main_page = BeautifulSoup(login_req.content, 'html.parser')
    practice_title = main_page.find_all('span', {'class':'h2'})

    for title in practice_title:
        title_url = f'https://codingbat.com/java/{title.get_text()}'
        sub_req = s.get(title_url)
        sub_page = BeautifulSoup(sub_req.content, 'html.parser')
        sub_items = sub_page.find_all('td', {'width':'200'})
        
        if os.path.exists(f'Java/{title.get_text()}'):
            shutil.rmtree(f'Java/{title.get_text()}')
        os.makedirs(os.path.join(f'Java/{title.get_text()}'))

        for item in sub_items:
            img = item.find('img')
            info = item.find('a')

            solved = (img['src'] == '/c2.jpg')
            problem_url = info['href']
            problem_title = info.get_text()

            if solved_only or solved:
                total += 1
                print(f'{problem_title} (solved: {solved}): {problem_url}')

                item_url = f'https://codingbat.com{problem_url}'
                problem = s.get(item_url)
                problem_page = BeautifulSoup(problem.content, 'html.parser')

                explanation = problem_page.find('p', {'class':'max2'})
                explanation = explanation.get_text()

                example = problem_page.find('table', {'border':'0'})
                example = str(example.find('td', {'valign':'top'}))
                example = example[example.find('</div><br/>')+11:example.find('<p>')].replace('<br/>','\n')
                print(example)

                code_line = problem_page.find('form', {'name':'codeform'})
                code = code_line.get_text()

                print(code)

                new_temp = temp.replace('<comment>', explanation)
                new_temp = new_temp.replace('<example>', example)
                new_temp = new_temp.replace('<code>', code)
                with open(f'Java/{title.get_text()}/{problem_title}.java', 'w', encoding='UTF8') as f:
                    f.write(new_temp)

print(f'{total} files were downloaded.')
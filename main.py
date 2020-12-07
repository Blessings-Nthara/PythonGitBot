from bs4 import BeautifulSoup
import requests

site_session = requests.Session()
html_text = site_session.get('https://github.com/login').text
soup = BeautifulSoup(html_text, 'lxml')
login = soup.find('div', id='login')
authenticity_token = login.find('form')
token = authenticity_token.findChild('input').get('value')
allow_signup = soup.find('input', id='allow_signup').get('value')
client_id = soup.find('input', id='client_id').get('value')
commit = soup.find('input', class_='btn btn-primary btn-block').get('value')
ga_id = soup.find('input', class_="js-octo-ga-id-input").get('value')
integration = soup.find('input', id="integration").get('value')
login = ""
password = ""
required=""
return_to = soup.find('input', id="return_to").get('value')
timestamp = soup.find(attrs={"name": "timestamp"})['value']
timestamp_secret = soup.find(attrs={"name": "timestamp_secret"})['value']
webauthn = soup.find(attrs={"name": "webauthn-iuvpaa-support"})['value']
support = soup.find(attrs={"name": "webauthn-support"})['value']


url = 'https://github.com/session'


allData = {'allow_signup': allow_signup, 'authenticity_token': token, 'client_id': client_id, 'commit': commit,
         'ga_id': ga_id, 'integration': integration, 'login': login, 'password': password, 'required_field_1526':
             required, 'return_to': return_to, 'timestamp': timestamp, 'timestamp_secret': timestamp_secret,
         'webauthn-iuvpaa-support': webauthn, 'webauthn-support': support}
siteRequest =site_session.post(url, data=allData )

if(siteRequest.status_code==200):
    issueHtml = site_session.get('https://github.com/Blessings-Nthara/PythonBot/issues/new').text

    soup2 = BeautifulSoup(issueHtml,'lxml')
    form_= soup2.find('form',id="new_issue")
    base_commit_oid = soup2.find(attrs={"name": "base_commit_oid"})['value']
    comment_id = soup2.find(attrs={"name": "comment_id"})['value']
    end_commit_oid = soup2.find(attrs={"name": "end_commit_oid"})['value']
    issue_body = "Deneme Body"
    issue_body_template = ''
    issuetitle = "Deneme"

    issue_data={'authenticity_token':form_.findChild('input').get('value'), 'base_commit_oid':base_commit_oid, 'comment_id':comment_id,
                'end_commit_oid':end_commit_oid, 'issue[body]':issue_body,
                'issue[body_template_name]':issue_body_template, 'issue[title]':issuetitle,
                'issue[user_assignee_ids][]': '', 'line': '', 'path': '', 'preview_side': '', 'preview_start_side': '',
                'required_field_a17e': '', 'saved_reply_id': '', 'start_commit_oid': '', 'start_line': '',
                'timestamp': soup2.find(attrs={"name": "timestamp"})['value'],
                'timestamp_secret': soup2.find(attrs={"name": "timestamp_secret"})['value']}

    print(site_session.post('https://github.com/Blessings-Nthara/PythonBot/issues',data=issue_data))
















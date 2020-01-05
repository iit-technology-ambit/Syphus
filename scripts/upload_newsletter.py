import os
from datetime import datetime

import requests

NEWSLETTER_PATH = 'newsletter.html'


def login():
    # login
    print('trying to login...')
    req_sess = requests.session()
    resp = req_sess.post('https://api.iit-techambit.in/auth/login', json={
        "email": os.getenv('API_SUPERUSER_EMAIL'),
        "password": os.getenv('API_SUPERUSER_PASSWORD'),
        "remember": "true"
    })

    if resp.status_code != 200:
        print("Login Failed!")
        print(resp.text)
        os._exit(1)

    print('Login successful!')
    return req_sess


def upload_newsletter(req_sess):

    with open(NEWSLETTER_PATH, 'r') as f:
        news_html = f.read()

    newsletter_payload = {
        'description': input('Enter description for the newsletter: '),
        "newsletter_content": news_html,
        "publish_date": input('Enter publish date in DD-MM-YYYY format: '),
        "cover_image_url": input('Enter URL to image upload on CDN: ')
    }

    # check date time
    try:
        dttm = datetime.strptime(newsletter_payload['publish_date'], '%d-%m-%Y')
        print("The datetime mentioned by you is " + str(dttm.strftime('%d-%m-%Y')))
        input("Please press enter to carry on, Ctrl+C to abort!")
    except Exception:
        print('incorrect datetime format')
        os._exit(1)

    print('Checking image url...')
    resp = req_sess.get(newsletter_payload['cover_image_url'])
    if resp.status_code != 200:
        print('Image URL not working!')
        os._exit(1)

    print('sending payload to newsletter endpoint')
    resp = req_sess.post('https://api.iit-techambit.in//newsletter/add', json=newsletter_payload)

    if resp.status_code != 200:
        print('Failed')
        print(resp.text)
        os._exit(1)
    print('Newsletter added!')
    print(resp.text)


if __name__ == "__main__":
    authenticated_sess = login()
    upload_newsletter(authenticated_sess)

from bs4 import BeautifulSoup as bs
import requests
import re

class questionScrap():
    # def __init__(self, question_id):
    #     self.question_id = question_id
    # def __init__(self):
        # self.question_id = question_id

    def fetchResponse(self):
        # BASE_URL = 'https://www.geeksforgeeks.org/problem/{}/'.format(self.question_id)
        BASE_URL = 'https://www.geeksforgeeks.org/problem-of-the-day'

        NEW_BASE_URL = ''
        response = {}

        page = requests.get(BASE_URL)
        print("Page", page)
        print("Status Code:", page.status_code)
        if(page.status_code == 200):
            soup = bs(page.content, 'html.parser')
            # anchor_tag = soup.find('a', id='potd_solve_prob')
            anchor_tag = soup.select("#potd_solve_prob")
            print("anchor tag", anchor_tag)
            if anchor_tag:
                NEW_BASE_URL = anchor_tag['href']

        response["url"] = NEW_BASE_URL
        if response:
            return response
        else:
            return {"error" : "Question Not Found"}

        # if NEW_BASE_URL:
        #     page = requests.get(NEW_BASE_URL)
        #     soup = bs(page.content, 'html.parser')


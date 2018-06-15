import requests

try:
    url1 = 'https://www.gmail.com'
    r = requests.get(url1)
    Responsecode = r.status_code
    if Responsecode == 200:
        print("Request successful on: " + url1)
        print("************************************")
        dataobj = r.text
        form_check = ['login_form', 'Login', 'Login_Form', 'login', 'Login_form', 'login_Form'
            , 'login form', 'Login Form', 'login form']
        for items in form_check:
            if items in dataobj:
                print("Login Page Present in: " + url1)
except requests.exceptions.ConnectionError as e:
    print("Unable to reach website")

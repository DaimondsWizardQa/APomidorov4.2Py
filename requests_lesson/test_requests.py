import requests

def test_requests(session_req):

    data = {
        'username': 'admin',
        'password': 'password123'
    }

    url = 'https://restful-booker.herokuapp.com/auth'

    # response = requests.post(url=url, json=data)
    # response = requests.get(url='https://restful-booker.herokuapp.com/booking').json()
    # print(response)
    # response_json = response.json()
    # print(response.headers)
    # print(response.status_code)
    # assert response.status_code == 200
    # print(response_json)

    # session_req.post(url=url, json=data)
    session_req.headers.update({'new_header': 'new_value'})
    print(session_req.headers)





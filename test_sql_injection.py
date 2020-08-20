import tempfile, requests, pytest, json

def test_post_api_1():
    url = "http://localhost:5000/v1/sanitized/input/"
    response = requests.request("POST", url, json = {'payload': 'hello'})
    res = json.loads(response.text)
    print("Test 1: Input = hello, should respond with sanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "sanitized"
    
def test_post_api_2():
    url = "http://localhost:5000/v1/sanitized/input/"
    payload = {}
    response = requests.request("POST", url,json = {'payload': '--'})
    res = json.loads(response.text)
    print("Test 2: Input = -- , should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"


def test_post_api_3():
    url = "http://localhost:5000/v1/sanitized/input/"
    response = requests.request("POST", url,json = {'payload': '1\'or\'1\'=\'1'})
    res = json.loads(response.text)
    print("Test 3: Input = '1'='1 , should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_4():
    url = "http://localhost:5000/v1/sanitized/input/"
    payload = {}
    response = requests.request("POST", url,json = {'payload': '1\'or\'1\'=\'1'})
    res = json.loads(response.text)
    print("Test 4: Input = 1'or2>1--, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_5():
    url = "http://localhost:5000/v1/sanitized/input/"
    payload = {}
    response = requests.request("POST", url,json = {'payload': '105 OR 1=1'})
    res = json.loads(response.text)
    print("Test 5: Input = 105 OR 1=1, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_6():
    url = "http://localhost:5000/v1/sanitized/input/"
    payload = {}
    response = requests.request("POST", url,json = {'payload': '\" or \"\"=\"\"'})
    res = json.loads(response.text)
    print("Test 6: Input = \" or \"\"=\"\", should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_7():
    url = "http://localhost:5000/v1/sanitized/input/"
    payload = {}
    response = requests.request("POST", url,json = {'payload': '105; DROP TABLE Suppliers'})
    res = json.loads(response.text)
    print("Test 6: Input = 105; DROP TABLE Suppliers, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"



















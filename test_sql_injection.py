import requests, pytest, json

url = "http://localhost:5000/v1/sanitized/input/"

def test_post_api_1():
    response = requests.request("POST", url, json = {'payload': 'hello'})
    res = json.loads(response.text)
    print("Test 1: Input = hello, should respond with sanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "sanitized"
    
def test_post_api_2():
    response = requests.request("POST", url,json = {'payload': '--'})
    res = json.loads(response.text)
    print("Test 2: Input = -- , should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_3():
    response = requests.request("POST", url,json = {'payload': '1\'or\'1\'=\'1'})
    res = json.loads(response.text)
    print("Test 3: Input = '1'='1 , should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_4():
    response = requests.request("POST", url,json = {'payload': '1\'or\'1\'=\'1'})
    res = json.loads(response.text)
    print("Test 4: Input = 1'or2>1--, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_5():
    response = requests.request("POST", url,json = {'payload': '105 OR 1=1'})
    res = json.loads(response.text)
    print("Test 5: Input = 105 OR 1=1, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_6():
    response = requests.request("POST", url,json = {'payload': '\" or \"\"=\"\"'})
    res = json.loads(response.text)
    print("Test 6: Input = \" or \"\"=\"\", should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_7():
    response = requests.request("POST", url,json = {'payload': '105; DROP TABLE Suppliers'})
    res = json.loads(response.text)
    print("Test 7: Input = 105; DROP TABLE Suppliers, should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_8():
    response = requests.request("POST", url,json = {'payload': '%3e'})
    res = json.loads(response.text)
    print("Test 8: Input = '%3e', should respond with unsanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "unsanitized"

def test_post_api_9():
    response = requests.request("POST", url,json = "string")
    res = json.loads(response.text)
    print("Test 9: Input = string, not correct json format, should respond with ERROR: Incorrect Data Format.  Actually responded with: " + res['result'])
    assert res['result'] == "ERROR: Incorrect Data Format"

def test_post_api_10():
    response = requests.request("POST", url, json = [1,2,3])
    res = json.loads(response.text)
    print("Test 10: Input = List[Int], not correct json format, should respond with ERROR: Incorrect Data Format.  Actually responded with: " + res['result'])
    assert res['result'] == "ERROR: Incorrect Data Format"

def test_post_api_11():
    response = requests.request("POST", url, json = {'payload': '08/21/2020'})
    res = json.loads(response.text)
    print("Test 11: Input = 08/21/2020, should respond with sanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "sanitized"

def test_post_api_12():
    response = requests.request("POST", url, json = {'payload': '08-21-2020'})
    res = json.loads(response.text)
    print("Test 12: Input = 08-21-2020, should respond with sanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "sanitized"

def test_post_api_13():
    response = requests.request("POST", url, json = {'payload': 'relykstm@gmail.com'})
    res = json.loads(response.text)
    print("Test 13: Input = relykstm@gmail.com, should respond with sanitized.  Actually responded with: " + res['result'])
    assert res['result'] == "sanitized"



















import requests


# -------------------------------
# 200 SUCCESS
# -------------------------------

def test_status_code_200():

    url = (
        "https://httpbingo.org/status/200"
    )

    response = requests.get(url)

    print("\n200 Response:\n")
    print(response.status_code)

    assert response.status_code == 200


# -------------------------------
# 201 CREATED
# -------------------------------

def test_status_code_201():

    url = (
        "https://jsonplaceholder.typicode.com/posts"
    )

    payload = {

        "title": "API Testing",
        "body": "Learning POST request",
        "userId": 1

    }

    response = requests.post(
        url,
        json=payload
    )

    print("\n201 Response:\n")
    print(response.status_code)

    assert response.status_code == 201


# -------------------------------
# 400 BAD REQUEST
# -------------------------------

def test_status_code_400():

    url = (
       "https://httpbingo.org/status/400"
    )

    response = requests.post(
        url,
        data="invalid_data"
    )

    print("\n400 Response:\n")
    print(response.status_code)

    # concept demonstration
    # assert response.status_code in [400, 201]
    assert response.status_code == 400


# -------------------------------
# 401 UNAUTHORIZED
# -------------------------------

def test_status_code_401():

    url = (
        "https://httpbingo.org/status/401"
    )

    response = requests.get(url)

    print("\n401 Response:\n")
    print(response.status_code)

    assert response.status_code == 401


# -------------------------------
# 403 FORBIDDEN
# -------------------------------

def test_status_code_403():

    url = (
        "https://httpbingo.org/status/403"
    )

    response = requests.get(url)

    print("\n403 Response:\n")
    print(response.status_code)

    assert response.status_code == 403


# -------------------------------
# 404 NOT FOUND
# -------------------------------

def test_status_code_404():

    url = (
        "https://jsonplaceholder.typicode.com/invalid"
    )

    response = requests.get(url)

    print("\n404 Response:\n")
    print(response.status_code)

    assert response.status_code == 404


# -------------------------------
# 500 INTERNAL SERVER ERROR
# -------------------------------

def test_status_code_500():

    url = (
        "https://httpbingo.org/status/500"
    )

    response = requests.get(url)

    print("\n500 Response:\n")
    print(response.status_code)

    assert response.status_code == 500
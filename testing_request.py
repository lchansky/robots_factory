import requests

r = requests.post(
    'http://127.0.0.1:8000/robots/api/v1/create',
    json={
        # "serial": "D3-R4",
        "model": "R9",
        "version": "D2",
        "created": "2023-01-29 23:59:59",
    },
)
pass

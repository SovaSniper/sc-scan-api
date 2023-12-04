import requests

class StorageService:
    def __init__(self):
        self.url = "https://api.pinata.cloud/pinning"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI0MTZjOTZmNi0wYzNlLTQ1YTEtOTZiNS0wYjVjOWQwZDA2OGMiLCJlbWFpbCI6ImFpLWxlaW5hQG91dGxvb2suY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjYyMDliMzM1M2IwY2MwZDk5YTI2Iiwic2NvcGVkS2V5U2VjcmV0IjoiODc3NzdjNzQ5OGQ5NmJlYjkwNGJlYTFkZTMxNjIwYTg4NGE5MWZkZDJhNjhlYzlmNDlkMDg0MmRjZTUxMDhiMCIsImlhdCI6MTY5OTA1Nzg4OX0.EUZ7vbk8YqzQt0vmzvOOLLedv48gppcH3xjvj7iJW-g"
        }

    def upload(self, data) -> str:
        payload = { "pinataContent": data }

        req = requests.post(f"{self.url}/pinJSONToIPFS", json=payload, headers=self.headers)
        response = req.json()
        if "IpfsHash" not in response:
            return ""
        
        return response["IpfsHash"]

storage = StorageService()

def get_storage():
    return storage
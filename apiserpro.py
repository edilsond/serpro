import dotenv, os, base64, requests, json

dotenv.load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

autorization = consumer_key + ':' + consumer_secret

def geraBearer(autorization):

    autorization_base64 = base64.b64encode(autorization.encode()).decode()
    return(autorization_base64)

def geraToken(autorization_base64):

    url = "https://gateway.apiserpro.serpro.gov.br/token"
    payload = "grant_type=client_credentials"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {autorization_base64}",
    "grant_type": "client_credentials"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    access_token = json.loads(response.content.decode())

    return(access_token['access_token'])


def consultaNFe(chave, token):
    url = f"https://gateway.apiserpro.serpro.gov.br/consulta-nfe-df/api/v1/nfe/{chave}"

    payload = ""
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    return(response.text)
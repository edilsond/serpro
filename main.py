from apiserpro import geraToken, geraBearer, consultaNFe
import dotenv, os, sys

dotenv.load_dotenv()

def main():

    if len(sys.argv) == 2:
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')

        autorization = consumer_key + ':' + consumer_secret
        access_token = geraToken(geraBearer(autorization))
        print(consultaNFe(sys.argv[1], access_token))

    else:
        print('Informe a chave de acesso da NFe como argumento do script')

if __name__ == '__main__':
    main()
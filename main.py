import requests
import sys

class Exploit:

    def __init__(self, url):
        self.webhook_url = url


    def execute(self):
        return requests.delete(self.webhook_url)

    
def main():
    if len(sys.argv) < 1:
        print(f'Uso: py {sys.argv[0]} <URL da Webhook>')
        sys.exit()

    webhook_url = sys.argv[1]

    exploit = Exploit(webhook_url)

    exploit.execute()
    
    print("Done, u can close it :)")
    input("Press Enter to Exit")


if __name__ == '__main__':
    main()
import requests as r
import argparse


def check(url):
    url = url
    try:
        response = r.get(url)
        response.raise_for_status()

        if response.history:
            print("Redirection exists from", response.history[0].url+" to "+response.url)
            return 1
        else:
            print("Redirection does not exist from", response.url)
            return 0

    except r.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except r.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except r.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except r.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    except r.exceptions.TooManyRedirects as errToo:
        print("Too Many redirects please try different one", errToo)
    except r.exceptions.SSLError as errSSL:
        print("SSL error: ", errSSL)


def ssl_check():
    parser = argparse.ArgumentParser(description="Check SSL Validation of any website")
    parser.add_argument("-i", "--interactivity", action="store_true", help="Allow CLI interactivity")
    parser.add_argument("-u", "--url", help="Write URL to check ssl validation ex: https://example.com")
    args = parser.parse_args()

    if args.interactivity:
        print('Interactivity On')
        url = input('Please write url:')
    else:
        url = args.url

    if url != '' or url != 'None':
        check(url)  # check ssl validation


if __name__ == '__main__':
    ssl_check()

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='PyEngine to create gists over git.')
    parser.add_argument('-c', '--config', type=str, required=True,
                        help='location of credentials file.',
                        default='/credentials/oauth.json')
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='file to put as a gist')
    args = parser.parse_args()
    return args
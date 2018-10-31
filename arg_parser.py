import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='PyEngine to create gists over git.')
    parser.add_argument('-c', '--config', type=str, required=True,
                        help='location of credentials file.',
                        default='/credentials/oauth.json')
    parser.add_argument('-tc', '--template_conf', type=str, required=True,
                        help='Jinja2 template file for config')
    parser.add_argument('-u', '--dcos_cluster_name', type=str, required=True,
                        help='Cluster where these visualisations are needed')
    args = parser.parse_args()
    return args
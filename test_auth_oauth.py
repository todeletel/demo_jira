# https://confluence.atlassian.com/display/JIRA/Configuring+OAuth+Authentication+for+an+Application+Link
from jira import JIRA
import jira.jirashell
key_cert_data = None
key_cert = 'jira.pem'
JIRA_URL = "http://localhost:8080"

with open(key_cert, 'r') as key_cert_file:
    key_cert_data = key_cert_file.read()

oauth_dict = {
    'access_token': 'rE9DzJExEOKjydJJIwIvAigGfrNrJOhK',
    'access_token_secret': 'rXiVQ9jies7jgH1QruHR1wg5H3bInSnc',
    'consumer_key': 'test',
    'key_cert': key_cert_data
}
auth_jira = JIRA(JIRA_URL, oauth=oauth_dict)

auth_jira.projects()


# jirashell -s http://localhost:8080 -od -ck "test" -k jira.pem -pt

# Create a public key pair using openssl
# openssl genrsa -out private.pem 2048
# openssl rsa -in private.pem -outform PEM -pubout -out public.pem
# Create an application in JIRA, enter random url, go to incoming oauth tab, type consumer key as you like, enter public key created in previous state, save it.
# Run jirashell -s https:/awesome.company.com -od -ck "<consumer key>" -k private.pem -pt and follow instructions
#
#


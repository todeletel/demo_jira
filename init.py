# http://jira.readthedocs.io/en/latest/ Python JIRA Library is the easiest way to automate JIRA.
from jira import JIRA
JIRA_URL = "http://118.25.22.36:8080"
JIRA_USER = "trace_tristan"
JIRA_PASS = "senge2018"

auth_tuple = (JIRA_USER, JIRA_PASS)
jira = JIRA(JIRA_URL, basic_auth=auth_tuple)


def create_issue(project_key_or_id, summary, desc):
    new_issue = jira.create_issue(project=project_key_or_id, summary=summary,
                                  description=desc, issuetype={'id': '10001'})


def show_all_project():
    print '--------project---------'
    projects = jira.projects()
    for p in projects:
        print(p.name, p.id)
    print '------------------------'
    p=jira.project(10000)
    print p

def show_issue_types():
    issue_types = jira.issue_types()
    print(issue_types[0].name)


if __name__ == '__main__':
    show_all_project()

    project_id = 10000
    summary = 'new sdl leak'
    desc = "a vul bug"
    create_issue(project_id, summary, desc)
    show_issue_types()
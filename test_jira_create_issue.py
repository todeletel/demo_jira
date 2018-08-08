# -*- coding: utf-8 -*

from init import jira


def test_show_all_project():
    projects = jira.projects()
    print(projects)


def test_show_issue_types():
    issue_types = jira.issue_types()
    print(issue_types)


def test_create_issue(summary,desc):
    project_id = 10008
    issue_type_id ='10001'

    new_issue = jira.create_issue(project=project_id, summary=summary,
                                  description=desc, issuetype={'id': issue_type_id})

if __name__ == '__main__':
    test_show_all_project()
    test_show_issue_types()
    test_create_issue(summary=u"oauth",
                      desc=u"完成oauthapi调研")
from init import jira


def test_show_all_project():
    projects = jira.projects()
    print(projects)


def test_show_issue_types():
    issue_types = jira.issue_types()
    print(issue_types)


def test_create_issue():
    project_id = 10001
    issue_type_id ='10001'
    summary = 'sdl test demo'
    desc = 'a big leak'
    new_issue = jira.create_issue(project=project_id, summary=summary,
                                  description=desc, issuetype={'id': issue_type_id})

if __name__ == '__main__':
    test_show_all_project()
    test_show_issue_types()
    test_create_issue()
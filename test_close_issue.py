from init import jira

def finish_issue(issue, status):
    jira.transition_issue(issue, status)

# issue=10001
# print(jira.issue(10001))
# transitions = jira.transitions(issue)
# t=[(t['id'], t['name']) for t in transitions]
# print t
finish_issue('JIRA-2', '21')
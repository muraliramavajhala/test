from jira import JIRA

options={'https://jira.mckesson.com:8443'}
jira = JIRA(options, basic_auth=('e2bmeek','xxx'))

issue = jira.issue('MI-333')

print(issue.fields.project.key) 
print(issue.fields.issuetype.name) 
print(issue.fields.reporter.displayName)
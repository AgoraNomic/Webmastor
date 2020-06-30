import sys
from datetime import datetime, timezone

monthshorts = ["jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

with open('Changelog.md') as f:
    changelog = f.read()

with open('Directory') as f:
    directory = f.read()
    
with open('WarningsAndErrors') as f:
    warnlog = f.read()

now = datetime.now(timezone.utc)

timestamp = (str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute))

preamble = "Welcome! This is the Webmastor's homepage, currently maintained by the inaugural Agoran Webmastor, nch. Below is a 'live' version of the Webmastor's report."

with open('docs/index.md', 'w') as f:
    f.write(preamble + "\n" + "\n")
    f.write("**Last Updated: " + timestamp + " (UTC)**\n\n")
    f.write(directory)
    f.write("\n")
    f.write(warnlog)
    f.write("\n")
    f.write(changelog)
    f.write("\n")

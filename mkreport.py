import sys
from datetime import datetime, timezone

with open('Directory') as f:
    directory = f.read()

with open('WarningsAndErrors') as f:
    warnlog = f.read()

now = datetime.now(timezone.utc)

# How many previous months listed (including this one)
history_len = 2
history = []

for i in range(history_len):
    history.append(now.month-i)
    
changelogs = []

# TODO: fix for year threshold
for j in history:
    changelogfile = "changelogs/" + str(now.year) + "-" + str(j).zfill(2) + ".txt"
    with open(changelogfile) as f:
        changelogs.append(f.read())

timestamp = (str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute))

preamble = "Welcome! This is the Webmastor's homepage, currently maintained by the inaugural Agoran Webmastor, nix. Below is a 'live' version of the Webmastor's report."

with open('docs/index.md', 'w') as f:
    f.write(preamble + "\n" + "\n")
    f.write("**Last Updated: " + timestamp + " (UTC)**\n\n")
    f.write(directory)
    f.write("\n")
    f.write(warnlog)
    f.write("\n")
    f.write("+---------+\n")
    f.write("|Changelog|\n")
    f.write("+---------+\n\n")
    # TODO: Add link to full changelog and autogenerate it
    for i in changelogs:
        f.write(i)
        f.write("\n")

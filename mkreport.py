import sys
from datetime import datetime, timezone

with open('Directory') as f:
    directory = f.read()

with open('WarningsAndErrors') as f:
    warnlog = f.read()

now = datetime.now(timezone.utc)

# How many months listed (including this one)
history_len = 2
history = []

for i in range(history_len):
    history.append(now.month-i)
    
changelogs = []

# Code for to find previous months and years specified by history_len. Over engineered to work for an arbitrary number of months back
for i in range(history_len):
    month = (now.month - i) % 12

    # because 12 (24, 36, etc) modulus 12 is 0, hardcode that 0s are 12s. Makes sense!
    if month==0:
        month = 12
    
    # Calculate the year for the given month
    if (now.month - i) == 0:
        year = now.year-1
    elif (now.month - i) < 0:
        year = now.year + (now.month - i) // 12
    else:
        year = now.year
    
    print(month)
    print(year)

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

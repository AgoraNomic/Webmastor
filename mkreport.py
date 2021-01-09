import sys
from datetime import datetime, timezone

with open('Directory') as f:
    directory = f.read()

with open('WarningsAndErrors') as f:
    warnlog = f.read()

now = datetime.now(timezone.utc)

# How many months listed (including this one)
history_len = 2
    
changelogs = []

# Find previous months and years specified by history_len.
for i in range(history_len):
    month = (now.month - i) % 12
    
    years_back = 0
    if i >= now.month:
        years_back = (i // 12) + 1
    
    if month == 0:
        month = 12
        
    cl_filename = "changelogs/" + str(now.year - years_back) + "-" + str(month).zfill(2) + ".txt"
    
    with open(cl_filename) as f:
        changelogs.append(f.read())

timestamp = (str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2))

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

import random

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

lines_added_per_user = {}
with open('testfile.txt', 'r', encoding='utf8') as file:
    commit_lines = file.read().split('commit')
    for commit in commit_lines[1:]:
        lines = commit.strip().split('\n')
        try:
            user = lines[1].split(':')[1].strip()
            user=user[0:user.find('<')].lower().replace(' ','')
        except:
            pass
        for line in lines[4:]:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                if parts[2][:5] != '':
                    added = int(parts[0].replace('-', '0')) #+ int(parts[1].replace('-', '0'))
                else:
                    added = 0
                if user in lines_added_per_user:
                    lines_added_per_user[user] += added
                else:
                    lines_added_per_user[user] = added

users = list(lines_added_per_user.keys())
lines_added = list(lines_added_per_user.values())




num_colors = len(users)
colors = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(num_colors)]
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(lines_added, labels=users, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'}, colors=colors)
plt.title('Lines Added by User')
plt.tight_layout()
plt.show()
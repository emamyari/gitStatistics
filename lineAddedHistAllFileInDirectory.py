import random
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

lines_added_per_user = {}
for filename in os.listdir("C:\\BO"):
    f = os.path.join("BO", filename)
    with open(f, 'r', encoding='utf8') as file:
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
                        added = int(parts[0].replace('-', '0')) + int(parts[1].replace('-', '0'))
                    else:
                        added=0
                    if user in lines_added_per_user:
                        lines_added_per_user[user] += added
                    else:
                        lines_added_per_user[user] = added

users = list(lines_added_per_user.keys())
lines_added = list(lines_added_per_user.values())



num_colors = len(users)
colors = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(num_colors)]
plt.figure(figsize=(10, 6))
plt.bar(users, lines_added, edgecolor='black', color=colors)
plt.xlabel('Users')
plt.ylabel('Lines Added')
plt.title('Lines Added by User')
for i in range(len(users)):
    plt.text(i, lines_added[i], format(lines_added[i], ','), ha='center', va='bottom')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
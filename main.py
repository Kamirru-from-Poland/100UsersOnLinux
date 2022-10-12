import os #IMPORTANT - run as a root
for i in range(1,101):
    print(os.system("useradd -p 123 u" + (str(i))))
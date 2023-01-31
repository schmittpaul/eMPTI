import subprocess


file1 = open('tranco_list.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    print(line.strip())
    subprocess.call(['browsertime', '--android', '-n', '3', '--timeouts.browserStart', '5000', '--timeouts.pageLoad', '20000', '--maxLoadTime', '25000', line.strip()])

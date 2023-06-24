import subprocess

# file1 = open('tranco_list.txt', 'r')
# file1 = open('valid_tranco_list.txt', 'r')
file1 = open('short_tranco_list.txt', 'r')
Lines = file1.readlines()

def is_valid_url(url):
    cmd = "find ./browsertime-results-norelay/{} -type f | wc -l".format(url.split("//")[1].strip())
    process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           encoding='utf-8')
    # wait for the process to terminate
    out, err = process.communicate()
    out = out.strip()
    if len(out) > 0 and int(out) == 2:
        return True
    return False

for line in Lines:
    url = line.strip()
    if is_valid_url(url):
        print(url)
        subprocess.call(['browsertime', '--android', '-n', '1', '--timeouts.browserStart', '5000', '--timeouts.pageLoad', '20000', '--maxLoadTime', '25000', line.strip()])

import json
import urllib.request

req = urllib.request.Request("http://www.reddit.com/r/saber/about.json")
req.add_header("User-agent",
               "Windows; U; Windows NT 5.1; de; rv:1.9.1.5)\
               Gecko/20091102 Firefox/3.5.5")

resp = urllib.request.urlopen(req)
content = resp.read().decode()
x = json.loads(content)

about = x["data"]["description"]


def find_best_girl():
    return about[about.find("1. Saber is Best")+3:211]

best_girl = find_best_girl()

print(best_girl)
print("")
input("press any key to exit...")
sys.exit(0)
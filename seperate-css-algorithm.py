app = input("Enter the app name: ")
filename = input("Enter the HTML file name: ")

f1 = open(app + "/templates/" + app + "/" + filename, "r", encoding="utf8")
f2 = open(app + "/static/" + app + "/" + "main-" + filename[:-5] + ".css", "w", encoding="utf8")
s = f1.read()

while "<style" in s:
    i1 = s.find("<style")
    i2 = s.find(">", i1)
    j1 = s.find("</style", i2)
    j2 = s.find(">", j1)
    f2.write(s[i2 + 1:j1])
    s = s[:i1] + s[j2 + 1:]

f1.close()
f2.close()

f1 = open(app + "/templates/" + app + "/" + filename, "w", encoding="utf8")
f1.write(s)
f1.close()

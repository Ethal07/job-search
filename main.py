import httpx
import selectolax

with open("./url.txt", "r") as file:
    url = file.readline()

jobs = []

with open("./jobs.txt", "w", encoding="utf-8") as file:
    for i in range(1, 50):

        html = httpx.get(url + str(i)).text

        parser = selectolax.lexbor.LexborHTMLParser(html)
                
        nodes = parser.css('[data-testid^="searchResultCard-"]')

        for j in range(0, len(nodes) - 1):
            job = nodes[j].text(separator="\n")[0:-19]
            if not job in jobs:
                if not (i == 0 and j == 0):
                    file.write("\n")
                file.write(job)
                jobs.append(job)
            else:
                continue
            file.write("\n")

print(len(jobs))
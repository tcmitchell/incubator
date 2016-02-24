1. Get a list of aggregates in JSON format

    http://genimondev.uky.edu/API/info/?q={"obj":{"type":"aggregate"},"output":"json","infoType":"simple"}

2. Get a list of aggregates in XML format -- this produces an error

    http://genimondev.uky.edu/API/info/?q={"obj":{"type":"aggregate"},"output":"xml","infoType":"simple"}

3. Get information about a single aggregate by short name in JSON format

    http://genimondev.uky.edu/API/info/?q={"obj":{"id":["max-ig"],"type":"aggregate"},"output":"json","infoType":"simple"}

4. Get information about a single aggregate by short name in XML format

    http://genimondev.uky.edu/API/info/?q={"obj":{"id":["max-ig"],"type":"aggregate"},"output":"xml","infoType":"simple"}

5. Get information about a single aggregate by URN in JSON format -- this produces an empty list

    http://genimondev.uky.edu/API/info/?q={"obj":{"id":["urn:publicid:IDN+instageni.maxgigapop.net+authority+cm"],"type":"aggregate"},"output":"json","infoType":"simple"}

6. Get information about a single aggregate by URN in XML format

    http://genimondev.uky.edu/API/info/?q={"obj":{"id":["urn:publicid:IDN+instageni.maxgigapop.net+authority+cm"],"type":"aggregate"},"output":"xml","infoType":"simple"}

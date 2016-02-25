# Example Queries

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

7. Get event information about an aggregate

    http://genimondev.uky.edu/API/data/?q={"obj":{"id":["max-ig"],"type":"aggregate"},"output":"xml","ts":{"gte":1456260153962,"lt":1456263753962}}

8. Just is_available for an aggregate

    http://genimondev.uky.edu/API/data/?q={"eventType":["is_available"],"obj":{"id":["max-ig"],"type":"aggregate"},"output":"xml","ts":{"gte":1456345005000,"lt":1456348605000}}

 * I couldn't get "output":"json" to work with this query, the document was empty

# Slivers

1. List all slivers in XML

    http://genimondev.uky.edu/API/info/?q={"obj":{"type":"sliver"},"output":"xml","infoType":"simple"}

2. Info about a single sliver in json

    http://genimondev.uky.edu/API/info/?q={"obj":{"id":["lan.sdn.uky.edu_sliver_38337"],"type":"sliver"},"output":"json","infoType":"detailed"}

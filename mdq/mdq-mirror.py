import hashlib
import json
import os
import time
import urllib
import urllib2


ENTITY_LIST_URL = 'http://mdq-beta.incommon.org/global/x-entity-list'

# Note: leave off the trailing slash, a slash will be appended
MDQ_BASE = 'http://mdq-beta.incommon.org/global'

# Fetch the entity list
# JSON decode it
# For each entry:
#       Download the data via the entityID
#       Generate a filename by escaping the forward slashes
#       Put the data in the file
#       Generate a SHA1 hash of the entityID
#       Create a symlink from the hash to the file


def hash_filename(entityID):
    hash_hex = hashlib.sha1(entityID).hexdigest()
    return "{sha1}%s" % hash_hex


def entity_filename(entityID):
    "Replace slashes with %2F"
    return entityID.replace('/', '%2F')


def fetch_url(url):
    x = urllib2.urlopen(url)
    raw_data = x.read()
    x.close()
    return raw_data


def fetch_metadata(base, entityID):
    quoted_entity = urllib.quote(entityID, safe='')
    url = '/'.join([base, 'entities', quoted_entity])
    print url
    return fetch_url(url)


def fetch_json(url):
    raw_data = fetch_url(url)
    data = json.loads(raw_data)
    return data


def main():
    all_entities = fetch_json(ENTITY_LIST_URL)
    for entity in all_entities:
        entityID = entity['entityID']
        e_fname = entity_filename(entityID)
        h_fname = hash_filename(entityID)
        print "%s\t%s\t%s\t" % (entityID, e_fname, h_fname)
        metadata = fetch_metadata(MDQ_BASE, entityID)
        with open(e_fname, 'wb') as f:
            f.write(metadata)
        os.symlink(e_fname, h_fname)
        time.sleep(5)

main()

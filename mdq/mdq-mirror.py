import hashlib
import json
import urllib
import urllib2


ENTITY_LIST_URL = 'http://mdq-beta.incommon.org/global/x-entity-list'
MDQ_BASE = 'http://mdq-beta.incommon.org/global/'

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


def fetch_metadata(base, entityID):
    pass


def fetch_all_entities(url):
    x = urllib2.urlopen(url)
    raw_data = x.read()
    x.close()
    data = json.loads(raw_data)
    return data


def main():
    all_entities = fetch_all_entities(ENTITY_LIST_URL)
    for entity in all_entities:
        entityID = entity['entityID']
        e_fname = entity_filename(entityID)
        h_fname = hash_filename(entityID)
        print "%s\t%s\t%s\t" % (entityID, e_fname, h_fname)

main()

# these modules are used to access and authenticate with your database cluster:
from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator

# specify the cluster and specify an authenticator containing a username and password to be passed to the cluster.

cluster = Cluster('couchbase://localhost', ClusterOptions(PasswordAuthenticator('Administrator', 'password')))

# following a successful authentication, a bucket can be opened.
# access a bucket in that cluster

bucket = cluster.bucket('default')
coll = bucket.default_collection()

# following a successful authentication, a bucket can be accessed to perform operations

# JSON Object for user0001
user0001 = {
    "firstName" : "Perry",
    "lastName" : "Mason",
    "email" : "perry.mason@acme.com",
    "tagLine" : "Who can we get on the case?",
    "type" : "user"
}

#insert a single document
rv = bucket.upsert('newDoc', user0001)
print (rv)

#insert multiple documents

user0002 = {
    "firstName" : "Major",
    "lastName" : "Tom",
    "email" : "major.tom@acme.com(opens in new tab)",
    "tagLine" : "Send me up a drink",
    "type" : "user"
}
user0003 = {
    "firstName" : "Jerry",
    "lastName" : "Wasaracecardriver",
    "email" : "jerry.wasaracecardriver@acme.com(opens in new tab)",
    "tagLine" : "el sob number one",
    "type" : "user"
}

rv = bucket.upsert_multi({'newDoc2':user0002, 'newDoc3':user0003})
print (rv)

# first lookup using the key
rv = bucket.get('newDoc2')
print(rv.value)

#first secondary lookup to find all users with email ending in @acme.com

query_result = cluster.query('SELECT * FROM `default` WHERE email LIKE $email', QueryOptions(named_parameters={'email': "%@acme.com"}))
for row in query_result:
   print(row) 
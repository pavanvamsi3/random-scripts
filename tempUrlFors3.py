import boto

con = boto.connect_s3()
bucket = con.get_bucket('bucket-name')
key = bucket.get_key('key-name')
tempurl = key.generate_url(expires_in=86400) #Time in seconds
print tempurl

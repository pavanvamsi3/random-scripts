# This script is used to give a signed url 
# for a particular object in S3. We can mention
# expiry time in seconds. After that the data is safe
# only the download link is expired.
# PS: Make sure you put the S3 Credentails in ~/.boto file.
import boto

con = boto.connect_s3()
bucket = con.get_bucket('bucket-name')
key = bucket.get_key('key-name')
tempurl = key.generate_url(expires_in=86400)
print tempurl

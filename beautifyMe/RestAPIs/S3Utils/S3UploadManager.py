from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings
from mimetypes import MimeTypes

class S3UploadManager:
     Connection = S3Connection(settings.ACCESS_KEY,settings.PASS_KEY)
     S3Bucket = Connection.create_bucket(settings.S3BUCKET_NAME)
     
     def uploadFileToS3(self ,filename,content):
          try :
               mime= MimeTypes.guess_type(filename)[0]
               k=Key(S3UploadManager.S3Bucket)
               k.key= filename
               k.set_metadata("Content-Type", mime)
               k.set_contents_from_string(content)
               k.set_acl("public-read")
          except Exception as e:
               raise type(e)(e.message)
# AWS/Buckets setup 
1. sign up for an aws account (requires credit card, no payment)
2. search s3 or go to link https://s3.console.aws.amazon.com/s3/home
3. create a bucket - only add bucket name, leave the rest as defaults
4. next we'll head over to the IAM (Identity & Access Management) link https://console.aws.amazon.com/iamv2/home
5. Select groups on the left menu
   1. create new group
   2. pick a name & skip the rest
6. Select Policies on the left menu
   1. click on the JSON editor and paste the following - IMPORTANT: switch 'your-bucket-name' with what we named our bucket in step 3
   2. after pasting and editing the policy we will click next, add name & description & save
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
```

7. Navigate back to Groups
   1. select your previously created group
   2. click permissions tab
   3. upper right corner there is a dropdown with 'Add permissions', click 'Attach policies'
   4. add your previously created policy to the group, save.
8. Navigate to Users
   1. Create a new user
   2. make sure to select access type of "Programmatic access"
   3. next step add the user to the group before saving


# Django/heroku settings
1. install the following packages:
   ```
    pip install boto3 django-storages
   ```
   NOTE: don't forget to update your requirements.txt
2. we need to update our INSTALLED_APPS with `'storages'`
3. to our heroku config vars & local_settings.py we will add the following:
   ```
   AWS_ACCESS_KEY_ID = 'your-iam-user-access-key'
   AWS_SECRET_ACCESS_KEY = 'your-iam-user-secret-access-key'
   AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
   AWS_URL = 'https://your-bucket-name.s3.amazonaws.com/'
   ```
4. to our settings.py we will add some non-sensitive information
    ```
    AWS_DEFAULT_ACL = None
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    ```
5. and into the except from our local_settings import we can add these:
    ```
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_URL = os.environ.get('AWS_URL')
    ```
6. next we update some settings to point Django to use the bucket for media storage
   1. if you have other settings for MEDIA_URL, MEDIA_ROOT we will delete/comment them
    ```
    MEDIA_URL = AWS_URL + '/media/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    ```

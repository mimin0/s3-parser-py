This is a simple python script that can help you to find the path to the right s3 object (text ones) by searching keyword

### Prerequisites
1. You have installed _python3_, _boto3_ lib and [_awscli_ tool](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) installed as well.

1. The script assumes you have configured authentication separately. more [details on AWS doc](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

1. Your IAM user has at least the next allowed [actions `s3:ListBucket` and `s3:GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) toward to the target bucket. 

1. The bucket policy must allow your IAM user to reach objects inside this bucket

### Notes
1. the current version of script works with the first 1000 objects in the target bucket. 
1. amount of objects as well as size of each one text object will have an impact on script execution time and **aws monthly bill**

### Test cases
1. 10 log files with 1MB each one. execution time ~1.5s
1. 100 log files with 1MB each one. execution time ~9.5s
1. 10 log files with 10MB each one. execution time ~4s


### How To Run

Run python script with args `bucket_name` and `keyword`
example:

        # python3.7 main.py 'my-s3-bucket' 'POST /bricks-'
        web/logs/apache.log
        web/logs/apache1.log
        web/logs/apache2.log
        web/logs/apache3.log
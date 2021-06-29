import boto3
import sys
import time

s3 = boto3.resource('s3')
client = boto3.client('s3')


def get_objects_list(bucket) -> list:
    my_bucket = s3.Bucket(bucket)

    keys_list = []

    for file in my_bucket.objects.all():
        # ignore folders key or empty folders
        if not file.key.endswith('/'):
            keys_list.append(file.key)

    return keys_list


def find_keyword(object_list, bucket, keyword) -> list:
    matched_objects = []
    for object in object_list:
        obj = s3.Object(bucket, object)
        # TODO: handle case if object is not a text file
        body = obj.get()['Body'].read().decode('utf-8')

        # if keyword in target file then add filename to the list
        if keyword in body:
            matched_objects.append(object)

    return matched_objects


start_time = time.time()
# check input args
try:
    bucket_name = sys.argv[1]
    looking_keyword = sys.argv[2]
except(IndexError):
    print(">> the script expects 2 arguments! e.g. main.py 'my-s3-bucket' 'my-keyword'")
    sys.exit()

# get all objects at target s3 bucket. return max 1000 objects. TODO: need to use paginator instead
all_objects = get_objects_list(bucket_name)

# find matches in text files
target_files = find_keyword(all_objects, bucket_name, keyword=looking_keyword)
for i in target_files:
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))

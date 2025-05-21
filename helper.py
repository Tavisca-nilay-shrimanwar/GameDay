from utils import exception_handler, logger
import boto3
import json
import subprocess
import sys


class Helper:
    def __init__(self):
        self.s3 = boto3.client("s3")

    @exception_handler
    def save_to_s3(self, bucket, key, data):
        return self.s3.put_object(
            Body=json.dumps(data),
            Bucket=bucket,
            Key=key,
        )

    @exception_handler
    def execute_script(self, script_name):
        process = subprocess.Popen(["python", "test.py"], stdout=sys.stdout, stderr=sys.stderr, text=True, shell=True)
        process.wait()
        return_code = process.returncode
        if return_code == 0:
            logger.info("Script executed successfully.")
        else:
            raise Exception("Execute script failed.")


helper = Helper()
#helper.execute_script()

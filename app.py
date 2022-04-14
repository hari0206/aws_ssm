import os
from dotenv import load_dotenv
import boto3

load_dotenv()

#To load the credentials from env 
secret_id = os.getenv('ACCESS_ID')
secret_key = os.getenv('ACCESS_KEY')
region = os.getenv('region')

# to connect aws ssm
client = boto3.client('ssm',region_name=region, aws_access_key_id = secret_id, aws_secret_access_key = secret_key)

# to get one mentioned parameter
response = client.get_parameters(
    Names = ['/DEV/MY_APP/PORT', '/DEV/MY_APP/PORT1'], WithDecryption = True
)

# to get multiple parameters using path 
response = client.get_parameters_by_path(
    # Names = ['/DEV/MY_APP/PORT', '/DEV/MY_APP/PORT1'], WithDecryption = True
    Path = '/DEV', WithDecryption = True, Recursive = True
)

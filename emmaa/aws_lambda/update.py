import boto3
from os import path
from zipfile import ZipFile

HERE = path.dirname(path.abspath(__file__))


def upload_function():
    """Upload the lambda function by pushing a zip :ile to Lambda.
    
    This function pre-supposes you are running from the same directory that
    contains the lambda script, which should be named: `lambda_script.py`.
    """
    lamb = boto3.client('lambda')
    with ZipFile(path.join(HERE, 'lambda.zip'), 'w') as zf:
        zf.write('./script.py')

    with open(path.join(HERE, 'lambda.zip'), 'rb') as zf:
        ret = lamb.update_function_code(ZipFile=zf.read(),
                                        FunctionName='emmaa-analysis')
        print(ret)
    return


if __name__ == '__main__':
    upload_function()

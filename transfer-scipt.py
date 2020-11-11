import json
import subprocess

api_fetch_file = 'api-fetch.json'

def fetch():
    gitlab_api_token_old='xxxxxxxx'
    project_url_old='https://<gitlab-instance-old.com>/api/v4/projects/<old-project-id>/variables/'

    out = 'curl -s -f --header \'PRIVATE-TOKEN: '+gitlab_api_token_old+'\' '+project_url_old+' > '+api_fetch_file
    print(out)
    stream = subprocess.Popen(out, shell=True)
    stream.wait()

def push():
    gitlab_api_token_new='yyyyyy'

    project_url_new='https://<gitlab-instance-new.com>/api/v4/projects/<new-project-id>/variables/'

    android_env_vars = json.loads(open(api_fetch_file).read())

    for x in android_env_vars:

        out = 'curl --request POST --header \'PRIVATE-TOKEN: '+gitlab_api_token_new+'\' '
        out += project_url_new
        for key in x:
            out+=' --form "'+key+'='+str(x[key])+'"'

        stream = subprocess.Popen(out, shell=True)
        stream.wait()
        print(out)

fetch()
push()

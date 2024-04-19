import json
import requests
import pprint
url = 'http://133.92.147.232:7777/api/llm'

#llm_type = 'tinyllama-1.1b-chat-v1.0.Q4_K_M'
llm_type = 'phi-2.Q4_K_M'

test_info = {
    'llm_type':llm_type,
    'llm_input_type':'ai_assistant',
    'text':'What Japanese movies do you recommend that make you cry?',
    'max_tokens':100,
    'end_texts':['\n']
}

print('post text')
pprint.pprint(test_info, sort_dicts=False)
ret = requests.post(url, json.dumps(test_info))
print('this is', ret)
ret_info = json.loads(ret.text)

print('respons text')
pprint.pprint(ret_info, sort_dicts=False)

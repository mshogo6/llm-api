from fastapi import FastAPI
from pydantic import BaseModel

import app.llama_cpp_switch as llama_cpp_switch
class Info(BaseModel):
    """
    Attributes
    ----------
    llm_type : str
        modelsディレクトリに入っているファイル名。拡張子はいらない
    llm_input_type : str
        LLMの入力の前につける文章の種類。そのまま(raw)の文章をいれると、変な答えが返ってくるため、よく使う文章をllama_cpp_swithcに追加して、分岐させている。
    text : str
        LLMの入力文章
    max_tokens : str
        LLMが返すトークン数の最大数
    end_texts : str
        これで指定した文字をLLMが出力したら、LLMの出力を止める。通常は改行コード('\n')などを指定。
    """
    llm_type: str
    llm_input_type : str
    text: str
    max_tokens: int
    end_texts : list
app = FastAPI()

@app.post('/api/llm')
async def llm(info: Info):
    ret_text = ''
    if info.llm_input_type == 'ai_assistant':
        ret_text = llama_cpp_switch.call_llm_system_user_assistant(info.llm_type, info.text, info.max_tokens, info.end_texts)
    if info.llm_input_type == 'raw':
        ret_text = llama_cpp_switch.call_llm(info.llm_type, info.text, info.max_tokens, info.end_texts)
    ret = {
        'text':ret_text
    }
    return ret

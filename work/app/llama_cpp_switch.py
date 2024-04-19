from llama_cpp import Llama

def call_llm(llm_type: str, text:str, max_tokens: int, end_texts: str):
    """
    生の文章でLLMを呼び出す。

    Parameters
    ----------
    llm_type : str
        modelsディレクトリに入っているファイル名。拡張子はいらない
    text : str
        LLMの入力文章
    max_tokens : int
        LLMが返すトークン数の最大数
    end_texts : str
        これで指定した文字をLLMが出力したら、LLMの出力を止める。通常は改行コード('\n')などを指定。

    Returns
    -------
    out_text : str
        返答テキスト
    """
    llm = Llama(f'models/{llm_type}.gguf')
    output = llm(text, max_tokens=max_tokens, stop=end_texts, echo=True)
    out_text = output['choices'][0]['text']
    return out_text


def call_llm_system_user_assistant(llm_type: str, text:str, max_tokens: int, end_texts: str):
    """
    チャット形式の文章でLLMを呼び出す。

    Parameters
    ----------
    llm_type : str
        modelsディレクトリに入っているファイル名。拡張子はいらない
    text : str
        LLMの入力文章
    max_tokens : int
        LLMが返すトークン数の最大数
    end_texts : str
        これで指定した文字をLLMが出力したら、LLMの出力を止める。通常は改行コード('\n')などを指定。

    Returns
    -------
    out_text : str
        返答テキスト
    """
    llm = Llama(f'models/{llm_type}.gguf')
    prompt = (
        '<|system|>\n'
        'You are an excellent AI assistant.\n'
        '<|user|>\n'
        f'{text}\n'
        '<|assistant|>\n'
    )
    end_texts += ['<|system|>', '<|user|>', '<|assistant|>']
    output = llm(prompt, stop=end_texts, max_tokens=max_tokens)
    out_text = output['choices'][0]['text']
    return out_text

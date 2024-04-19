FROM python:3.10-slim

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt update && apt install -y libopenblas-dev ninja-build build-essential pkg-config
RUN python -m pip install --upgrade pip pytest cmake scikit-build setuptools sse-starlette pydantic-settings starlette-context

RUN apt-get -y install git

RUN pip install -U pip &&\
 pip install --no-cache-dir fastapi uvicorn requests

RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama_cpp_python --verbose

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7777", "--reload"]

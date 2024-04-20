DIR='./work/models'

cd $DIR
echo "current dir is '`pwd`'"

echo "Downloading phi-2"
wget -q https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf

echo "Downloading TinyLlama"
wget -q https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

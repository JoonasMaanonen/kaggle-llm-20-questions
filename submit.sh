SUB_NAME="llama-3-8b-instruct-baseline"
MODEL_FOLDER_PATH="models/Meta-Llama-3-8B-Instruct/"
export KAGGLE_KEY=~/.kaggle/kaggle.json
SUB_FOLDER=submissions/$SUB_NAME/submission.tar.gz

echo "Running eval..."

echo "Creating the submission..."


mkdir submissions/$SUB_NAME


# Pip install libs that are not in Kaggle by default.
# Dependencies (uv for speed)
pip install uv==0.1.45 # uv is faster pip install

pip install -U --platform=manylinux1_x86_64  --platform=manylinux_2_17_x86_64 --only-binary=:all:  --target lib outlines==0.0.43

tar --use-compress-program='pigz --fast' \
    -cf $SUB_FOLDER \
    --dereference \
    bots \
    $MODEL_FOLDER_PATH \
    util \
    data_models \
    main.py \
    lib


echo "Submitting via the Kaggle CLI..."
kaggle competitions submit -c llm-20-questions -f $SUB_FOLDER -m $SUB_NAME

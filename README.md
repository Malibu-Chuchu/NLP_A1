# NLP Assignment1 That's What i like
## st124952 Patsachon Pattakulpong
## What you going to get from me! 😊
In this project i will find the top10 similar words! 

# This is my model comparison and analysis
## Model Comparison and Analysis

| Model             | Window Size | Training Loss | Training Time | Syntactic Accuracy | Semantic Accuracy |
|-------------------|-------------|---------------|---------------|--------------------|-------------------|
| Skipgram (model 1)          | 2     | 9.559290        | 5m 41s      | 0.00%            | 0.00%           |
| Skipgram (NEG) (model 2)    | 2     | 2.230449        | 5m 35s       | 0.00%            | 0.00%           |
| Glove (model 3)            | 2     | 0.131319       | 1m 6s      | 0.00%            | 0.00%           |
| Glove (Gensim) (model 4)    | -     | -       | -       | 55.45%            | 93.87%           |

## Correlation Scores

| Model               | Skipgram (model 1)  | Skipgram (NEG) (model 2) | Glove (model 3)  | Glove (Gensim) (model 4) |
|---------------------|-----------|----------------|-------|----------------|
| MSE            | -0.0100   | -0.0562        | -0.0735 | 0.6019      |

- In this scenario, firstly i want to choose model4 which is GloVe(Gensim) but the Keyvector has no attributes for word embedding.
So, my conclusion i will choose Skipgram model which is model1. It has the least negative correlation among the four, indicating it may slightly outperform the others in aligning with others data.

## How to run the application:
- python app.py

## My Application Demo
<img width="1440" alt="Screenshot 2568-01-20 at 2 00 32 AM" src="https://github.com/user-attachments/assets/e7212d11-1bd2-4a0a-a0ab-8ebdbd782ca1" />


## References
1. https://arxiv.org/pdf/1301.3781.pdf
2. https://aclanthology.org/D14-1162.pdf
3. https://www.fit.vutbr.cz/˜imikolov/rnnlm/word-test.v1.txt
4. http://alfonseca.org/eng/research/wordsim353.htm/




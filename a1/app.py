from flask import Flask, render_template, request, jsonify
import torch
import numpy as np
import json
from skipgram import Skipgram

app = Flask(__name__)

with open("/Users/maliboochuchu/Desktop/AIT/nlp/a1/word2index.json", "r") as f:
    word2index = json.load(f)

with open("/Users/maliboochuchu/Desktop/AIT/nlp/a1/vocab.json", "r") as f:
    vocabs = json.load(f)

vocab_size = len(word2index)
embedding_size = 2
model = Skipgram(vocab_size, embedding_size)

# Load the entire model
model_path = "/Users/maliboochuchu/Desktop/AIT/nlp/a1/Skipgram_Model.bin"
model.load_state_dict(torch.load(model_path))
model.eval()

def get_embed(model, word):
    try:
        index = word2index.get(word, word2index.get('<UNK>'))  # Handle unknown words gracefully
        word_tensor = torch.LongTensor([index])
        embed_c = model.embedding_center(word_tensor)
        embed_o = model.embedding_outside(word_tensor)
        embed = (embed_c + embed_o) / 2
        return embed[0][0].item(), embed[0][1].item()
    except Exception as e:
        raise ValueError(f"Error getting embedding for '{word}': {str(e)}")

def cosine_similarity(A, B):
    dot_product = np.dot(A.flatten(), B.flatten())
    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)
    return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0.0

def search_similar_context(input_word, model, vocabs, word2index, top_n=10):
    try:
        # Get embedding for the input word
        input_embed = get_embed(model, input_word)
        input_embed = np.array(input_embed)  # Ensure it's a NumPy array

        word_similarities = {}
        for word in vocabs:
            try:
                word_embed = get_embed(model, word)
                word_embed = np.array(word_embed)  # Ensure it's a NumPy array
                similarity = cosine_similarity(input_embed, word_embed)
                word_similarities[word] = similarity
            except Exception as e:
                # Ignore words with errors during embedding calculation
                print(f"Skipping word '{word}' due to error: {str(e)}")

        # Sort words by similarity in descending order
        sorted_similarities = sorted(word_similarities.items(), key=lambda x: x[1], reverse=True)
        filtered_words = [word for word, _ in sorted_similarities if word != input_word]

        # Return the top N most similar words
        return filtered_words[:min(top_n, len(filtered_words))]

    except KeyError:
        return "This word is not in the vocabulary. Please try a new word."
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            input_data = request.get_json()
            input_word = input_data.get("search", "").strip()
            if not input_word:
                return jsonify({"error": "Input word cannot be empty."}), 400

            similar_contexts = search_similar_context(input_word, model, vocabs, word2index)
            return jsonify(similar_contexts)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__, static_folder='.')

# Load pre-trained model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set pad_token_id to eos_token_id
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

@app.route('/api/perform_action', methods=['POST'])
def perform_action():
    data = request.get_json()
    action = data['action']

    # Encode the action
    inputs = tokenizer.encode(action, return_tensors='pt', padding=True, truncation=True)
    attention_mask = inputs.ne(tokenizer.pad_token_id).long()

    # Generate AI response with attention mask
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({'response': response})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
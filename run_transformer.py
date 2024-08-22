import sys
from transformers import TFAutoModelForCausalLM, AutoTokenizer # this alreafy knows to use metal, bc it uses the install tensorflow repo, which i installed the metal pluggin to. 
import tensorflow as tf # this tensorflow is set up with metal. so both of these reference it

# transformer_metal.py

def run_transformer(prompt):
    # Your existing logic for processing the prompt
    print(f"Received prompt: {prompt}")
    # Add the rest of your processing logic here
    tokenizer = AutoTokenizer.from_pretrained('gpt2')
    model = TFAutoModelForCausalLM.from_pretrained('gpt2')

    # Define input text
    input_text = prompt

    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors='tf')

    # Generate text using the model
    # output = model.generate(input_ids, max_length=100, num_return_sequences=1) OLD

    # Tokenize the input text
    attention_mask = tf.ones_like(input_ids)

    output = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=100,
            num_return_sequences=1,
            repetition_penalty=1.2,
            temperature=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Simulate some output
    output = f"Processed prompt: {generated_text}"
    
    return output

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        print(run_transformer(prompt))
    else:
        print("No prompt provided.")
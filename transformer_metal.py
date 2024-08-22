from transformers import TFAutoModelForCausalLM, AutoTokenizer # this alreafy knows to use metal, bc it uses the install tensorflow repo, which i installed the metal pluggin to. 
import tensorflow as tf # this tensorflow is set up with metal. so both of these reference it

"""
if i can track down all of the code involved in this, like the smallest amount of code possible, just what is needed, then i will be able to understand how to translate it better
"""

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = TFAutoModelForCausalLM.from_pretrained('gpt2')

# Define input text
input_text = "what is the universe?"

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
print(generated_text)
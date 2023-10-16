import torch
import openai

# Set up your OpenAI API credentials
openai.api_key = ''

def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the GPT-3 model, e.g., 'text-davinci-003'
        prompt=prompt,
        max_tokens= 150  # Adjust the desired length of the generated text
    )
    return response.choices[0].text.strip()

# Function to embed the watermark in the text
def embed_watermark(original_text, watermark):
    # Convert the watermark to binary
    watermark_binary = ''.join(format(ord(char), '08b') for char in watermark)

    # Embed the watermark using zero-width characters
    zero_width_chars = ['\u200B', '\u200C', '\u200D']
    watermarked_text = original_text

    for bit in watermark_binary:
        zero_width_char = zero_width_chars[int(bit)]
        watermarked_text += zero_width_char

    return watermarked_text

# Function to check if a text contains a watermark
def contains_watermark(watermarked_text):
    
    zero_width_chars = ['\u200B', '\u200C', '\u200D']
    watermark_binary = ''

    for char in watermarked_text:
        if char in zero_width_chars:
            bit = str(zero_width_chars.index(char))
            watermark_binary += bit

    watermark = ''.join(chr(int(watermark_binary[i:i+8], 2)) for i in range(0, len(watermark_binary), 8))
    return watermark

# Example usage
prompt = input("Enter a prompt: ")
watermark = "richpp"

# Generate text based on a prompt
original_text = generate_text(prompt)
print("Text generated by GPT-3:", original_text)



# Embed the watermark in the text
watermarked_text = embed_watermark(original_text, watermark)
print("\nWatermarked text is -")
print(watermarked_text)

# Check if the watermarked text contains the watermark
extracted_watermark = contains_watermark(watermarked_text)

print("\nExtracted watermark:", extracted_watermark)



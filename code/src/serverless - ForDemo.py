
def read_docx_to_string(file_path):
    # Open the Word document
    doc = Document(file_path)

    # Initialize an empty string to hold the content
    full_text = ""

    # Loop through all paragraphs and append them to the string
    for para in doc.paragraphs:
        full_text += para.text + "\n"  # Add a newline after each paragraph

    return full_text


# Replace with the path to your Word document
file_path = 'data/Adjustment.docx'
doc_text = read_docx_to_string(file_path)

file_path = 'data/AUTransfer.docx'
doc_text += "\n" +read_docx_to_string(file_path)

file_path = 'data/ClosingNotice-ReallocationFees.docx'
doc_text += "\n" +read_docx_to_string(file_path)

file_path = 'data/InputRequest.docx'
doc_text += "\n" +read_docx_to_string(file_path)

# here we need to provide the api key for the LLM interface, I have removed it for security purpose
client = InferenceClient(

)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": doc_text
        }
    ]
)

print(completion.choices[0].message['content'])
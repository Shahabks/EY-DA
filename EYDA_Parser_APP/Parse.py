import os, sys
import argparse
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
load_dotenv()

from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader

def load_parsing_instruction(filepath):
    if not filepath:
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading the prompt instruction file '{filepath}': {e}")
        sys.exit(1)

def main():
    parser_arg = argparse.ArgumentParser(description="Parse PDF documents into markdown with noise cleaned.")
    parser_arg.add_argument("--prompt", help="Path to prompt_inst.txt file (optional)", default=None)
    parser_arg.add_argument("--input", help="Path to the input PDF file", required=True)
    parser_arg.add_argument("--output", help="Path for the output markdown file (optional)", default=None)
    args = parser_arg.parse_args()

    # Load prompt instruction if provided
    prompt_instruction = load_parsing_instruction(args.prompt)
    if prompt_instruction:
        print(f"Using custom prompt instruction from: {args.prompt}")
    else:
        print("No prompt file provided. Running without custom instructions.")

    # Set your API key for Llama Cloud
    LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY", "llx-XXXXlO")
    #MML_API_KEY = os.getenv("MML_API_KEY", "sk-proj-xxxxxx")  

    # Build parser parameters; include custom prompt if available.
    parser_kwargs = {
        "api_key": LLAMA_CLOUD_API_KEY,
        "result_type": "markdown",
        "language": "ja",
        "premium_mode": True,
        "parse_page_with_lvm": True,
        "vendor_multimodal_model_name": "openai-gpt4o",
        #"vendor_multimodal_api_key":MML_API_KEY,
        "structured_output": True,
        "preserve_layout_alignment_across_pages": True,
        "extract_layout": True,
        "adaptive_long_table": True,
    }
    if prompt_instruction:
        parser_kwargs["user_prompt"] = prompt_instruction

    # Instantiate the parser
    text_parser = LlamaParse(**parser_kwargs)

    # Set up the file extractor for PDF files
    file_extractor = {".pdf": text_parser}

    # Define the input file (PDF)
    input_files = [args.input]

    # Parse the document(s)
    documents = SimpleDirectoryReader(input_files=input_files, file_extractor=file_extractor).load_data()

    # Define the output file path.
    if args.output:
        output_file = args.output
    else:
        output_dir = os.path.dirname(os.path.abspath(args.input))
        base = os.path.splitext(os.path.basename(args.input))[0]
        output_file = os.path.join(output_dir, base + "-parsed_output.md")

    # Save the parsed content to the output file.
    with open(output_file, "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.text + "\n\n")

    print(f"Parsed document saved to: {output_file}")

if __name__ == "__main__":
    main()
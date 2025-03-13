import PyPDF2
import os

# Get the current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in the input directory
input_dir = os.path.join(current_dir, "input")
print(f"Input directory: {input_dir}")
print("Files in input directory:")
for file in os.listdir(input_dir):
    print(f"  - {file}")
    # Try to open each PDF file that matches our target
    if "LLMs" in file and file.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, file)
        print(f"\nFound matching PDF: {pdf_path}")
        print(f"File exists: {os.path.exists(pdf_path)}")
        
        try:
            pdf = PyPDF2.PdfReader(pdf_path)
            print(f"Number of pages: {len(pdf.pages)}")
            
            # Extract text from all pages
            all_text = ""
            for i in range(len(pdf.pages)):
                print(f"Extracting page {i+1}/{len(pdf.pages)}...")
                text = pdf.pages[i].extract_text()
                all_text += text + "\n\n"
            
            # Save the extracted text to a file
            with open("pdf_content.txt", "w", encoding="utf-8") as f:
                f.write(all_text)
            print("\nExtracted text saved to pdf_content.txt")
            
            # Print a sample of the content
            print("\nSample of extracted content:")
            print(all_text[:500])
            
        except Exception as e:
            print(f"Error: {e}") 
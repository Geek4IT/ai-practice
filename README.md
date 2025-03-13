# AI Practice: PDF to Beautiful Web Converter

A toolkit for extracting content from PDF files and transforming it into beautifully designed, responsive web pages.

## 🌟 Project Overview

This project provides a streamlined workflow for:
1. Extracting text content from PDF files
2. Processing and cleaning the extracted text
3. Generating visually appealing, responsive web pages from the content

The generated web pages feature modern design principles, responsive layouts, and both light and dark mode support.

## 📁 Project Structure

```
.
├── input/                  # Directory for source PDF files
│   ├── Building effective agents _ Anthropic.pdf
│   ├── Here's how I use LLMs to help me write code.pdf
│   └── v0_prompt.txt
├── output/                 # Directory for generated files
│   ├── agents_pdf/         # Batch-processed PDF content
│   ├── *.html              # Generated web pages
│   └── *.txt               # Extracted text content
├── extract_pdf.py          # Basic PDF text extraction script
├── extract_agents_pdf.py   # Advanced PDF extraction with batching
├── prompt_to_website.md    # Design prompt for web page generation
└── venv/                   # Python virtual environment
```

## 🚀 Features

- **PDF Text Extraction**: Extract text from PDF files with proper formatting
- **Batch Processing**: Process large PDFs in manageable batches to avoid memory issues
- **Text Cleaning**: Remove unprintable characters and fix encoding issues
- **Beautiful Web Page Generation**: Convert extracted content into visually stunning web pages
- **Responsive Design**: Web pages work perfectly on all devices (mobile, tablet, desktop)
- **Dark/Light Mode**: Automatic theme switching based on system preferences with manual override

## 🛠️ Usage

### Setting Up

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install PyPDF2
   ```

### Extracting Text from PDFs

Basic extraction:
```
python extract_pdf.py
```

Advanced extraction with batching:
```
python extract_agents_pdf.py
```

### Generating Web Pages

1. Place your PDF files in the `input/` directory
2. Run the extraction script to generate text content
3. Use the design prompt in `prompt_to_website.md` with an AI assistant to generate HTML files
4. Find the generated web pages in the `output/` directory

## 🧩 Web Page Design Features

- Modern, magazine-style layout
- Carefully selected typography for optimal readability
- Visual hierarchy through thoughtful use of font sizes, weights, and colors
- Responsive design that works on all devices
- Dark/light mode support
- Micro-interactions for enhanced user experience
- Data visualizations (where appropriate)
- Supplementary information and resources

## 📝 License

[Your chosen license]

## 🙏 Acknowledgements

- [PyPDF2](https://github.com/py-pdf/PyPDF2) for PDF processing
- [Tailwind CSS](https://tailwindcss.com/) for styling
- [Font Awesome](https://fontawesome.com/) for icons
- [Mermaid.js](https://mermaid.js.org/) for diagrams 
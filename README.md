# Document-summarizer

# Text Summarizer

This Python script utilizes the tkinter library to create a simple graphical user interface (GUI) for summarizing text content. The summarization is performed using a pre-trained BERT-based model for summarization from the transformers library, introducing elements of Machine Learning (ML) and Natural Language Processing (NLP).

## Dependencies
Make sure you have the required libraries installed. You can install them using the following commands:

```bash
pip install tkinter transformers beautifulsoup4 requests
```

## Usage

1. **Run the Script:**
   Execute the script in a Python environment:

   ```bash
   python gui.py
   ```

2. **GUI Overview:**
   - The GUI includes two input sections: one for summarizing webpages by providing a URL, and the other for summarizing manually entered documents.
   - Enter the URL of a webpage in the designated entry field and click the "Summarize Webpage" button to retrieve summaries of the linked content.
   - Alternatively, enter the document text manually in the provided entry field and click the "Summarize Document" button to generate a summary.

3. **Webpage Summarization:**
   - The script uses BeautifulSoup to extract all anchor tags (`<a>`) from the provided URL.
   - It then summarizes the text content of each link using the pre-trained BERT-based summarization model.
   - The results, including link text, URL, and summary, are displayed in the result section.

4. **Document Summarization:**
   - For manual document summarization, enter the document text in the specified entry field.
   - Click the "Summarize Document" button to obtain a summary of the entered document.

5. **Result Display:**
   - The summarized content is displayed in a scrollable text area, allowing easy reading of the results.

## Important Notes:
- The summarization model used is "sshleifer/distilbart-cnn-12-6."
- The maximum and minimum length, length penalty, number of beams, and early stopping parameters are set for optimal ML and NLP-based summarization performance. Feel free to adjust these values based on your preferences.

## Acknowledgments:
- The summarization model is powered by the transformers library.
- BeautifulSoup is used for web scraping.
- The GUI is created using the tkinter library.

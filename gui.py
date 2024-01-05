import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# Load pre-trained BERT summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

def get_webpage_summary(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')
    summaries = []

    for link in links:
        text = link.string
        if not text:
            continue
        summary = summarizer(text, max_length=170, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)
        summaries.append(f"Link text: {text}\nURL: {link.get('href')}\nSummary: {summary[0]['summary_text']}\n\n")

    return summaries

def summarize_document(document):
    summary = summarizer(document, max_length=170, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]["summary_text"]

def process_url():
    url = url_entry.get()
    if url:
        summaries = get_webpage_summary(url)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        for s in summaries:
            result_text.insert(tk.END, s)
        result_text.config(state=tk.DISABLED)

def process_document():
    document_text = document_entry.get(1.0, tk.END)
    if document_text:
        summary = summarize_document(document_text)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Document:\n{document_text}\n\nSummary:\n{summary}")
        result_text.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Text Summarizer")

# URL input
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()
url_button = tk.Button(root, text="Summarize Webpage", command=process_url)
url_button.pack()

# Document input
document_label = tk.Label(root, text="Enter Document:")
document_label.pack()
document_entry = scrolledtext.ScrolledText(root, width=60, height=10)
document_entry.pack()
document_button = tk.Button(root, text="Summarize Document", command=process_document)
document_button.pack()

# Result display
result_text = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
result_text.pack()

root.mainloop()

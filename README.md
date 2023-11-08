# Libre AI Chatbot

## Introduction
This project is designed to provide a simple and interactive way to learn about Libre cryptocurrency through an AI-powered chatbot. The chatbot is built using a combination of OpenAI's GPT models, and Gradio for the user interface, providing users with accurate and instant responses based on Libre's official documentation.

## Overview
The Libre AI Chatbot is a wrapper around OpenAI's ChatGPT that provides users with the ability to inquire about the Libre cryptocurrency. It utilizes an indexing and retrieval system to fetch information from Libre's official documentation, which was systematically collected via a scraping script. The chatbot serves as a bridge between users and complex technical data, offering a conversational interface that simplifies the process of understanding Libre's underlying principles, technology, and functionalities. It's important to note that this system is not an open-source language model itself but leverages OpenAI's pre-trained models to interpret and respond to user queries about Libre.

![Libre Chatbot Example](/Users/argishtiovsepyan/Desktop/WORK/libre-chat/images "Libre AI Chatbot")

## Features
- Scraping of Libre's documentation to gather detailed and up-to-date information.
- A chat interface to ask questions and receive answers quickly.
- Answers generated by an AI model trained with the scraped documentation.

## How It Works
The project consists of two main parts:

1. **Scraper**: A Python script using Selenium to navigate through specified Libre websites and to save the content as PDFs in a local directory.

2. **Chatbot**: A Python application that constructs an index from the scraped data and provides a web interface using Gradio where users can ask questions and receive answers.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.6+
- Selenium
- ChromeDriver (for Selenium)
- Gradio
- OpenAI API access

## Future Work
This ChatGPT wrapper for Libre cryptocurrency represents just the initial phase of a larger ambition to enhance user accessibility to crypto-related information. Future developments will explore the integration of open-source language models, potentially utilizing Hugging Face's robust offerings or leveraging OpenAI's systems that permit the fine-tuning of existing language models. The goal is to incrementally build a more sophisticated and tailored chatbot that can offer richer interactions, learn from user queries, and provide even more nuanced information. Further exploration will also involve enhancing the retrieval mechanisms and potentially training a custom language model that better understands the crypto domain's unique vocabulary and concepts. I look forward to evolving this tool into a comprehensive resource for crypto enthusiasts and newcomers alike.

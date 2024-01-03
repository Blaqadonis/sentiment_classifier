# Sentiment Classifier
### Powered by 🅱🅻🅰🆀

![image](https://github.com/Blaqadonis/sentiment_classifier/assets/100685852/3bb89e85-08bd-4752-b983-37218254f30c)  ![image](https://github.com/Blaqadonis/sentiment_classifier/assets/100685852/dafa0505-3ccf-4894-8408-2a928100805c) ![image](https://github.com/Blaqadonis/sentiment_classifier/assets/100685852/9ef4fed6-1bf3-4c02-9cec-cd1e8e35b937)




## Project Overview
The Sentiment Classifier project is a FastAPI-based web application designed to classify product reviews into positive, negative, or neutral categories. It utilizes the Cohere API for natural language processing, allowing for accurate sentiment analysis of user-provided reviews. The application is easy to use with a straightforward interface for inputting reviews and receiving instant classification results.

## Key Features
- **Sentiment Classification:** Classifies reviews into positive, negative, or neutral categories.
- **Cohere Integration:** Leverages Cohere's powerful `embed-english-v3.0` model for analysis.
- **FastAPI Framework:** Utilizes FastAPI for efficient and scalable web service.
- **Interactive API Documentation:** Accessible via `/docs` endpoint for easy testing and interaction.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository:**
``` git clone https://github.com/Blaqadonis/sentiment_classifier ```
2. **Set Environment Variable:**
- Set the `api_key` environment variable for Cohere:
  ```
  export api_key='your_cohere_api_key'
  ```
- Replace `your_cohere_api_key` with your actual API key.

## Usage

1. **Start the Application:**
- Run ``` uvicorn sentiment_classifier:app ``` in your bash terminal.
2. **Access the API Documentation:**
- Navigate to `http://127.0.0.1:8000/docs` in your web browser.
- Use the interactive interface to test the sentiment classifier.

## Screenshots

1. **API Documentation:**
![API Documentation Screenshot](![one](https://github.com/Blaqadonis/sentiment_classifier/assets/100685852/0ddb6c30-8c10-4296-b192-dda517b8bd23)
)

2. **Example of API Usage:**
![API Usage Screenshot](![two](https://github.com/Blaqadonis/sentiment_classifier/assets/100685852/aeba906f-4c3c-47df-ba7d-6f6473c201a3)
)


## Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for more details.


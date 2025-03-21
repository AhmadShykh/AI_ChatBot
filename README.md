# AI Chatbot Project

## Overview
This project consists of an AI chatbot where the frontend is built using React, and the backend uses Flask with a PyTorch-based deep learning model for natural language processing. The React frontend sends requests to the Flask backend, which processes the input and returns chatbot responses.

## Technologies Used

### Frontend (React)
- React.js
- Axios (for HTTP requests)
- Bootstrap/Tailwind (for styling)

### Backend (Flask)
- Flask (Python web framework)
- Flask-CORS (for handling CORS issues)
- PyTorch (for deep learning model)
- NLTK (for text processing)
- Pandas (for data handling)
- BeautifulSoup (for text cleaning)
- Regex (for text preprocessing)

## Project Structure
```
AI-Chatbot-Project/
│── frontend               # React application at the root
│── AI/                # AI code
│   │── model.py            # Neural network model
│   │── test.py       
│   │── train.json      
│   │── clean.py              
│   │── chat.py              
│── README.md               # Project documentation
```

## Installation and Setup

### Backend (Flask)
1. Clone the repository:
   ```sh
   git clone https://github.com/AI_ChatBot.git
   cd AI-Chatbot-Project/AI
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt # If does not exists look at the files
   ```
4. Run the Flask server:
   ```sh
   python .py
   ```
   The server should now be running at `http://127.0.0.1:5000/`

### Frontend (React)
1. Navigate to the frontend directory:
   ```sh
   cd ../
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React app:
   ```sh
   npm start
   ```
   The frontend should now be running at `http://localhost:3000/`

## API Endpoints
### 1. Chat Endpoint
- **URL:** `/chat`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "prompt": "Hello, how are you?"
  }
  ```
- **Response:**
  ```json
  {
    "response": "I am fine, how can I help you?"
  }
  ```

## Model Training
The chatbot uses a deep learning model implemented in PyTorch. To retrain the model:
```sh
python train.py
```
This will save a new model file (`data.pth`) that the Flask server will use.

## Example Image Placeholders
![Model Result](https://github.com/user-attachments/assets/383df9f7-f021-46be-9fe8-5e23b00429f8)
![Website Front Page](https://github.com/user-attachments/assets/f9d30ec3-e431-4170-84c7-3831664fa910)
![Chat Page](https://github.com/user-attachments/assets/f8fff4de-36fe-44e4-b229-cc799e1dfa0e)


## Future Improvements
- Implement a more advanced NLP model like GPT-3.5
- Improve response accuracy
- Deploy the chatbot online

## License
This project is licensed under the MIT License.

## Contributors
- **Ahmad Ali** - Backend Developer
- **Rameez Quereshi** - Frontend Developer
- **Abbaas Rizvi** - Team Lead

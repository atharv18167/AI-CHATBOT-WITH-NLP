# AI-CHATBOT-WITH-NLP

*COMPANY* : CODTECH IT SOLUTION 

*NAME* : ATHARV OMPRAKASH SATARDEKAR

*INTERN ID* : CT04DR2349

*DOMAIN* : PYTHON PROGRAMMING 

*DURATION*: 4 WEEKS 

*MENTOR* : NEELA SANTOSH

##Chatbot Using Natural Language Processing (NLP)

This project is based on building a chatbot using Natural Language Processing (NLP) techniques with the help of Python. A chatbot is a computer program that can interact with users by understanding their text input and responding in a meaningful way. The main aim of this project was to understand how NLP works in practical applications and to implement a working chatbot that can answer user queries using modern NLP libraries instead of simple keyword matching. This project helped me gain hands-on experience in Python programming, text processing, and semantic understanding of language.

The chatbot was developed using the Python programming language and the spaCy library, which is a powerful and widely used NLP toolkit. The chatbot works in a command-line interface where the user types a message and the chatbot responds based on the meaning of the input. Instead of matching exact words, the chatbot uses semantic similarity with word vectors, which allows it to understand different ways of asking the same question. This makes the chatbot more intelligent and closer to real-world chatbot behavior.

In this project, I designed the chatbot using an intent-based approach. All the chatbot knowledge is stored in a JSON file called intents.json. Each intent contains a tag that represents the purpose of the user’s message, a list of example patterns that users might type, and a list of possible responses that the chatbot can give. This structure makes the chatbot easy to understand and easy to expand in the future by simply adding more intents, patterns, and responses without changing the main Python code.

To improve accuracy, I implemented text preprocessing using spaCy. Preprocessing is an important step in NLP because raw user input often contains unnecessary words or variations. In this project, the text is converted to lowercase, stopwords are removed, words are lemmatized to their base form, and only meaningful alphabetic tokens are kept. This preprocessing step ensures that the chatbot focuses on the actual meaning of the sentence rather than unnecessary noise.

The most important part of this project is the use of semantic similarity through spaCy word vectors. I used the en_core_web_md spaCy model, which provides pre-trained word embeddings. Each user input is converted into a numerical vector, and each training pattern from the intents file is also converted into vectors. Cosine similarity is then calculated between the user input vector and all pattern vectors. The chatbot selects the response corresponding to the highest similarity score. This approach allows the chatbot to correctly respond even if the user does not type the exact words present in the training data. For example, the chatbot can understand that “When do you work?” and “What are your office timings?” have similar meanings.

To avoid incorrect answers, I also implemented a similarity threshold. If the similarity score is below a certain value, the chatbot responds with a default fallback message indicating that it did not understand the query. This makes the chatbot more reliable and prevents random or misleading responses. The chatbot runs continuously in a loop until the user types a quit command, making it interactive and easy to use.

Through this project, I learned many important concepts related to NLP and Python development. I learned how Natural Language Processing works, how text preprocessing improves results, and how word embeddings represent language mathematically. I also gained a clear understanding of cosine similarity and how semantic matching is different from simple keyword matching. In addition, I learned how to structure a real project using JSON data, how to manage Python virtual environments, and how to use Git and GitHub for version control and project sharing.

This chatbot project fulfills all the requirements of the given task. It uses an NLP library, answers user queries, and provides a working Python chatbot application. Although the chatbot is simple, it demonstrates real NLP concepts and can be easily extended with more data, more intents, or even a web interface in the future. Overall, this project helped me build a strong foundation in NLP and practical Python programming and increased my confidence in developing real-world applications.


##OUTPUT 
<img width="1350" height="906" alt="Image" src="https://github.com/user-attachments/assets/1896120c-e02b-4cb8-b2c3-9d681791c693" />

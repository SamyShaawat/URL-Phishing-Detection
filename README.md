# URL Phishing Detection Using Llama 2
This project explores the use of deep learning techniques for URL phishing detection. We use a transformer-based model called Llama 2 to classify URLs as phishing or legitimate.  

## Description

In this project, we developed a robust URL phishing detection model using the LLaMA-2, a cutting-edge Large Language Model (LLM) from Meta AI. Phishing attacks, a prevalent cyber threat, deceive users into clicking malicious links disguised as legitimate websites. 

Motivated by the surge in phishing-related crimes and their devastating consequences, we aimed to bolster defenses against these threats. Our approach involved training the LLaMA-2 model on diverse datasets and fine-tuning it with real-world data. Utilizing advanced preprocessing techniques and Byte Pair Encoding for tokenization, we achieved a significant accuracy improvement in phishing detection compared to existing models. Our results demonstrate the LLaMA-2's potential as a highly effective tool for combating URL phishing, reaching a maximum accuracy of 98%.


## Datasets

The project includes the following datasets:

* dataset_11430.csv
* dataset_12500.csv
* dataset_13500.csv
* dataset_20000.csv
* ourdataset_44980.csv

These datasets contain features extracted from URLs, such as the presence of certain keywords, the length of the URL, and the presence of suspicious characters. The datasets are preprocessed using techniques such as shuffling and normalization.
## Model

The `Model` folder contains four Jupyter notebooks, each dedicated to training and evaluating the LLaMA-2 model on different datasets for URL phishing detection.

### Contents:
- `LlaMA-2-7b-hf_11430.ipynb`
- `LlaMA-2-7b-hf_12500.ipynb`
- `LlaMA-2-7b-hf_13500.ipynb`
- `LlaMA-2-7b-hf_20000.ipynb`

### Running the Files:
1. Ensure you have Jupyter Notebook installed.
2. Open Jupyter Notebook.
3. Navigate to the `Model` folder.
4. Click on the desired notebook (`LlaMA-2-7b-hf_*.ipynb`) to open it.
5. Follow the instructions within the notebook to execute the code cells sequentially.
6. Monitor the training progress and evaluation metrics displayed within the notebook.
7. After running all cells, the trained model and evaluation metrics will be saved automatically.

### Ignored Folders and Files:
- `savedModels/`: Contains saved models.
- `savedTokenizers/`: Contains saved tokenizers.
- `savedCheckPoints/`: Contains saved checkpoints.
- `savedLosses/`: Contains saved loss information.
- `savedMetrices/`: Contains saved evaluation metrics.

These folders and files are ignored according to the `.gitignore` configuration within the Model folder.

## API (Rest API Flask)

The `Rest API Flask` folder contains a Flask-based RESTful API for utilizing the trained LLaMA-2 model for URL phishing detection.

### Requirements:
To run the API, ensure you have the following packages installed. You can install them using the provided `requirements.txt` file:

```shell 
pip install -r requirements.txt
``` 


The requirements include:
- flask
- torch
- transformers
- pandas

### Running the API:
1. Navigate to the `Rest API Flask` folder.
2. Ensure the required packages are installed by running the command mentioned above.
3. Execute the `run.py` script to start the Flask server:
```shell
python run.py
```

4. The server will start, and you can access the API endpoints defined in the `routes.py` file.

### Folder Structure:
The `Rest API Flask` folder contains the following structure:
- `run.py`: Entry point for starting the Flask server.
- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `model.py`: Defines functions for loading the trained model.
  - `routes.py`: Defines API endpoints and request handling.
  - `utils.py`: Contains utility functions used within the application.
- `models/`: Ignored folder that contain saved models.
- `tokenizers/`: Ignored folder that contain saved tokenizers.

Ensure that you have the necessary files, folder and dependencies installed to run the API.





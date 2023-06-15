# chatgpt-langchain-demos
This project was first intended to host the demonstration for this Meetup event: https://www.meetup.com/fr-FR/lyonjug/events/293949285/

However, it can also be used as a reference for simple demonstrations of the ChatGPT model (using the OpenAI API or LangChain).

## Setup
This project was tested with Python 3.8.10 on a Linux machine.

Start by creating a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Then install the dependencies:
```bash
pip install -r requirements.txt
```

Finally, copy the `.env.template` file to `.env` and fill in the required values (your OpenAI API key).
```bash
cp .env.template .env
```

Make sure to setup the venv as the default environment in your IDE.

You should now be able to run `demo.ipynb`!

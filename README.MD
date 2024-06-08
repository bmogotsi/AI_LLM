# Artificial Intelligence

## Beginner’s Guide to Building LLM Apps with Python
		By Shittu Olumide, KDnuggets Team Writer on June 6, 2024 in Artificial Intelligence

### Objective
	>> create a simple AI personal assistant APP 
		>>>that generates a response based on the user's prompt 
	>> deploy it to access it globally
	
## Prerequisites
	>> Python (3.5+)
	>> OpenAI
		>>> OpenAI API keys
		
## Installation and updating
	>> pip install openai
	>> pip install langchain
	>> pip install streamlit --upgrade

## Usage


## Deploying your LLM application
 
	Deploying an LLM app means making it accessible over the internet 
	so others can use and test it without requiring access to your local computer. 
	This is important for collaboration, user feedback, and real-world testing, 
	ensuring the app performs well in diverse environments. 

	To deploy the app to the Streamlit Cloud, follow these steps:

		>> Create a GitHub repository for your app. 
			Make sure your repository includes two files: app.py and requirements.txt
		>> Go to Streamlit Community Cloud, 
			https://streamlit.io/cloud
			click the "New app" button from your workspace, 
			and specify the repository, branch, and main file path. 
			branch: https://github.com/bmogotsi/AI_LLM/tree/main/LLMs_app_001
			main file path: /LLMs_app_001/app.py
		>> Click the Deploy button, 
			and your LLM application will now be deployed to Streamlit Community Cloud and can be accessed globally.
			
			
#### Demo of some of the features:
	To test:
		>> Manual (console)
			streamlit run z:\gitProjectFlr\AI_LLM\LLMs_app_001\app.py
		>> Streamlit Community Cloud
			https://streamlit.io/cloud
			see above "Deploying your LLM application"
#### OpenAI
	https://github.com/openai/openai-python
	 OpenAI is a research organization and technology company 
	 that aims to ensure artificial general intelligence (AGI) benefits all of humanity. 
	 One of its key contributions is the development of advanced LLMs such as GPT-3 and GPT-4. 
	 These models can understand and generate human-like text, 
	 making them powerful tools for various applications like chatbots, content creation, and more.
	
	$ pip3 show openai
		Name: openai
		Version: 0.28.0
		Summary: Python client library for the OpenAI API
		Home-page: https://github.com/openai/openai-python
		Author: OpenAI
		Author-email: support@openai.com
		License:
		Location: C:\Users\ben\AppData\Local\Programs\Python\Python311\Lib\site-packages
		Requires: aiohttp, requests, tqdm
		Required-by:

#### LangChain
	https://github.com/langchain-ai/langchain
	LangChain is a framework 
	designed to simplify the development of applications that leverage LLMs. 
	It provides tools and utilities to manage and streamline the various aspects of working with LLMs, 
	making building complex and robust applications easier.
	
	$ pip3 show langchain
		Name: langchain
		Version: 0.0.292
		Summary: Building applications with LLMs through composability
		Home-page: https://github.com/langchain-ai/langchain
		Author:
		Author-email:
		License: MIT
		Location: C:\Users\ben\AppData\Local\Programs\Python\Python311\Lib\site-packages
		Requires: aiohttp, dataclasses-json, langsmith, numexpr, numpy, pydantic, PyYAML, requests, SQLAlchemy, tenacity

#### Streamlit
	
	Streamlit is a powerful and easy-to-use Python library for creating web applications. 
	Streamlit allows you to create interactive web applications using Python alone. 
	You don't need expertise in web development (HTML, CSS, JavaScript) to build functional and visually appealing web apps.
	It's beneficial for building machine learning and data science apps, 
	including those that utilize LLMs.  
	
	$ pip3 show streamlit
		Name: streamlit
		Version: 1.27.1
		Summary: A faster way to build and share data apps
		Home-page: https://streamlit.io
		Author: Snowflake Inc
		Author-email: hello@streamlit.io
		License: Apache License 2.0
		Location: C:\Users\ben\AppData\Local\Programs\Python\Python311\Lib\site-packages
		Requires: altair, blinker, cachetools, click, gitpython, importlib-metadata, numpy, packaging, pandas, pillow, protobuf, pyarrow, pydeck, python-dateutil, requests, rich, tenacity, toml, tornado, typing-extensions, tzlocal, validators, watchdog
		Required-by:

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


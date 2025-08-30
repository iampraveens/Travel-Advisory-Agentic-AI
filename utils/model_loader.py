import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class ConfigLoader:
    
    def __init__(self):
        self.config = load_config()

    def __getitem__(self, key):
        return self.config.get(key)
    
class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai", "google_genai"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()
    
    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading LLM from Groq..............")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI..............")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name=model_name, api_key=openai_api_key)

        elif self.model_provider == "google_genai":
            print("Loading LLM from Google GenAI..............")
            google_api_key = os.getenv("GEMINI_API_KEY")
            model_name = self.config["llm"]["google_genai"]["model_name"]
            llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=google_api_key)
        else:
            raise ValueError(f"Invalid model provider: {self.model_provider}")
        
        return llm
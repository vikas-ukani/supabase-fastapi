import os
import requests
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def callProfileAPI():
    data = supabase.table("profile").select('*').eq('id', 1).single().execute()
    response = requests.get(data.data.get('profile')).json()
    return response

!pip install fastapi uvicorn nest_asyncio pyngrok
from pyngrok import ngrok

# paste your token inside the quotes
ngrok.set_auth_token("39vRAjrjmFQf9lvYlLpXzt34yA0_7zzbha2htKdzgnRaPdsdh")

!pkill -f ngrok
from pyngrok import ngrok
ngrok.kill()

public_url = ngrok.connect(8000)


from pyngrok import ngrok

# paste your token inside the quotes
ngrok.set_auth_token("39vRAjrjmFQf9lvYlLpXzt34yA0_7zzbha2htKdzgnRaPdsdh")

from pyngrok import ngrok
ngrok.kill()

public_url = ngrok.connect(8000)



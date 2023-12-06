import bcrpt 

password= '12345'

bcrpt.hashpw(password, bcrpt.gensalt(12))

def get_hashed_password(plain_text_password):

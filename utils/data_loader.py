import pandas as pd

COMPANY_POSTS_FILE = "data/company_posts.csv"

def load_company_posts():
    try:
        posts = pd.read_csv(COMPANY_POSTS_FILE)
        return posts
    except FileNotFoundError:
        return pd.DataFrame(columns=["Crop", "Quantity", "Contact", "Location"])

def save_company_post(crop, quantity, contact, location):
    try:
        posts = pd.read_csv(COMPANY_POSTS_FILE)
        new_post = pd.DataFrame([[crop, quantity, contact, location]], 
                                columns=["Crop", "Quantity", "Contact", "Location"])
        posts = pd.concat([posts, new_post], ignore_index=True)
    except FileNotFoundError:
        posts = pd.DataFrame([[crop, quantity, contact, location]], 
                             columns=["Crop", "Quantity", "Contact", "Location"])
    posts.to_csv(COMPANY_POSTS_FILE, index=False)
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from textblob import TextBlob
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


# Function to add background image to the page
def set_background(root, image_path):
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Resize to screen size
    bg_image = ImageTk.PhotoImage(bg_image)

    # Create label for the background image and keep a reference to it
    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to avoid garbage collection
    bg_label.place(relwidth=1, relheight=1)  # Make the image cover the whole window
    return bg_label


# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password match
    if username == "vijay" and password == "12345":
        messagebox.showinfo("Login Success", "Welcome to the Home Page")
        root.destroy()  # Close the login window
        home_page()  # Open the home page
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Function to create Home Page with options
def home_page():
    home_root = tk.Tk()
    home_root.title("Home Page")

    # Set background image for the home page
    set_background(home_root, "background.jpg")

    # Create buttons for Analysis, Predictions, and Graphs, centered in the window
    frame = tk.Frame(home_root)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

    btn_analysis = tk.Button(frame, text="Sentiment Analysis", width=30, height=2, command=perform_analysis)
    btn_analysis.grid(row=0, pady=10)


    btn_graphs = tk.Button(frame, text="Graphs", width=30, height=2, command=show_graphs)
    btn_graphs.grid(row=2, pady=10)

    # Exit Button
    btn_exit = tk.Button(frame, text="Exit", width=30, height=2, command=home_root.quit)
    btn_exit.grid(row=3, pady=10)

    home_root.mainloop()


# Load the dataset and perform basic exploration (you can replace 'instagram.csv' with your dataset)
df = pd.read_csv("instagram.csv")


# Clean the review_description text
def cleantext(text):
    text = re.sub(r"@[0-9a-zA-Z]+", "", text)  # Removing mentions
    text = re.sub(r"#", "", text)  # Removing '#' from reviews
    text = re.sub(r"RT[\s]+", "", text)  # Removing Retweets
    text = re.sub(r"https?:\\/\\/S+", "", text)  # Removing hyperlinks
    return text


# Clean the 'review_description' column
df['review_description'] = df['review_description'].apply(cleantext)


# Sentiment Analysis Calculation Function
def calculate_sentiments(ds):
    sentiments = TextBlob(ds['review_description']).sentiment
    return pd.Series([sentiments.subjectivity, sentiments.polarity])


# Applying sentiment analysis to the 'review_description' column
df[['Subjectivity', 'Polarity']] = df.apply(calculate_sentiments, axis=1)


# Function to categorize sentiment polarity into Positive, Negative, or Neutral
def categorize_sentiment(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"


# Apply sentiment categorization
df['Sentiment Analysis'] = df['Polarity'].apply(categorize_sentiment)


# Performing Sentiment Analysis - Main Function
def perform_analysis():
    print(f"Dataset Shape: {df.shape}")
    print(f"Dataset Info: {df.info()}")
    print(f"Missing Values: {df.isna().sum()}")
    print(f"Duplicated Values: {df.duplicated().sum()}")

    # Show sample cleaned data
    print(f"Sample Data: {df.sample(5)}")

    # WordCloud Visualization
    all_words = " ".join(words for words in df['review_description'])
    wordcloud = WordCloud(width=1000, height=1000, random_state=21, max_font_size=119).generate(all_words)
    plt.figure(figsize=(20, 20), dpi=80)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Plot sentiment distribution
    count = df['Sentiment Analysis'].value_counts()
    sns.countplot(data=df, x='Sentiment Analysis')
    plt.show()


# Predictions Function
def make_predictions():
    dataset = df[['review_description', 'Sentiment Analysis']]
    le = LabelEncoder()
    dataset['Sentiment Analysis'] = le.fit_transform(dataset['Sentiment Analysis'])

    # Splitting the dataset into training and test data
    X = dataset['review_description']
    y = dataset['Sentiment Analysis']
    xtrain, xtest, ytrain, ytest = train_test_split(X, y)

    # Define the pipeline
    the_pipeline = Pipeline([
        ('Vectorizing', CountVectorizer()),
        ('TFID', TfidfTransformer()),
        ('classifier', MultinomialNB())
    ])

    the_pipeline.fit(xtrain, ytrain)

    prediction = the_pipeline.predict(xtest)

    z = confusion_matrix(ytest, prediction)
    print("Confusion Matrix:")
    print(z)

    print("Classification Report:")
    print(classification_report(ytest, prediction))


# Graphs Function - Visualization
def show_graphs():
    plt.rcParams['figure.figsize'] = (12, 8)
    sns.kdeplot(data=df, x='Polarity')
    plt.show()

    sns.histplot(data=df, x='Polarity')
    plt.show()

    sns.countplot(data=df, x='Sentiment Analysis')
    plt.show()


# Create the main login page
root = tk.Tk()
root.title("Login Page")

# Set background image for the login page
set_background(root, "background.jpg")

# Create labels and entry widgets for username and password, centered
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame in the window

label_username = tk.Label(frame, text="Username:")
label_username.grid(row=0, pady=5)

entry_username = tk.Entry(frame)
entry_username.grid(row=1, pady=5)

label_password = tk.Label(frame, text="Password:")
label_password.grid(row=2, pady=5)

entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=3, pady=5)

# Create Login and Exit buttons
btn_login = tk.Button(frame, text="Login", width=30, height=2, command=login)
btn_login.grid(row=4, pady=10)

btn_exit = tk.Button(frame, text="Exit", width=30, height=2, command=root.quit)
btn_exit.grid(row=5, pady=10)

# Start the Tkinter event loop for the login page
root.mainloop()

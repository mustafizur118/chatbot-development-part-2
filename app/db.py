from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="23-chatbot",
    user="chatbot23",
    password="1234",
    host="localhost",
    port="5000"
)

# Create a cursor
cur = conn.cursor()


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

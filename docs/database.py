import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="00000000",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def create_tables(conn, cur):
    # Check if tables exist
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'Article')")
    article_exists = cur.fetchone()[0]
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'Topic')")
    topic_exists = cur.fetchone()[0]
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'Event')")
    event_exists = cur.fetchone()[0]
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'ArticleTopic')")
    article_topic_exists = cur.fetchone()[0]
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'ArticleEvent')")
    article_event_exists = cur.fetchone()[0]

    # Create tables if they don't exist
    if not article_exists:
        cur.execute('''
            CREATE TABLE Article (
                article_id SERIAL PRIMARY KEY,
                source_id VARCHAR(255),
                source_name VARCHAR(255),
                author VARCHAR(255),
                title TEXT,
                description TEXT,
                url TEXT,
                url_to_image TEXT,
                published_at TIMESTAMP,
                content TEXT,
                category VARCHAR(255),
                article TEXT,
                title_sentiment FLOAT
            )
        ''')

    if not topic_exists:
        cur.execute('''
            CREATE TABLE Topic (
                topic_id SERIAL PRIMARY KEY,
                topic_name VARCHAR(255)
            )
        ''')

    if not event_exists:
        cur.execute('''
            CREATE TABLE Event (
                event_id SERIAL PRIMARY KEY,
                event_name VARCHAR(255)
            )
        ''')

    if not article_topic_exists:
        cur.execute('''
            CREATE TABLE ArticleTopic (
                article_id INTEGER,
                topic_id INTEGER,
                FOREIGN KEY (article_id) REFERENCES Article(article_id),
                FOREIGN KEY (topic_id) REFERENCES Topic(topic_id)
            )
        ''')

    if not article_event_exists:
        cur.execute('''
            CREATE TABLE ArticleEvent (
                article_id INTEGER,
                event_id INTEGER,
                FOREIGN KEY (article_id) REFERENCES Article(article_id),
                FOREIGN KEY (event_id) REFERENCES Event(event_id)
            )
        ''')
        
        # Commit the transaction and close connection
conn.commit()
conn.close()
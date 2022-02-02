import sqlite3


class Database:
    def __init__(self, path_to_db="files/keywords.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db, isolation_level=None)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def close_db(self):
        return self.connection.close()

    def create_table_keywords(self):
        sql = f'''
        CREATE TABLE keywords (id INTEGER PRIMARY KEY,
                            keyword varchar(255) NOT NULL,
                            chat_id int NOT NULL);
        '''
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_keyword(self, keyword: str, chat_id: int):

        sql = """
        INSERT INTO keywords (keyword, chat_id) VALUES (?, ?) returning id;
        """
        self.execute(sql, parameters=(keyword, int(chat_id)), commit=True)

    def select_all_keywords(self):
        sql = """
        SELECT id ,keyword, chat_id FROM keywords 
        """
        return self.execute(sql, fetchall=True)

    def delete_keyword(self, word_id):
        sql = f"""
        DELETE FROM keywords WHERE id = {word_id} 
        """
        return self.execute(sql, commit=True)

    def create_table_block_keywords(self):
        sql = f'''
        CREATE TABLE blkeywords (id INTEGER PRIMARY KEY,
                            keyword varchar(255) NOT NULL,
                            chat_id int NOT NULL)
        '''
        self.execute(sql, commit=True)

    def add_block_keyword(self, keyword: str, chat_id: int):

        sql = """
        INSERT INTO blkeywords (keyword, chat_id) VALUES (?, ?) returning id
        """
        self.execute(sql, parameters=(f"'{keyword}'", int(chat_id)), commit=True)

    def delete_from_block_list(self, word_id):
        sql = f"""
        DELETE FROM blkeywords WHERE id = {word_id} 
        """
        return self.execute(sql,commit=True)

    def select_all_block_keywords(self):
        sql = """
        SELECT id, keyword, chat_id FROM blkeywords
        """
        return self.execute(sql, fetchall=True)

    def is_keywords_table_created(self):
        sql = """
        SELECT name FROM sqlite_master WHERE type='table' AND name='keywords';
        """
        return self.execute(sql, fetchall=True)

    def is_block_keywords_table_created(self):
        sql = """
        SELECT name FROM sqlite_master WHERE type='table' AND name='blkeywords';
        """
        return self.execute(sql, fetchall=True)

    def create_table_tweets(self):
        pass
        # sql = """
        # CREATE TABLE tweets (id INTEGER PRIMARY KEY,
        #                     keyword varchar(255) NOT NULL,
        #                     chat_id int NOT NULL)
        # """


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")



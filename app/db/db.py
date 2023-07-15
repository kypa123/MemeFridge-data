import psycopg2


class PostgreSQL:
    def __init__(self, connectioninfo: dict):
        self.connectionInfo = connectioninfo

        try:
            self.conn = psycopg2.connect(**self.connectionInfo)
        except Exception as e:
            raise e
        else:
            self.cur = self.conn.cursor()

    def insertData(self, llm: str, datalist: list):
        query = ''
        for data in datalist:
            query += '('
            query += f"'{data[0]}','{data[1]}','{data[2]}','{llm}'"
            query += '),'
        query = query[:-1]
        try:
            res = self.cur.execute(
                f"insert into llm_buzzwords (name, descr, tags, llm) values {query} on conflict do nothing;")

        except Exception as e:
            return e
        else:
            self.conn.commit()
            return 'ok'

    def getRecentData(self, lastid: int) -> list:
        self.cur.execute(f'select * from llm_buzzwords where id > {lastid}')
        return self.cur.fetchall()

    def closeConnection(self):
        self.conn.close()
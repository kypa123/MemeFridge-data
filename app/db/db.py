import psycopg2


class PostgreSQL:
    def __init__(self, connectioninfo: str):
        self.connectionInfo = connectioninfo

        try:
            self.conn = psycopg2.connect(self.connectionInfo)
        except Exception as e:
            raise e
        else:
            self.cur = self.conn.cursor()

    def insertData(self, llm: str, datalist: list):
        for data in datalist:
            self.cur.execute(
                f'insert into llm_buzzwords (name, descr, tags, llm) values ("{data.name}","{data.descr}","{data.tags}","{llm}")')

    def getRecentData(self, lastid: int) -> list:
        self.cur.execute(f'select * from llm_buzzwords where id > {lastid}')
        return self.cur.fetchall()

    def closeConnection(self):
        self.conn.close()

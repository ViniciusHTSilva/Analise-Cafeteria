import psycopg2


conexao = psycopg2.connect("dbname=postgres",
                           user="postgres",
                            password="postgres",
                           host="localhost",
                           port="5433")
cursor = conexao.cursor()

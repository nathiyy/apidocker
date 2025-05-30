from flask import Flask, jsonify
import redis
import requests
import mysql.connector
import traceback
import ast

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/order')
def create_order():
    try:
    # Primeiro tento pegar o produto do cache
        cached = cache.get('product')
        if cached: # Se tiver no cache, já uso direto
            product = ast.literal_eval(cached.decode('utf-8'))
        else: # Senão, pego da API de produtos
            r = requests.get('http://products:3001/products')
            product = r.json()[0]
            cache.set('product', str(product)) # Salvo no cache pra não precisar buscar de novo depois

        # Conectando no banco de dados MySQL
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="example",
            database="ecommerce"
        )
        cursor = db.cursor()
         # Criando a tabela de pedidos, caso ainda não exista
        cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT, quantity INT, total_price INT)")
        cursor.execute("INSERT INTO orders (product_id, quantity, total_price) VALUES (%s, %s, %s)", (product['id'], 2, int(product['price']) * 2))
        db.commit()
        # Fechando conexão com banco
        cursor.close()
        db.close()
       
        # Retornando os dados do pedido em formato JSON
        return jsonify({
            "order_id": 101,
            "product_id": product['id'],
            "quantity": 2, # Aqui eu estou fixando a quantidade como 2 só pra testar
            "total_price": int(product['price']) * 2
        })
    except Exception as e: # Só mostrando o erro no terminal, pra saber o que aconteceu
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__": # Subindo o servidor Flask na porta 3002
    app.run(host='0.0.0.0', port=3002)

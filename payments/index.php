<?php

$request_uri = $_SERVER['REQUEST_URI']; // Pego a URL que foi acessada

if ($request_uri === '/payment') {
    // Faço uma requisição pra API de pedidos pra pegar os dados do pedido
    $orderJson = file_get_contents('http://orders:3002/order');
    $orderData = json_decode($orderJson, true); // transformo o JSON em array

    $response = [  // Simulo um pagamento e retorno a resposta com status "paid"
        'status' => 'paid',
        'order' => $orderData
    ];

    header('Content-Type: application/json'); // Defino o tipo de retorno como JSON
    echo json_encode($response);
} else {
    http_response_code(404); // Se não for a rota certa, retorno erro 404
    echo json_encode(['error' => 'Not found']);
}

# Prueba 2: Panel de ventas

Crea un panel de ventas para la dueña de una pequeña cadena de 4 cafeterías.

Los datos están en `vendas-mini.csv`: los pedidos del período. El archivo está sucio a propósito. Primero límpialo y muestra qué corregiste (qué tipo de problema y cuántas filas de cada uno). Muestra la facturación total del período.

La dueña tiene que ver lo que importa en 5 segundos y poder hacer clic en una cifra para ver las filas que la componen.

Archivo principal: `painel.html`. Tiene que abrirse con dos clics, así que los datos limpios van dentro del propio HTML.

## Esmero
- Haz que se vea realmente bien: quien pase la vista tiene que detenerse y dejar de desplazarse.
- Usa las herramientas y habilidades que tengas (diseño, animación, generador de imágenes). Tú eliges.

## Imágenes (opcional)
- Si esta interfaz genera imágenes, genera como máximo 4 e indica el nombre de archivo de cada una (img1.jpg, img2.jpg...), para que las guarde junto al HTML. En el HTML, usa <img src="img1.jpg"> y muestra un dibujo en SVG o CSS en su lugar si el archivo no existe, para que la página nunca abra con una imagen rota.
- Si no genera, dibuja todo en SVG o CSS dentro del HTML. La prueba vale lo mismo.
- Modo rayos X: la tecla X y un botón pequeño activan los contornos, con un color para cada imagen y otro para cada animación hecha con código, con una etiqueta pequeña en cada uno.

## Cómo entregar (estás en una ventana de chat, sin carpeta)
- Responde con UN archivo HTML completo en un único bloque de código, desde <!doctype html> hasta </html>, con el CSS y JavaScript dentro.
- El archivo tiene que estar completo. Nada de "el resto sigue igual".
- No uses archivos de Internet. Nunca reproduzcas sonido.
- No hagas preguntas. Termina de una vez.
- Después del bloque, en hasta 5 líneas: qué hiciste y cómo abrirlo.

Los datos están abajo, entre las líneas ===. Coloca los datos DENTRO del HTML.

=== vendas-mini.csv ===
pedido,data,loja,produto,qtd,preco,pagamento
50053,2026-08-06,Beira-Rio,Gelado,4,13.50,cartao
50082,2026-08-08,Centro,Café em grão 250g,1,39.90,pix
50193,2026-08-15,Centro,Espresso,1,6.50,pix
50042,2026-08-05,Rodoviária,Bolo de fubá,4,9.50,cartao
50039,2026-08-05,Beira-Rio,Coado,2,8.00,pix
50177,2026-08-14,Centro,Gelado,4,13.50,pix
50130,2026-08-10,Alto da Serra,Gelado,4,13.50,dinheiro
50070,2026-08-07,Beira-Rio,Café em grão 250g,4,39.90,pix
50188,2026-08-14,Alto da Serra,Coado,1,8.00,pix
50187,2026-08-14,Alto da Serra,Gelado,3,13.50,cartao
50119,2026-08-10,Centro,Cappuccino,3,11.00,pix
50020,2026-08-04,Beira-Rio,Latte,2,12.00,pix
50207,2026-08-15,Alto da Serra,Latte,1,12.00,pix
50114,2026-08-09,Alto da Serra,Gelado,4,13.50,dinheiro
50146,2026-08-11,Alto da Serra,Pão de queijo,2,7.00,cartao
50201,2026-08-15,Rodoviária,Cappuccino,3,11.00,pix
50021,2026-08-04,Beira-Rio,Cappuccino,4,R$ 11.00,dinheiro
50169,2026-08-13,Rodoviária,Cappuccino,2,11.00,cartao
50026,2026-08-04,RODOVIÁRIA,Latte,3,12.00,cartao
50091,2026-08-08,Rodoviária,Gelado,2,13.50,dinheiro
50139,2026-08-11,Rodoviária,Café em grão 250g,1,39.90,cartao
50058,2026-08-06,Rodoviária,Espresso,1,R$ 6.50,pix
50190,2026-08-15,Centro,Café em grão 250g,2,39.90,dinheiro
50135,2026-08-11,Centro,Pão de queijo,1,7.00,cartao
50154,2026-08-12,Beira-Rio,Pão de queijo,1,7.00,dinheiro
50079,2026-08-08,Centro,Espresso,3,6.50,cartao
50045,2026-08-05,Alto da Serra,Bolo de fubá,2,9.50,dinheiro
50129,10/08/2026,Alto da Serra,Bolo de fubá,2,9.50,cartao
50024,2026-08-04,Rodoviária,Gelado,1,13.50,pix
50141,2026-08-11,Rodoviária,Gelado,4,13.50,pix
50003,2026-08-03,Centro,Latte,4,12.00,pix
50199,2026-08-15,Beira-Rio,Pão de queijo,2,7.00,cartao
50223,16/08/2026,Alto da Serra,Espresso,1,6.50,cartao
50075,2026-08-07,Alto da Serra,Espresso,3,6.50,cartao
50069,2026-08-07,Beira-Rio,Gelado,4,13.50,dinheiro
50146,2026-08-11,Alto da Serra,Pão de queijo,2,7.00,cartao
50106,2026-08-09,Rodoviária,Gelado,2,13.50,pix
50208,2026-08-15,Alto da Serra,Coado,3,8.00,pix
50049,2026-08-06,Centro,Cappuccino,3,11.00,cartao
50209,2026-08-16,Centro,Coado,2,8.00,cartao
50087,2026-08-08,Beira-Rio,Espresso,3,6.50,pix
50124,2026-08-10,Rodoviária,Gelado,2,13.50,cartao
50076,7 ago 2026,Alto da Serra,Latte,2,12.00,pix
50040,2026-08-05,Beira-Rio,Café em grão 250g,3,39.90,cartao
50145,2026-08-11,Alto da Serra,Café em grão 250g,3,39.90,pix
50066,2026-08-07,Centro,Pão de queijo,2,7.00,cartao
50183,14 ago 2026,Beira-Rio,Bolo de fubá,4,9.50,pix
50152,2026-08-12,Beira-Rio,Coado,1,8.00,pix
50035,2026-08-05,Centro,Bolo de fubá,3,9.50,dinheiro
50222,2026-08-16,Alto da Serra,Gelado,1,13.50,cartao
50140,2026-08-11,Rodoviária,Coado,3,8.00,pix
50057,2026-08-06,Rodoviária,Latte,2,12.00,pix
50068,2026-08-07,Beira-Rio,Latte,3,12.00,dinheiro
50097,2026-08-09,Centro,Latte,1,12.00,pix
50174,2026-08-13,Alto da Serra,Café em grão 250g,4,39.90,pix
50088,08/08/2026,Beira-Rio,Coado,3,8.00,pix
50202,2026-08-15,Rodoviária,Espresso,1,6.50,cartao
50148,2026-08-12,Centro,Gelado,3,13.50,pix
50110,2026-08-09,Rodoviária,Coado,1,8.00,pix
50162,2026-08-13,Centro,Cappuccino,3,11.00,pix
50134,2026-08-11,Centro,Pão de queijo,4,7.00,cartao
50204,2026-08-15,Alto da Serra,Café em grão 250g,1,39.90,cartao
50072,2026-08-07,Rodoviária,Latte,2,12.00,pix
50167,13/08/2026,Beira-Rio,Café em grão 250g,1,39.90,pix
50203,2026-08-15,Rodoviária,Latte,4,12.00,pix
50016,2026-08-04,Centro,Bolo de fubá,3,9.50,pix
50136,2026-08-11,Beira-Rio,Latte,2,12.00,pix
50173,2026-08-13,Alto da Serra,Café em grão 250g,1,39.90,dinheiro
50021,2026-08-04,Beira-Rio,Cappuccino,4,R$ 11.00,dinheiro
50150,2026-08-12,Centro,Gelado,2,R$ 13.50,cartao
50090,2026-08-08,Rodoviária,Pão de queijo,4,7.00,pix
50116,2026-08-10,Centro,Espresso,1,6.50,cartao
50120,2026-08-10,Beira-Rio,Pão de queijo,3,7.00,cartao
50093,2026-08-08,Alto da Serra,Pão de queijo,4,7.00,pix
50115,2026-08-10,Centro,Pão de queijo,3,7.00,pix
50103,2026-08-09,Beira-Rio,Café em grão 250g,2,39.90,cartao
50191,15 ago 2026,Centro,Bolo de fubá,4,9.50,cartao
50099,2026-08-09,Centro,Latte,3,12.00,cartao
50019,4 ago 2026,Centro,Gelado,2,13.50,pix
50031,2026-08-05,Centro,Pão de queijo,3,7.00,pix
50107,2026-08-09,Rodoviária,Coado,4,8.00,pix
50059,2026-08-06,Rodoviária,Bolo de fubá,3,9.50,cartao
50161,2026-08-13,Centro,Pão de queijo,4,7.00,pix
50175,2026-08-13,Alto da Serra,Espresso,3,6.50,pix
50019,4 ago 2026,Centro,Gelado,2,13.50,pix
50164,13 ago 2026,Centro,Café em grão 250g,1,39.90,cartao
50176,2026-08-14,Centro,Coado,4,8.00,pix
50008,3 ago 2026,Beira-Rio,Bolo de fubá,1,9.50,cartao
50221,16 ago 2026,Rodoviária,Latte,4,12.00,pix
50143,2026-08-11,Rodoviária,Coado,4,8.00,pix
50085,2026-08-08,Beira-Rio,Latte,1,12.00,cartao
50030,2026-08-04,Alto da Serra,Gelado,2,R$ 13.50,pix
50216,16/08/2026,Beira-Rio,Espresso,4,6.50,cartao
50013,2026-08-03,Alto da Serra,Latte,1,12.00,pix
50073,2026-08-07,Rodoviária,Café em grão 250g,4,39.90,cartao
50038,2026-08-05,Beira-Rio,Cappuccino,4,11.00,pix
50215,2026-08-16,Beira-Rio,Café em grão 250g,1,39.90,dinheiro
50017,2026-08-04,Centro,Cappuccino,4,11.00,pix
50163,2026-08-13,Centro,Espresso,3,6.50,cartao
50056,2026-08-06,Beira-Rio,Latte,2,12.00,pix
50184,14 ago 2026,Beira-Rio,Pão de queijo,4,7.00,pix
50213,2026-08-16,Centro,Gelado,3,13.50,cartao
50012,2026-08-03,Alto da Serra,Coado,1,8.00,pix
50077,2026-08-07,Alto da Serra,Pão de queijo,1,7.00,cartao
50158,2026-08-12,Alto da Serra,Latte,3,12.00,pix
50065,2026-08-07,Centro,Espresso,3,6.50,cartao
50100,09/08/2026,Centro,Café em grão 250g,4,39.90,pix
50027,2026-08-04,Rodoviária,Cappuccino,1,11.00,cartao
50205,15/08/2026,Alto da Serra,Pão de queijo,1,7.00,cartao
50029,2026-08-04,Alto da Serra,Pão de queijo,4,7.00,pix
50197,2026-08-15,beira-rio ,Café em grão 250g,1,39.90,pix
50004,2026-08-03,Centro,Bolo de fubá,2,9.50,dinheiro
50206,2026-08-15,ALTO DA SERRA,Café em grão 250g,2,39.90,pix
50149,2026-08-12,Centro,Latte,4,12.00,pix
50125,2026-08-10,Rodoviária,Latte,1,12.00,pix
50032,2026-08-05,Centro,Bolo de fubá,4,9.50,pix
50048,2026-08-05,Alto da Serra,Cappuccino,4,11.00,cartao
50054,2026-08-06,Beira-Rio,Latte,3,12.00,cartao
50217,2026-08-16,Beira-Rio,Gelado,4,13.50,pix
50198,2026-08-15,Beira-Rio,Latte,3,12.00,pix
50081,2026-08-08,Centro,Cappuccino,2,11.00,cartao
50007,2026-08-03,Beira-Rio,Coado,3,"8,00",cartao
50179,2026-08-14,Centro,Gelado,1,13.50,cartao
50144,2026-08-11,Alto da Serra,Espresso,4,6.50,cartao
50015,2026-08-04,centro ,Pão de queijo,1,7.00,cartao
50078,2026-08-08,Centro,Bolo de fubá,1,9.50,cartao
50014,2026-08-03,Alto da Serra,Café em grão 250g,4,39.90,pix
50156,2026-08-12,Rodoviária,Cappuccino,4,11.00,cartao
50211,2026-08-16,Centro,Bolo de fubá,2,9.50,pix
50155,2026-08-12,Rodoviária,Latte,2,12.00,dinheiro
50055,2026-08-06,Beira-Rio,Cappuccino,1,11.00,cartao
50101,2026-08-09,Centro,Latte,1,12.00,pix
50127,2026-08-10,Rodoviária,Gelado,2,13.50,cartao
50192,2026-08-15,Centro,Cappuccino,4,11.00,pix
50047,2026-08-05,Alto da Serra,Bolo de fubá,1,9.50,cartao
50165,2026-08-13,centro ,Latte,4,"12,00",pix
50123,2026-08-10,Beira-Rio,Coado,1,8.00,cartao
50098,2026-08-09,Centro,Espresso,4,6.50,cartao
50180,2026-08-14,Centro,Café em grão 250g,4,39.90,pix
50157,2026-08-12,Alto da Serra,Cappuccino,2,11.00,cartao
50166,13 ago 2026,Beira-Rio,Bolo de fubá,4,9.50,pix
50122,2026-08-10,Beira-Rio,Café em grão 250g,1,39.90,pix
50102,2026-08-09,Beira-Rio,Pão de queijo,1,7.00,cartao
50214,2026-08-16,Centro,Espresso,1,6.50,pix
50171,2026-08-13,Rodoviária,Coado,1,8.00,pix
50151,2026-08-12,Centro,Cappuccino,3,11.00,cartao
50117,2026-08-10,Centro,Gelado,2,13.50,pix
50147,2026-08-12,Centro,Espresso,1,6.50,pix
50109,2026-08-09,Rodoviária,Café em grão 250g,4,39.90,pix
50050,2026-08-06,Centro,Cappuccino,2,11.00,pix
50159,2026-08-12,Alto da Serra,Café em grão 250g,2,39.90,pix
50025,2026-08-04,Rodoviária,Coado,1,8.00,pix
50064,2026-08-07,Centro,Café em grão 250g,2,39.90,pix
50033,05/08/2026,Centro,Café em grão 250g,1,39.90,cartao
50006,03/08/2026,Beira-Rio,Espresso,4,6.50,pix
50172,2026-08-13,Rodoviária,Coado,4,8.00,pix
50060,2026-08-06,Rodoviária,Espresso,4,6.50,cartao
50108,2026-08-09,Rodoviária,Coado,4,8.00,cartao
50185,2026-08-14,Rodoviária,Espresso,4,6.50,cartao
50212,2026-08-16,Centro,Latte,1,12.00,cartao
50210,2026-08-16,Centro,Espresso,1,R$ 6.50,pix
50132,2026-08-11,Centro,Café em grão 250g,3,39.90,dinheiro
50126,2026-08-10,Rodoviária,Cappuccino,3,11.00,pix
50061,2026-08-06,Alto da Serra,Latte,1,12.00,pix
50133,2026-08-11,Centro,Espresso,1,6.50,dinheiro
50044,2026-08-05,Rodoviária,Coado,2,8.00,cartao
50080,2026-08-08,Centro,Café em grão 250g,4,39.90,dinheiro
50112,2026-08-09,Alto da Serra,Pão de queijo,3,7.00,pix
50018,2026-08-04,Centro,Pão de queijo,3,7.00,dinheiro
50118,2026-08-10,Centro,Cappuccino,4,11.00,pix
50002,2026-08-03,Centro,Cappuccino,3,11.00,pix
50131,2026-08-11,Centro,Cappuccino,1,11.00,cartao
50195,2026-08-15,Beira-Rio,Pão de queijo,3,7.00,cartao
50052,2026-08-06,Centro,Gelado,1,13.50,cartao
50168,2026-08-13,Beira-Rio,Coado,4,"8,00",pix
50096,2026-08-09,Centro,Cappuccino,1,11.00,cartao
50063,2026-08-07,Centro,Latte,1,12.00,cartao
50005,2026-08-03,Beira-Rio,Cappuccino,4,11.00,pix
50092,2026-08-08,Rodoviária,Coado,2,8.00,cartao
50051,2026-08-06,Centro,Bolo de fubá,4,9.50,pix
50001,2026-08-03,Centro,Espresso,3,6.50,cartao
50128,2026-08-10,Alto da Serra,Café em grão 250g,2,39.90,cartao
50160,2026-08-12,Alto da Serra,Café em grão 250g,2,39.90,cartao
50218,2026-08-16,Beira-Rio,Pão de queijo,2,7.00,pix
50170,2026-08-13,Rodoviária,Cappuccino,2,11.00,pix
50104,2026-08-09, Beira-Rio,Espresso,4,6.50,pix
50037,2026-08-05,Beira-Rio,Bolo de fubá,1,9.50,pix
50009,2026-08-03,Rodoviária,Gelado,1,13.50,cartao
50062,2026-08-06,Alto da Serra,Bolo de fubá,3,9.50,dinheiro
50224,16 ago 2026,Alto da Serra,Espresso,2,6.50,pix
50022,2026-08-04,Beira-Rio,Cappuccino,3,11.00,pix
50084,2026-08-08,Beira-Rio,Cappuccino,2,11.00,cartao
50113,2026-08-09,Alto da Serra,Espresso,3,6.50,cartao
50121,2026-08-10,Beira-Rio,Bolo de fubá,1,9.50,cartao
50042,2026-08-05,Rodoviária,Bolo de fubá,4,9.50,cartao
50036,2026-08-05,Beira-Rio,Café em grão 250g,2,39.90,pix
50219,2026-08-16,Rodoviária,Latte,2,12.00,cartao
50023,2026-08-04,Beira-Rio,Coado,1,8.00,pix
50041,2026-08-05,Beira-Rio,Café em grão 250g,1,39.90,cartao
50083,2026-08-08,Centro,Pão de queijo,1,7.00,cartao
50095,2026-08-08,Alto da Serra,Gelado,2,13.50,pix
50187,2026-08-14,Alto da Serra,Gelado,3,13.50,cartao
50105,2026-08-09,Beira-Rio,Coado,4,8.00,cartao
50220,2026-08-16,Rodoviária,Latte,3,12.00,cartao
50153,2026-08-12,Beira-Rio,Bolo de fubá,2,9.50,cartao
50142,2026-08-11,Rodoviária,Coado,3,8.00,cartao
50194,2026-08-15,Centro,Cappuccino,2,11.00,cartao
50034,2026-08-05,Centro,Pão de queijo,3,7.00,pix
50067,2026-08-07,Beira-Rio,Coado,4,8.00,cartao
50178,2026-08-14,Centro,Gelado,4,"13,50",cartao
50186,2026-08-14,Alto da Serra,Latte,4,12.00,cartao
50189,2026-08-15,Centro,Café em grão 250g,4,39.90,pix
50028,2026-08-04,Alto da Serra,Café em grão 250g,4,39.90,cartao
50137,2026-08-11,Beira-Rio,Espresso,1,6.50,dinheiro
50071,2026-08-07,beira-rio ,Espresso,4,6.50,cartao
50138,2026-08-11,Beira-Rio,Cappuccino,2,11.00,dinheiro
50181,14/08/2026, Beira-Rio,Coado,3,8.00,pix
50043,2026-08-05,Rodoviária,Latte,4,12.00,cartao
50182,2026-08-14,Beira-Rio,Espresso,1,6.50,dinheiro
50196,2026-08-15,Beira-Rio,Espresso,4,6.50,pix
50010,2026-08-03,Rodoviária,Café em grão 250g,1,39.90,pix
50111,2026-08-09,Alto da Serra,Bolo de fubá,1,9.50,dinheiro
50074,2026-08-07,Alto da Serra,Coado,4,8.00,dinheiro
50086,2026-08-08,Beira-Rio,Cappuccino,2,11.00,pix
50089,2026-08-08,Rodoviária,Coado,2,8.00,dinheiro
50094,2026-08-08,Alto da Serra,Bolo de fubá,2,9.50,pix
50046,2026-08-05,Alto da Serra,Latte,3,12.00,cartao
50011,2026-08-03,Rodoviária,Bolo de fubá,1,9.50,cartao
50200,2026-08-15,Rodoviária,Café em grão 250g,3,39.90,cartao
90002,2026-08-06,Centro,TESTE - NAO CONTAR,99,1.00,pix
90001,2026-10-26,Centro,TESTE - NAO CONTAR,99,1.00,pix
=== fin ===

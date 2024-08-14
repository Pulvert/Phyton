{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPoYPoTeeZESaabVVo2vngX"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":8,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"WNoXlN6BDv1T","executionInfo":{"status":"ok","timestamp":1721054958240,"user_tz":-120,"elapsed":221,"user":{"displayName":"Diego","userId":"07408759357351876848"}},"outputId":"601c790c-30ed-4eab-cae5-b103dbc48f01"},"outputs":[{"output_type":"stream","name":"stdout","text":["Tu pedido Pizza Barbacoa ha sido confirmado.\n","Tu pedido Pizza 4 Quesos ha sido confirmado.\n","Tu pedido Pizza Margarita ha sido confirmado.\n","Tu pedido Pizza con Piña ha sido confirmado.\n"]}],"source":["\"\"\"\n"," * Explora el concepto de callback en tu lenguaje creando un ejemplo\n"," * simple (a tu elección) que muestre su funcionamiento.\n"," *\n"," * DIFICULTAD EXTRA (opcional):\n"," * Crea un simulador de pedidos de un restaurante utilizando callbacks.\n"," * Estará formado por una función que procesa pedidos.\n"," * Debe aceptar el nombre del plato, una callback de confirmación, una\n"," * de listo y otra de entrega.\n"," * - Debe imprimir un confirmación cuando empiece el procesamiento.\n"," * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre\n"," *   procesos.\n"," * - Debe invocar a cada callback siguiendo un orden de procesado.\n"," * - Debe notificar que el plato está listo o ha sido entregado.\n","\"\"\"\n","import time\n","import random\n","import threading\n","\n","def mi_callback(resultado):\n","    print(f\"Operación completada con resultado: {resultado}\")\n","\n","def operacion_asincrona(callback):\n","    print(\"Operación asíncrona iniciada...\")\n","    time.sleep(2)  # Simula una operación que toma tiempo\n","    resultado = 42  # Resultado de la operación\n","    callback(resultado)\n","\n","operacion_asincrona(mi_callback)\n","\n","# Extra\n","\n","def ready(a):\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{a} listo!\")\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{a} en mesa!\")\n","\n","def ready(b):\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{b} listo!\")\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{b} en mesa!\")\n","\n","def ready(c):\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{c} listo!\")\n","  random_number = random.randint(1, 10)\n","  time.sleep(random_number)\n","  print(f\"{c} en mesa!\")\n","\n","def order(a,b,c):\n","  print(f\"Oido cocina!, preparamos {a},{b} y {c}\")\n","  ready(a)\n","  ready(b)\n","  ready(c)\n","\n","\n","order(\"Pulpo\",\"Bravas\",\"Calamares\")\n","\n","# Solución\n","\n","\"\"\"\n","Ejercicio\n","\"\"\"\n","\n","def greeting_process(name: str, callback):\n","    print(\"Ejecutando el proceso de saludo...\")\n","    callback(name)\n","\n","def greet_callback(name: str):\n","    print(f\"Hola, {name}!\")\n","\n","greeting_process(\"Brais\", greet_callback)\n","\n","\"\"\"\n","Extra\n","\"\"\"\n","\n","def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):\n","    def process():\n","        confirm_callback(dish_name)\n","        time.sleep(random.randint(1, 10))\n","        ready_callback(dish_name)\n","        time.sleep(random.randint(1, 10))\n","        delivered_callback(dish_name)\n","\n","    threading.Thread(target=process).start()\n","\n","def confirm_order(dish_name: str):\n","    print(f\"Tu pedido {dish_name} ha sido confirmado.\")\n","\n","def order_ready(dish_name: str):\n","    print(f\"Tu pedido {dish_name} está listo.\")\n","\n","def order_delivered(dish_name: str):\n","    print(f\"Tu pedido {dish_name} ha sido entregado.\")\n","\n","order_process(\"Pizza Barbacoa\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza 4 Quesos\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza Margarita\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza con Piña\", confirm_order, order_ready, order_delivered)\n","\n","order_process(\"Pizza Barbacoa\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza 4 Quesos\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza Margarita\", confirm_order, order_ready, order_delivered)\n","order_process(\"Pizza con Piña\", confirm_order, order_ready, order_delivered)"]}]}
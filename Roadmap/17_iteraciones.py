{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNzfPUIe84oGP06hBZrLITk"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"4kwwa5SPrW26","executionInfo":{"status":"ok","timestamp":1720533339526,"user_tz":-120,"elapsed":244,"user":{"displayName":"Diego","userId":"07408759357351876848"}},"outputId":"3693c76f-2f14-42bc-e69a-02068a3892fd"},"outputs":[{"output_type":"stream","name":"stdout","text":["1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","1\n","2\n","3\n","4\n","1\n","2\n","3\n","4\n","1\n","2\n","3\n","4\n","1\n","2\n","3\n","4\n","a\n","b\n","c\n","d\n","1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n","P\n","y\n","t\n","h\n","o\n","n\n","4\n","3\n","2\n","1\n","e\n","m\n","o\n","r\n","u\n","Índice: 0, valor: e\n","Índice: 1, valor: m\n","Índice: 2, valor: o\n","Índice: 3, valor: r\n","Índice: 4, valor: u\n"]}],"source":["\"\"\"\n"," * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir\n"," * números del 1 al 10 mediante iteración.\n"," *\n"," * DIFICULTAD EXTRA (opcional):\n"," * Escribe el mayor número de mecanismos que posea tu lenguaje\n"," * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?\n","\"\"\"\n","\n","# For\n","for x in range (1, 11):\n","  print (x)\n","\n","# While\n","x = 0\n","while x != 10:\n","  x += 1\n","  print(x)\n","\n","# Recursividad\n","def count (a):\n","  if a == 0:\n","    return 1\n","  else:\n","    count(a-1)\n","  print(a)\n","\n","count(10)\n","\n","\n","# Solución\n","\n","\"\"\"\n","Ejercicio\n","\"\"\"\n","# For\n","for i in range(1, 11):\n","    print(i)\n","\n","# While\n","i = 1\n","while i <= 10:\n","    print(i)\n","    i += 1\n","\n","# Recursividad\n","def count_ten(i=1):\n","    if i <= 10:\n","        print(i)\n","        count_ten(i + 1)\n","\n","count_ten()\n","\n","\"\"\"\n","Extra\n","\"\"\"\n","\n","for e in [1, 2, 3, 4]:\n","    print(e)\n","\n","for e in {1, 2, 3, 4}:\n","    print(e)\n","\n","for e in (1, 2, 3, 4):\n","    print(e)\n","\n","for e in {1: \"a\", 2: \"b\", 3: \"c\", 4: \"d\"}:\n","    print(e)\n","\n","for e in {1: \"a\", 2: \"b\", 3: \"c\", 4: \"d\"}.values():\n","    print(e)\n","\n","print(*[i for i in range(1, 11)], sep=\"\\n\")\n","\n","for c in \"Python\":\n","    print(c)\n","\n","for e in reversed([1, 2, 3, 4]):\n","    print(e)\n","\n","for e in sorted([\"m\", \"o\", \"u\", \"r\", \"e\"]):\n","    print(e)\n","\n","for i, e in enumerate(sorted([\"m\", \"o\", \"u\", \"r\", \"e\"])):\n","    print(f\"Índice: {i}, valor: {e}\")\n"]}]}
{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPSxQxmNSYqJYtZZE4UTpaU"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":75,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"fJwRjPHPTjnu","executionInfo":{"status":"ok","timestamp":1722868934196,"user_tz":-120,"elapsed":380,"user":{"displayName":"Diego","userId":"07408759357351876848"}},"outputId":"d7fa3eec-628b-438c-fdb2-5f82c4bce27b"},"outputs":[{"output_type":"stream","name":"stdout","text":["[1]\n","[[1]]\n","[1, 1]\n","[[1], [1, 1]]\n","[1, 2, 1]\n","[[1], [1, 1], [1, 2, 1]]\n","[1, 3, 3, 1]\n","[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]\n","[1, 4, 6, 4, 1]\n","[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]\n"]}],"source":["def pascal_triangle(n):\n","    triangle = []\n","\n","    for row_num in range(n): # Crea un bucle según la cantidad de filas\n","        row = [1] * (row_num + 1)  # Crea una nueva fila con unos\n","        # Se crea una lista de listas [1]\n","\n","        for j in range(1, row_num): # Modifica los unos de la posición \"1\" a la\n","        #posición que representa el número de \"row_num\"\n","            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]\n","\n","        triangle.append(row) #Añade la fila(lista) a la lista triangle\n","        print(row)# Va imprimiendo las filas\n","\n","pascal_triangle(5)\n","\n","\n","\n"]}]}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOKUcjmosmel5d4IF3ZrKmR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/muhammadqodir1313/numpy/blob/main/numpy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c_X7MiP6onwq",
        "outputId": "07609f93-0f14-4d20-c050-9ec2ea257be1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1D Massiv:  [1 2 3 4 5]\n",
            "2D Massiv:\n",
            " [[1 2 3]\n",
            " [4 5 6]]\n",
            "Massivlar yig'indisi:  15\n",
            "O'rtacha:  3.0\n",
            "Ko'paytma:  120\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "\n",
        "#1. Massiv yaratish\n",
        "#Bu Muhammadqodirning ishi\n",
        "array_1d = np.array([1, 2, 3, 4, 5])\n",
        "array_2d = np.array([[1, 2, 3], [4, 5, 6]])\n",
        "#2. Matematik operatsiyalar\n",
        "sum_array = np.sum(array_1d)\n",
        "mean_array = np.mean(array_1d)\n",
        "product_array = np.prod(array_1d)\n",
        "print(\"1D Massiv: \", array_1d)\n",
        "\n",
        "print(\"2D Massiv:\\n\", array_2d)\n",
        "\n",
        "print(\"Massivlar yig'indisi: \", sum_array)\n",
        "\n",
        "print(\"O'rtacha: \", mean_array)\n",
        "\n",
        "print(\"Ko'paytma: \", product_array)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "#1. DataFrame yaratish\n",
        "\n",
        "data = {\n",
        "\n",
        "'Ism': ['Ali', 'Vali', 'Sardor'],\n",
        "\n",
        "'Yoshi': [25, 30, 22],\n",
        "\n",
        "'Shahar': ['Toshkent', 'Samarqand', 'Buxoro']\n",
        "\n",
        "}\n",
        "\n",
        "df=pd.DataFrame (data)\n",
        "\n",
        "#2. Ma'lumotlarni ko'rish\n",
        "\n",
        "print(df)\n",
        "\n",
        "#3. Filtrlash young_people = df [df ['Yoshi'] < 30] print(\"30 yoshdan kichiklar: \\n\", young_people)\n",
        "\n",
        "#4. O'zgartirish\n",
        "\n",
        "df ['Yoshi'] += 1 # Har bir shaxsning yoshini 1 ga oshirish print(\"Yangilangan DataFrame: \\n\", df)\n",
        "\n",
        "#5. CSV formatda saqlash\n",
        "\n",
        "df.to_csv('data.csv', index=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mOuiRCS9rt3Q",
        "outputId": "89142b50-2139-4dd3-aaba-4c9c6d78a4d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "      Ism  Yoshi     Shahar\n",
            "0     Ali     25   Toshkent\n",
            "1    Vali     30  Samarqand\n",
            "2  Sardor     22     Buxoro\n"
          ]
        }
      ]
    }
  ]
}
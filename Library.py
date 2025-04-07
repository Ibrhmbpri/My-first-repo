{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNnlIO2cjxNUj7Andbru0Sz",
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
        "<a href=\"https://colab.research.google.com/github/Ibrhmbpri/My-first-repo/blob/main/Library.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hH5yKT8Hjax_",
        "outputId": "8cae715d-1f1a-4056-a784-90df202b90f4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Books in the Library:\n",
            "1984 by George Orwell\n",
            "To Kill a Mockingbird by Harper Lee\n"
          ]
        }
      ],
      "source": [
        "# library.py\n",
        "\n",
        "class Book:\n",
        "    def __init__(self, title, author):\n",
        "        self.title = title\n",
        "        self.author = author\n",
        "\n",
        "    def display_info(self):\n",
        "        print(f\"{self.title} by {self.author}\")\n",
        "\n",
        "class Library:\n",
        "    def __init__(self):\n",
        "        self.books = []\n",
        "\n",
        "    def add_book(self, book):\n",
        "        self.books.append(book)\n",
        "\n",
        "    def show_books(self):\n",
        "        print(\"Books in the Library:\")\n",
        "        for book in self.books:\n",
        "            book.display_info()\n",
        "\n",
        "# Example usage\n",
        "if __name__ == \"__main__\":\n",
        "    book1 = Book(\"1984\", \"George Orwell\")\n",
        "    book2 = Book(\"To Kill a Mockingbird\", \"Harper Lee\")\n",
        "\n",
        "    library = Library()\n",
        "    library.add_book(book1)\n",
        "    library.add_book(book2)\n",
        "\n",
        "    library.show_books()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "code = \"\"\"\n",
        "class Book:\n",
        "    def __init__(self, title, author):\n",
        "        self.title = title\n",
        "        self.author = author\n",
        "\n",
        "    def display_info(self):\n",
        "        print(f\"{self.title} by {self.author}\")\n",
        "\n",
        "class Library:\n",
        "    def __init__(self):\n",
        "        self.books = []\n",
        "\n",
        "    def add_book(self, book):\n",
        "        self.books.append(book)\n",
        "\n",
        "    def show_books(self):\n",
        "        print(\"Books in the Library:\")\n",
        "        for book in self.books:\n",
        "            book.display_info()\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    book1 = Book(\"1984\", \"George Orwell\")\n",
        "    book2 = Book(\"To Kill a Mockingbird\", \"Harper Lee\")\n",
        "\n",
        "    library = Library()\n",
        "    library.add_book(book1)\n",
        "    library.add_book(book2)\n",
        "\n",
        "    library.show_books()\n",
        "\"\"\"\n",
        "\n",
        "with open(\"library.py\", \"w\") as f:\n",
        "    f.write(code)"
      ],
      "metadata": {
        "id": "anaaIkHnj9Un"
      },
      "execution_count": 2,
      "outputs": []
    }
  ]
}
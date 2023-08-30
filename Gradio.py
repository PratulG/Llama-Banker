{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOANCcBsHpnfTN58WmhPBgT",
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
        "<a href=\"https://colab.research.google.com/github/PratulG/Llama-Banker/blob/main/Gradio.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "b1cPUVM_6f6d"
      },
      "outputs": [],
      "source": [
        "import gradio as gr\n",
        "\n",
        "# Define the function that performs the query\n",
        "def query_document(question):\n",
        "    # Querying the document\n",
        "    response = query_engine.query(question)\n",
        "    return response.response\n",
        "\n",
        "# Define a function to handle the button click\n",
        "def on_button_click(question):\n",
        "    answer = query_document(question)\n",
        "    return answer\n",
        "\n",
        "# Create the Gradio interface\n",
        "iface = gr.Interface(\n",
        "    fn=on_button_click,\n",
        "    inputs=gr.inputs.Textbox(lines=1, label=\"Enter your question\"),\n",
        "    outputs=gr.outputs.Textbox(label=\"Answer\"),\n",
        "    live=True,\n",
        "    capture_session=True,\n",
        "    layout=\"vertical\",  # Arrange components vertically\n",
        "    title=\"Document Query App\",  # Add a title to the app\n",
        "    description=\"Ask questions about the document\",  # Add a description\n",
        "    article=\"This app allows you to ask questions about the document and get answers.\",  # Add an article\n",
        "    examples=[[\"What is the CEO sentiment?\", \"\"]],  # Add example questions\n",
        "    theme=\"default\",  # Choose a theme (optional)\n",
        "    buttons=[\"Get Answer\"],  # Add a button\n",
        "    button_color=\"lightblue\",  # Customize the button color\n",
        ")\n",
        "\n",
        "# Launch the Gradio app\n",
        "iface.launch()"
      ]
    }
  ]
}
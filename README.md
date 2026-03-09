# ChanyoungHan_web_technologies_hand_in_2
ChanyoungHan_web_technologies_hand_in_2

Simple Flask Todo & Memo App

This is a simple web application built with Python (Flask) that allows
users to write a Todo list and a memo, and store personal
information.

Features - Add and delete todo items - Write and save personal memo -
Store name and email information - Simple pastel UI with navigation

Project Structure

project/ app.py requirements.txt

    templates/
        index.html
        memo.html
        info.html

    static/
        style.css

    todos.json
    memo.json
    info.json

Installation

If Flask is not installed: pip install flask

Running the Application

Start the Flask server: python app.py

Open the browser: http://localhost:5000

API Endpoints

Todo GET /todos POST /todos DELETE /todos/

Memo GET /memo-data POST /memo-data

User Info GET /info-data POST /info-data

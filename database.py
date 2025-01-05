import os

import psycopg2
import streamlit as st
from dotenv import load_dotenv
from psycopg2 import sql

from contrato import Vendas

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
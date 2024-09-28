import sys
print("Python version:", sys.version)
print("Starting import process...")

try:
    from flask import Flask, request, jsonify
    print("Flask imported successfully")
    from langchain_community.agent_toolkits import create_sql_agent
    print("create_sql_agent imported successfully")
    from langchain.sql_database import SQLDatabase
    print("SQLDatabase imported successfully")
    from langchain.chat_models import ChatOpenAI
    print("ChatOpenAI imported successfully")
    from sqlalchemy import create_engine
    print("create_engine imported successfully")
    import os
    print("os imported successfully")
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

print("All imports successful")

app = Flask(__name__)

print("Flask app created")

os.environ["OPENAI_API_KEY"] = ""

engine = create_engine("sqlite:///comics.db")
db = SQLDatabase(engine)

llm = ChatOpenAI(model="gpt-3.5-turbo")



agent_executor = create_sql_agent(llm, db=db, verbose=True)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form.get('message')

    try:
        result = agent_executor.invoke({"input": user_input})
        response_text = result['output']
    except Exception as e:
        response_text = f"Sorry, I couldn't process your request: {str(e)}"

    return jsonify({"response": response_text})

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=5000)
    print("Flask app has stopped running")
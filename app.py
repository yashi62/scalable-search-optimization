from flask import Flask, request, render_template, jsonify
from search_engine import SearchEngine

app = Flask(__name__)
search_engine = SearchEngine()

@app.route('/')
def home():
    return render_template('results.html', results=[], query="", page=1, total_pages=0)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    page = int(request.args.get('page', 1))

    if not query:
        return render_template('results.html', results=[], query="", page=1, total_pages=0)

    try:
        results, total_pages = search_engine.search(query, page)
        return render_template('results.html', results=results, query=query, page=page, total_pages=total_pages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

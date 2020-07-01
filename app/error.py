from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(error):
    """
        method to render 404 pages
    """
    return render_template('page_not_found.html'),404
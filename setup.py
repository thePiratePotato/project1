from flaskblog import create_app
# instead of import app, import create_app function

app =  create_app()
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=80,debug=True)

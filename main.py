from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route("/")
def hello_world():
    options =  {
        'page-size': 'A4',
        'margin-top': '0.2in',
        'margin-right': '0.2in',
        'margin-bottom': '0.2in',
        'margin-left': '0.4in',
        'encoding': "UTF-8",
        'custom-header': [('Accept-Encoding', 'gzip')]}
    dynamic_html = render_template('page2.html')
    print(dynamic_html)
    pdf = pdfkit.from_string(dynamic_html, False, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment;filename=test.pdf'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

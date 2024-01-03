from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route("/")
def hello_world():
    options = {
        'margin-top': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'encoding': "UTF-8",
        'page-size':'A4', 
        'disable-smart-shrinking': True,
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    dynamic_html = render_template('page1.html')
    pdf = pdfkit.from_string(dynamic_html, False, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment;filename=test.pdf'
    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

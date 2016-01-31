from flask import Flask,render_template,request,url_for
from scrapper import get_series
from scrapper import download
from downloader import download_func
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    if(request.method=='POST'):
        search=request.form['tv_series']
        dict=get_series(search)
        return render_template("search_results.html",dict=dict)
    return render_template("search.html")

@app.route("/download/<path:linkurl>")
def download_view(linkurl):
    complete_url=download(linkurl)
    download_func(complete_url)
    return "download complete"


if __name__ == "__main__":
    app.run(debug=True)

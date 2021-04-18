from flask import Flask, render_template, request
import pafy



app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')
	

@app.route('/convertidormp4', methods=['POST'])
def ConvertidorMp4():
    if request.method == 'POST':
        video = pafy.new(request.form['url'])
        title = video.title
        imagen = video.thumb
        best = video.getbest(preftype='mp4')
        filename = best.download()
        return render_template('convertidor.html', title=title, imagen=imagen)
         
          

 
       
if __name__ == '__main__':
    app.run(debug=True)
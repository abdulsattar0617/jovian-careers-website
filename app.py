from flask import Flask , render_template
import json 
   
  
with open("templates/config.json", 'r') as config:   
  params = json.load(config)["params"] 
  
  app = Flask(__name__) 
   
  @app.route("/")
  def hello_world(): 
    return render_template('home.html', params=params)   

 







if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) 
#Importation des bibliotheques necessaires
from flask import Flask, redirect, render_template, request , jsonify, session, url_for
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from flask_sqlalchemy import SQLAlchemy
from watchdog.events import FileSystemEventHandler
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import time
import os
import io
from PIL import Image
from random import randint
import tensorflow_addons as tfa
from keras.utils import load_img, img_to_array
import timeit

#Configuration de l'pplication

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password123@localhost/my_app_db'

# Cle pour JSON Web Token
app.config['JWT_SECRET_KEY'] = 'jkasfdqw345S@$$#@df'
app.config['SECRET_KEY'] = 'jkasfdqw345S@$$#@dfh'
#db = SQLAlchemy(app)
#db.init_app(app)

jwt = JWTManager(app)


    

#dic = {0 : 'NonDemented', 1 : 'VeryMildDemented' , 2 : 'MildDemented' , 3 : 'ModerateDemented' }

#Initialisation des classes (pour le dataset kaggle)
CLASSES = ['MildDemented','ModerateDemented','NonDemented','VeryMildDemented']
labels =dict(zip([0,1,2,3], CLASSES))

#Initialisation des classes (pour le dataset adni)
#CLASSES = ['AD','MCI','CN']
#labels =dict(zip([0,1,2], CLASSES))


#Load de modele deja entrainé (modele CNN)
model=tf.keras.models.load_model('alzheimer_vgg_cnn_model')

#variable pour ralentire la premiere prediction afin de loader les elements necessaire
frst = 1



#Fonction pour charger l'image choisie
def loading_images(img_path):
	k=load_img(img_path,target_size=(176,176))
	k=img_to_array(k)/255.0
	k=k.reshape(1,176,176,3)
	return k

#Fonction de prediction en utilisant le modele
def predict_label(img_path):
	"""i = load_img(img_path, target_size=(176,176))
	i = img_to_array(i)/255.0
	i = i.reshape(1, 176,176,3)"""
	i=loading_images(img_path)
	p = model.predict(i)
	data_array = np.array(p)
	max_value = np.max(data_array)
	predicted_label = labels[np.argmax(p[0])]
	
	return max_value,predicted_label
    

#Classe utilisateurs
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

#les utilisateurs pour etre connecte (remarque: a mettre dans une base de donnes)
users = {
    'belabied': '123',
    'hassina': '123' 
}
	

"""class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    
    def __repr__(self):
        return f"<User {self.username}>" 
    
with app.app_context():
    # db can now be used
    db.create_all()

new_user = User(username='john', password='password123')
db.session.add(new_user)
db.session.commit()"""

#Les routes pour charger les pages web

#route initiale de platforme
@app.route("/", methods=['GET', 'POST'])
def main():
	if 'token' not in session:
		return render_template("index.html",connect=True)
	return render_template("index.html",connect=False)


#route pour afficher la page des tests
@app.route("/test", methods=['GET', 'POST'])

def test():
    if 'token' not in session:
		#si n'st pas connecté afficher la page login
        return redirect(url_for('loginPageTest')) 
	#sinon affichage de page de test (prediction)
    return render_template('predict1.html')


#route pour afficher la page contenant la docummentation de l'api
@app.route("/docs", methods=['GET'])
def docs():
	return render_template("docs/api_doc.html")


#route de page about project
@app.route("/about")
def about_page():
	return "Analyse d'images IRM avec les techniques de l'apprentissage profond dans le cadre de la détection de la maladie d'Alzheimer."

#route pour executer la prediction dans la page des tests
@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	global frst
	if request.method == 'POST':
		#requperation de l'image choisie
		img = request.files['my_image']
        
		#sauvgarde de l'image
		img_path = "static/" + img.filename	
		print(img_path)
		img.save(img_path)
        
		#ralentir 7 secondes dans la premiere prediction pour charger les elemnts necessaire
		if frst == 1 :
			time.sleep(7)
			frst=2

		#execution de fonction de prediction
		accuracy,p = predict_label(img_path)

		#calcule le temps de prediction
		time1 = timeit.timeit(lambda: predict_label(img_path), number=1)
		print('prediction time:',time1)
        
		
	#affichage de la page de prediction avec l image choisie et la prediction ainsi le pourcentage
	return render_template("predict1.html", prediction = p, img_path = img_path,acc=accuracy)



#route pour etre authentifier
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(users)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
		#verifier si l utilisateur existe
        if username not in users or users[username] != password:return render_template('loginTest.html',NotConnect=True)
        
        #creation de token 
        access_token = create_access_token(identity=username)
        
        #ajout de token a la session
        session['token'] = access_token
        
		#redirection vers page tests
        return redirect(url_for('test'))
	#sinon rediriger vers la page login
    return render_template('loginTest.html')


    
"""@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username, password=password).first() 
    if user:
        return redirect(url_for('test'))
    else:
        return 'Invalid login'"""


#route de page de login (a ete modifier et remplacer par la page loginTest)
@app.route('/login/page', methods=['GET', 'POST'])
def loginPage():
    return render_template('login.html')

#route de page de login (qu on utilise maintenant)
@app.route('/login/page/test', methods=['GET', 'POST'])
def loginPageTest():
    return render_template('loginTest.html')

#route de deconnexion
@app.route('/exit')
def shutdown():
    # Clear session
    session.clear()
    return redirect('/')

"""
@app.before_request
def check_token():
    if 'token' not in session:
        return render_template('login.html')"""
"""
@app.before_request
def shutdown_session(exception=None):
    session.clear()"""

#Les routes de restful api pour etre utilise dans les code par les devoloppeurs et integrer notre modele dans differantes applications medicales (en utilisant les requetes et reponses en format json)

#le endpoint de l api d authentification
@app.route('/api/v1/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    # Validate user credentials (e.g., compare hashed password)
    user = User(id=1, username='cerist_user', password='12345678')

    if data['username'] == user.username and data['password'] == user.password:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    

#le endpoint de l api de prediction en uploadant les images
@app.route("/api/v1/predict2",  methods = ['GET', 'POST'])
@jwt_required()
def get_api_output2():
	global frst
	if request.method == 'POST':
		img = request.files['my_image']
        
		img_path = "static/" + img.filename	
		print(img_path)
		img.save(img_path)
        
		if frst == 1 :
			time.sleep(7)
			frst=2
		#prediction et retourner le resultat en format json
		accuracy,p = predict_label(img_path)
	response = {'prediction': p,'with accuracy':float(accuracy)}
	return jsonify(response)

#le endpoint de l api de prediction en utilisant le chemin des images (dans le cas ou les images se trouve localement)
@app.route("/api/v1/predict", methods = ['POST'])
def get_api_output():
	global frst
	if 'image_path' not in request.json:
		return jsonify({'error':'Invalid request, Image path not found.'}),400
	img_path = request.json["image_path"]
	if frst == 1 :
		time.sleep(5)
		frst=2
	#prediction et retourner le resultat en format json	
	p = predict_label(img_path)
	response = {'prediction': p,}
	return jsonify(response)

#lancement de serveur pour executer l application web et api restful
if __name__ =='__main__':
	#app.debug = True
	app.run(host='127.0.0.1', port=8000,debug = True)

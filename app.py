from flask import Flask, request, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)

# creates a key for a new session (instead of putting render_template (url, user_data=user_data))
# 'cause it was getting the error loading the page "jinja2.exceptions.UndefinedError: 'user_data' is undefined"

app.secret_key = "my_secret_key"

# Defining the main route on the "/"


@app.route("/", methods=["GET"])

def index():

  print ("redirected to page sucessfuly")
  return render_template("dm4370scriptgenerator.html")

#######################################################################################################################

# Defining second route to renderize another or multiples templates 
# the onclick js function to trigger a template must have the URL: http://127.0.0.1:5000/vplstunnelingscript

@app.route("/vplstunneling", methods=["POST", "GET"])

def vplstunneling():

  print ("redirected to page sucessfuly")
  return render_template("vplstunneling.html")

# Defining third route to renderize another or multiples templates 
# the onclick js function to trigger a template must have the URL: http://127.0.0.1:5000/vplstunnelingscript

@app.route("/vplstunnelingscript", methods=["GET", "POST"])

def vplstunnelingscript():

  #to pass throught jinja2 exception error, declare user_data calling the session and on the template

  user_datavpls = session.get ('user_datavpls', {})
  print ("Success sending back the data from the server-side to client-side:", user_datavpls)
  return render_template("vplstunnelingscript.html", user_datavpls = user_datavpls), 200


# Defining fourth route to renderize another or multiples templates 
# the onclick js function to trigger a template must have the URL: http://127.0.0.1:5000/eddmetroscript

####################################################################################################################

@app.route("/eddmetroscript", methods=["GET", "POST"])

def edd_metroscript():

  #to pass throught jinja2 exception error, declare user_data calling the session and on the template

  user_data = session.get ('user_data', {})
  print ("Success sending back the data from the server-side to client-side:", user_data)
  return render_template("dm4370EDDmetroscript.html"), 200

# function to get the js json data and send to the terminal output

@app.route("/store-data", methods=["POST", "GET"])

def store_data():
    
    # take the http request and json formated data from the client-side

    data = request.get_json()

    # Initialize an empty dictionary to store individual variables

    user_data = {} 
    
    # the variables here will be used as tags on the 127.0.0.1:5000 forms page to generate the script 

    circuito_value = data.get("circuito")

    cliente_value = data.get("cliente")

    produto_value = data.get("produto")

    radio_valueVLAN = data.get("radioValueVLAN")

    radio_valueCPE = data.get("radioValueCPE")

    VLAN_value = data.get("VLAN")

    METRO_value = data.get("METRO")

    CPE_value = data.get("CPE")

    METROspeed_value = data.get("METROSPEED")

    CPEspeed_value = data.get("CPESPEED")

    # Assign values to individual variables in the dictionary

    user_data["Hostname Circuito"] = circuito_value #string

    user_data["Hostname Cliente"] = cliente_value #string

    user_data["produto (Serviços)"] = produto_value #checklist

    user_data["METROPossuiVLAN?"] = radio_valueVLAN #checkradio

    user_data["CPEPossuiVLAN?"] = radio_valueCPE #checkradio

    user_data["Porta VLAN"] = VLAN_value #float

    user_data["Porta METRO"] = METRO_value #float

    user_data["Porta CPE"] = CPE_value # float

    user_data["METRO Velocidade"] = METROspeed_value #checklist

    user_data["CPE Velocidade"] = CPEspeed_value #checklist

    # Check for missing user input (optional)

    if not all(user_data.values()):
      return jsonify({"message": "Some inputs are missing!"}), 400

    # Process and store the user data (e.g., print to console)

    print("Sucessfuly collected the JSON data on the client-side:")
    
    for key, value in user_data.items():
      print(f"{key}: {value}")

#calls session user_data that was creating at the start of the page 
#(session MUST be equal to variable user_data)

    session['user_data']=user_data

  # after collecting and process the data, redirects to function index () of @app.route ()
  # There will able to render the next html template with the data collect sent back from server 

    return redirect (url_for("index" )), 200


@app.route("/store-datavpls", methods=["POST", "GET"])

def store_datavpls():
    
    # take the http request and json formated data from the client-side

    datavpls = request.get_json()

    # Initialize an empty dictionary to store individual variables

    user_datavpls = {} 
    
    # the variables here will be used as tags on the 127.0.0.1:5000 forms page to generate the script 

    circuito_value = datavpls.get("circuitovpls")

    cliente_value = datavpls.get("clientevpls")

    VLAN_value = datavpls.get("VLANvpls")


    # Assign values to individual variables in the dictionary

    user_datavpls["Seguimento de Rede do tunelamento VPLS"] = circuito_value #string

    user_datavpls["VPN do tunelamento VPLS"] = cliente_value #string

    user_datavpls["VLAN do tunelamento VPLS"] = VLAN_value #float

  

    # Check for missing user input (optional)

    if not all(user_datavpls.values()):
      return jsonify({"message": "Some inputs are missing!"}), 400

    # Process and store the user data (e.g., print to console)

    print("Sucessfuly collected the JSON data on the client-side for VPLS TUNNELING:")
    
    for key, value in user_datavpls.items():
      print(f"{key}: {value}")

#calls session user_data that was creating at the start of the page 
#(session MUST be equal to variable user_data)

    session['user_datavpls']=user_datavpls

  # after collecting and process the data, redirects to function index () of @app.route ()
  # There will able to render the next html template with the data collect sent back from server 

    return redirect (url_for("index")), 200

# ... app.run will start the local web server

if __name__ == "__main__":
  app.run(debug=True, host= '127.0.0.1', port = '5000')

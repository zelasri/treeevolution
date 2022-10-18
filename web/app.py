"""
Flask application routes
"""
import os
import json
import random
from datetime import datetime
import uuid
import pickle
import numpy as np

from flask import Flask, render_template, flash, jsonify
from flask import redirect, url_for, request, session, make_response

# treevolution module imports
from treevolution.models.tree import Tree
from treevolution.world import World
from treevolution.models import trees
from treevolution.base.geometry import Point
from treevolution.context.weather import Season

from .utils import import_submodules, all_subclasses, load_class
import_submodules(trees)

# default simulation config template
# user storage could be improved by using MongoDB
# but add-on is no longer supported by Heroku
simu_config = {
    "seed": 42,
    "start": None,
    "end": None,
    "ntrees": 1,
    "ndays": 1,
    "classes": [],
    "valid": False,
    "running": False
}

# default world
W_WIDTH, W_HEIGHT = 100, 100 # static world size

# initialize the flask app
app = Flask("treevolution_app", static_folder='./web/static', template_folder='./web/templates')
app.secret_key = b'_9@y3LL"F4Q8z\n\xec]/'

@app.route('/')
def index():
    """
    Route which displays the home page 
    """
    return render_template("home.html")

@app.route('/check', methods=['POST'])
def check_user():
    """
    Route which checks the current uuid of user.
    Route initializes also the user data folder
    """

    json_data = request.get_json()

    if 'treevolution_uuid' in json_data:

        # get user uuid and store it into session
        user_uuid = json_data['treevolution_uuid']
        session['treevolution_uuid'] = user_uuid
        return make_response(jsonify({"message": "ok"}), 200)

    else:
        # generate new uuid
        user_uuid = str(uuid.uuid4())
        session['treevolution_uuid'] = user_uuid

        user_config = simu_config.copy()
        set_user_config(user_config)

        return make_response(jsonify({"message": "created", "uuid": user_uuid}), 200)


@app.route('/simulation')
def simulation():
    """
    Route which enables the simulation view.
    Also returns the user config in order to propose world simulation
    """

    # read user config path
    user_config = get_user_config(date_str=True)

    tree_choices = []
    for current_cl in all_subclasses(Tree):
        full_name = '.'.join([current_cl.__module__, current_cl.__name__])

        # currently selected only
        if full_name in user_config["classes"]:
            tree_choices.append((full_name, current_cl.__name__))

    return render_template("simulation.html", trees=sorted(tree_choices), config=user_config)

@app.route('/config')
def config():
    """
    Route in order to display the config form to user with its own config data 
    """

    # get current user config
    user_config = get_user_config(date_str=True)

    tree_choices = []
    for current_cl in all_subclasses(Tree):
        full_name = '.'.join([current_cl.__module__, current_cl.__name__])

        # tuple with: (module_name, class_name, currentyly selected)
        tree_choices.append((full_name, current_cl.__name__, full_name in user_config["classes"]))
    
    return render_template("config.html", trees=sorted(tree_choices), config=user_config)

@app.route('/update', methods=['POST'])
def update():
    """
    Route in order to update the user config using specific form
    """

    # get current user config
    user_config = get_user_config()
    
    user_config["seed"] = int(request.form['seed'])
    user_config["ntrees"] = int(request.form['treeNumber'])
    user_config["ndays"] = int(request.form['daysNumber'])

    # check start and end selected date
    start_date = request.form['startDate']
    end_date = request.form["endDate"]

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # enable to display date in specific format
    user_config["start"] = start_date
    user_config["end"] = end_date

    if start_date >= end_date:
        
        # restore default values
        user_config["valid"] = False
        user_config["start"] = None
        user_config["end"] = None

        set_user_config(user_config) # update config

        flash('Invalid start date and end date.', 'error')
        return redirect(url_for('config'))

    if "classes" not in request.form:
        user_config["valid"] = False

        set_user_config(user_config) # update config
        flash('You need to select at least one Tree class.', 'error')
        return redirect(url_for('config'))
    
    # update classes
    user_config["classes"] = request.form.getlist('classes')
    user_config["valid"] = True
    set_user_config(user_config) # update config
    remove_user_world() # need to remove current model file

    flash('Configuration has been updated. The simulation has been reset.', 'success')

    return redirect("/config")

@app.route('/init', methods=['POST'])
def init():
    """
    Route which initializes the world only if the user config is valid
    """

    user_config = get_user_config()

    if user_config['valid']:
        
        # create new world with seed and start date
        print("Initialization of the new world using current config")
        start_date = user_config['start']

        # set seed for current world simulation
        random.seed(user_config['seed'])
        
        current_world = World(start_date, W_WIDTH, W_HEIGHT)

        # add trees into the world
        for _ in range(user_config['ntrees']):

            # use of numpy in order to preserve the same random sequence
            # in order to compare with src/main_visu.py
            selected_class = np.random.choice(user_config['classes'])
            
            tree_class = load_class(selected_class)

            # random coordinate
            tree_coordinate = Point.random(W_WIDTH, W_HEIGHT)

            # new tree creation
            new_tree = tree_class(tree_coordinate, user_config['start'], current_world)

            # finally add the new tree
            current_world.add_tree(new_tree)

        # save the current world instance as pickle obj
        save_user_world(current_world)

    else:
        user_config['running'] = False
        set_user_config(user_config) # update current config

        return json.dumps({'error': 'Your current configuration is no longer valid.'}), 403

    # enable to keep track of running world if page change
    user_config['running'] = True

    output_data = json.dumps(prepare_output_world(current_world))
    set_user_config(user_config) # update current config

    return output_data

@app.route('/state', methods=['GET'])
def state():
    """
    Route which returns the current state of the simulation world if exists
    """

    # cannot use the store.. (need serializable classes)
    current_world = load_user_world()

    # get current state of world if exists
    if current_world is None:

        return make_response(jsonify({'error': 'Current world was not found.'}), 403)

    return make_response(jsonify(prepare_output_world(current_world)), 200)


@app.route('/step', methods=['POST'])
def step():
    """
    Route which simulates the simulation world by ndays (set inside user config)
    """

    # cannot use the store.. (need serializable classes)
    user_config = get_user_config()
    current_world = load_user_world() # load current user world
        
    # check if world exists
    if current_world is None:

        return make_response(jsonify({'error': 'Current world was not found.'}), 403)

    # check the current world date
    if current_world.date >= user_config['end']:
        return json.dumps(prepare_output_world(current_world))

    # simulate the current world to the next day
    for _ in range(user_config['ndays']):
        current_date, _, _, _ = current_world.step()

        # check end of simulation
        if current_date >= user_config['end']:
            break

    # save the current user world instance as pickle obj
    save_user_world(current_world)

    return make_response(jsonify(prepare_output_world(current_world)), 200)


# all utils functions
def prepare_output_world(world):
    """
    Function which prepares the expect output format of a world in order to display it in web application
    """

    user_config = get_user_config()
    current_date = world.date

    json_world = world.to_json()
    json_world['current_date'] = current_date.strftime('%Y-%m-%d')
    json_world['season'] = Season.to_str(Season.get(current_date))

    json_world['finished'] = current_date >= user_config['end']

    # compute the percent of progression
    total_days = (user_config['end'] - user_config['start']).days
    elapsed_days = (current_date - user_config['start']).days
    
    json_world['progression'] = (elapsed_days / float(total_days)) * 100

    return json_world

def remove_user_world():
    """
    Remove the saved world obj of user
    """

    user_uuid = session['treevolution_uuid']
    user_model_path = os.path.join(app.static_folder, 'tmp', user_uuid, 'model.obj')

    if os.path.exists(user_model_path):
        os.remove(user_model_path)

def load_user_world():
    """
    Load and return the saved world obj of user
    """

    user_uuid = session['treevolution_uuid']
    user_model_path = os.path.join(app.static_folder, 'tmp', user_uuid, 'model.obj')

    # check model path exists
    if not os.path.exists(user_model_path):
        return None

    # load and return it
    with open(user_model_path, 'rb') as file_buffer:
        return pickle.load(file_buffer)


def save_user_world(world):
    """
    Save the user world as obj file
    """

    user_uuid = session['treevolution_uuid']
    user_model_path = os.path.join(app.static_folder, 'tmp', user_uuid, 'model.obj')

    # backup the current world
    with open(user_model_path, 'wb') as file_buffer:
        pickle.dump(world, file_buffer)


def get_user_config(date_str=False):
    """
    Load the saved current user config
    """

    # read user config path
    user_uuid = session['treevolution_uuid']
    user_config_path = os.path.join(app.static_folder, 'tmp', user_uuid, 'config.json')

    # if no folder exists then return default config
    if not os.path.exists(user_config_path):
        return simu_config.copy()

    file_buffer = open(user_config_path, 'r', encoding="utf-8")
    user_config = json.load(file_buffer)

    # update date as datetime if required
    if user_config["start"] is not None and not date_str:
        user_config["start"] = datetime.strptime(user_config["start"], '%Y-%m-%d')
    
    if user_config["end"] is not None and not date_str:
        user_config["end"] = datetime.strptime(user_config["end"], '%Y-%m-%d')

    return user_config


def set_user_config(user_config):
    """
    Update the current user config into specific file using its uuid
    """

    # save user config
    # prepare date format
    if user_config["start"] is not None:
        user_config["start"] = user_config["start"].strftime('%Y-%m-%d')
    
    if user_config["end"] is not None:
        user_config["end"] = user_config["end"].strftime('%Y-%m-%d')

    # create folder with default config
    user_uuid = session['treevolution_uuid']
    user_path = os.path.join(app.static_folder, 'tmp', user_uuid)

    if not os.path.exists(user_path):
        os.makedirs(user_path)

    filepath = os.path.join(user_path, 'config.json')
    with open(filepath, 'w', encoding="utf-8") as file_buffer:
        json.dump(user_config, file_buffer, indent=4)

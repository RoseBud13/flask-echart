from flask import Flask
from flask import render_template

from api import getData
import json
from datetime import datetime
import pytz


app = Flask(__name__)


@app.route('/')
def render():
    '''Parse raw json data with needed information and render to HTML page

    Methods: using for loop to extract the needed content and format a new list

    Return: return html file with the arguments in the list
    '''
    api_data = getData()
    # api_init_json =json.dumps(api_data)
    api_json = json.loads(api_data)
    print(type(api_json))

    CST = pytz.timezone('Asia/Shanghai')
    local_time = datetime.now(CST)
    current_time = local_time.strftime('%Y-%m-%d %H:%M:%S %Z %z')
    print(current_time)

    name = []
    total = []
    in_use = []

    for key, value in api_json.items():
        print(key, value)
        item_name = key
        item_detailed = json.loads(api_json[key])
        item_total = item_detailed['Count']
        item_in_use = item_detailed['InUse']
        name.append(item_name)
        total.append(item_total)
        in_use.append(item_in_use)
    
    item_list = [{"name":n,"total":t,"inuse":i} for n, t, i in zip(name, total, in_use)] 
    print(item_list)
    print(type(item_list))
    # item_string = json.dumps(item_list)
    # print(item_string)
    # print(type(item_string))
    # sub_string = item_string.replace("[", "{\"data\":[")
    # final_string = sub_string.replace("]", "]}")
    # print(final_string)
    # print(type(final_string))
    # final_dict = json.loads(final_string)
    # print(final_dict)
    # print(type(final_dict))

    return render_template('index.html', data=item_list, current_time=current_time)


@app.route('/chart')
def render_chart():
    

if __name__ == '__main__':
    app.run()

from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "Flask Filler"
net_id = "team"

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = query
		ingredients = query.split(',')
		data = []
		for ing in ingredients:
			data.append(ing)


	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)




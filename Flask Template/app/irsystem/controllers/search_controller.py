from . import *  
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "Flask Filler"
net_id = ""


ingredients = ["151 proof rum", "190 Proof Everclear","7-Up","Absinthe","Absolut Peppar","Acerola","Advocaat","Aftershock","Ale","Aliz\u00e9",
"Allspice","Almond","Almond flavoring","Almond syrup","Amaretto","Amarula Cream","Amer Picon","Angelica root","Angostura bitters",
"Anise","Anisette","Aperol","Apfelkorn","Apple","Apple brandy","Apple cider","Apple juice","Apple schnapps","Apple-cranberry juice",
"Apricot","Apricot brandy","Apricot liqueur","Apricot nectar","Aquavit","Asafoetida","Avocado","A\u00f1ejo rum","Bailey's irish cream",
"Banana","Banana liqueur","Banana rum","Banana syrup","Batida de Coco","Battery","Beef bouillon","Beer","Berries","Bitter lemon",
"Bitters","Black Sambuca","Black pepper","Black rum","Black vodka","Blackberries","Blackberry brandy","Blackberry schnapps","Blackcurrant cordial",
"Blackcurrant schnapps","Blackcurrant squash","Blackcurrant vodka","Blended whiskey","Bloody mary mix","Blue Curacao",
"Blueberries","Blueberry schnapps","Bourbon",
"Brandy",
"Bread",
"Brown sugar",
"Butter",
"Butterscotch schnapps",
"Cachaca",
"Cactus Juice liqueur",
"Campari",
"Canadian whisky",
"Candy",
"Cantaloupe",
"Cappuccino",
"Caramel",
"Caramel coloring",
"Caramel liqueur",
"Carbonated soft drink",
"Carbonated water",
"Cardamom",
"Carrot",
"Cayenne pepper",
"Celery",
"Celery salt",
"Chambord raspberry liqueur",
"Champagne",
"Cherries",
"Cherry",
"Cherry Cola",
"Cherry Heering",
"Cherry brandy",
"Cherry juice",
"Cherry liqueur",
"Cherry syrup",
"Cherry vodka",
"Chocolate",
"Chocolate ice-cream",
"Chocolate liqueur",
"Chocolate milk",
"Chocolate mint liqueur",
"Chocolate syrup",
"Cider",
"Cinnamon",
"Cinnamon schnapps",
"Cinzano Bitters",
"Citrus rum",
"Citrus vodka",
"Clamato juice",
"Cloves",
"Club soda",
"Coca-Cola",
"Cocktail onion",
"Cocoa powder",
"Coconut",
"Coconut cream",
"Coconut liqueur",
"Coconut milk",
"Coconut rum",
"Coconut syrup",
"Coffee",
"Coffee brandy",
"Coffee liqueur",
"Coffeemate",
"Cognac",
"Cola",
"Collins mix",
"Condensed milk",
"Coriander",
"Corn syrup",
"Cornstarch",
"Corona",
"Cranberries",
"Cranberry juice",
"Cranberry liqueur",
"Cranberry vodka",
"Cream",
"Cream of coconut",
"Cream soda",
"Creme de Almond",
"Creme de Banane",
"Creme de Cacao",
"Creme de Cassis",
"Creme de Fraise",
"Creme de Fraise des Bois",
"Creme de Noyaux",
"Crown Royal",
"Crystal light",
"Cucumber",
"Cumin seed",
"Curacao",
"Cynar",
"Daiquiri mix",
"Dark Creme de Cacao",
"Dark rum",
"Dr. Pepper",
"Drambuie",
"Dry Vermouth",
"Dubonnet Blanc",
"Dubonnet Rouge",
"Egg",
"Egg white",
"Egg yolk",
"Eggnog",
"Erin Cream",
"Espresso",
"Everclear",
"Fanta",
"Fennel seeds",
"Fernet Branca",
"Firewater",
"Food coloring",
"Forbidden Fruit",
"Frangelico",
"Fresca",
"Fruit",
"Fruit cocktail",
"Fruit juice",
"Fruit punch",
"Fruit syrup",
"Galliano",
"Gatorade",
"Gelatin",
"Genever",
"George Dickel",
"Gin",
"Ginger",
"Ginger ale",
"Ginger beer",
"Glycerine",
"Godiva liqueur",
"Gold rum",
"Gold tequila",
"Goldschlager",
"Grain alcohol",
"Grand Marnier",
"Grape Pucker",
"Grape juice",
"Grape schnapps",
"Grape soda",
"Grapefruit",
"Grapefruit juice",
"Grapefruit schnapps",
"Grapefruit-lemon soda",
"Grapes",
"Grappa",
"Green Chartreuse",
"Green Creme de Menthe",
"Green Curacao",
"Grenadine",
"Guava juice",
"Guava syrup",
"Guinness stout",
"Half-and-half",
"Hawaiian Punch",
"Hazelnut liqueur",
"Heavy cream",
"Herbal liqueur",
"Honey",
"Honey liqueur",
"Hoopers Hooch",
"Horseradish",
"Hot Damn",
"Hot chocolate",
"Hot red pepper flakes",
"Hpnotiq",
"Ice",
"Ice 101",
"Ice-cream",
"Iced tea",
"Irish Mist",
"Irish cream",
"Irish whiskey",
"Jack Daniels",
"Jalapeno",
"Jello",
"Jim Beam",
"Johnnie Walker",
"Jolt Cola",
"Jose Cuervo",
"J\u00e4germeister",
"Kahlua",
"Key Largo schnapps",
"Kirschwasser",
"Kiwi",
"Kiwi liqueur",
"Kool-Aid",
"Kummel",
"Lager",
"Lakka",
"Lemon",
"Lemon gin",
"Lemon juice",
"Lemon liqueur",
"Lemon peel",
"Lemon schnapps",
"Lemon soda",
"Lemon vodka",
"Lemon-lime mix",
"Lemon-lime sherbet",
"Lemon-lime soda",
"Lemonade",
"Licor 43",
"Light cream",
"Light rum",
"Lillet",
"Lime",
"Lime juice",
"Lime juice cordial",
"Lime liqueur",
"Lime peel",
"Lime vodka",
"Limeade",
"Limoncello",
"Lingonberry jam",
"Mad Dog 20/20",
"Madeira",
"Malibu rum",
"Malt liquor",
"Mandarin",
"Mandarine Napoleon",
"Mango",
"Mango juice",
"Mango liqueur",
"Mango syrup",
"Maple syrup",
"Maraschino cherry",
"Maraschino cherry juice",
"Maraschino liqueur",
"Margarita mix",
"Marjoram leaves",
"Marshmallows",
"Maui",
"Mello Yello",
"Melon liqueur",
"Melon vodka",
"Metaxa",
"Mezcal",
"Midori melon liqueur",
"Milk",
"Mint",
"Mint syrup",
"Molasses",
"Monin bitter",
"Mountain Dew",
"Nutmeg",
"Nuts",
"Olive",
"Olive juice",
"Orange",
"Orange Curacao",
"Orange Vermouth",
"Orange bitters",
"Orange juice",
"Orange liqueur",
"Orange peel",
"Orange rum",
"Orange soda",
"Orange spiral",
"Orange vodka",
"Orange-flower water",
"Oreo cookie",
"Orgeat syrup",
"Ouzo",
"Papaya",
"Papaya juice",
"Parfait d'Amour",
"Passion fruit juice",
"Passion fruit syrup",
"Passoa",
"Peach",
"Peach Vodka",
"Peach brandy",
"Peach juice",
"Peach liqueur",
"Peach nectar",
"Peach schnapps",
"Peachtree schnapps",
"Peanut liqueur",
"Pear",
"Pear brandy",
"Pear juice",
"Pear liqueur",
"Pear soft drink",
"Pepper sauce",
"Peppermint extract",
"Peppermint schnapps",
"Pepsi Cola",
"Pernod",
"Peychaud bitters",
"Pickled pepper",
"Pimm's No. 1",
"Pina colada mix",
"Pineapple",
"Pineapple juice",
"Pineapple rum",
"Pineapple soda",
"Pineapple vodka",
"Pineapple-coconut juice",
"Pineapple-orange juice",
"Pineapple-orange-banana juice",
"Pineau des Charentes",
"Pink lemonade",
"Pisang Ambon",
"Pisco",
"Pistachio liqueur",
"Pi\u00f1a Colada",
"Plums",
"Port",
"Powdered sugar",
"Prune juice",
"Pumpkin",
"Purple passion",
"Raisins",
"Raspberries",
"Raspberry cordial",
"Raspberry jam",
"Raspberry juice",
"Raspberry liqueur",
"Raspberry schnapps",
"Raspberry syrup",
"Raspberry vodka",
"Razzmatazz",
"Red Bull",
"Red wine",
"RedRum",
"Rhubarb",
"Ricard",
"Rock and rye",
"Root beer",
"Root beer schnapps",
"Rose's sweetened lime juice",
"Rosewater",
"Rum",
"Rum cream liqueur",
"Rumple Minze",
"Rye whiskey",
"Safari",
"Sake",
"Salt",
"Sambuca",
"Sarsaparilla",
"Saurer apfel",
"Schnapps",
"Schweppes Lemon",
"Schweppes Russchian",
"Scotch",
"Seagram 7",
"Sherbet",
"Sherry",
"Shochu",
"Sirup of roses",
"Sloe gin",
"Snapple",
"Soda water",
"Sour Apple Pucker",
"Sour apple liqueur",
"Sour mix",
"Southern Comfort",
"Soy milk",
"Soy sauce",
"Sparkling white wine",
"Spiced rum",
"Sprite",
"Squirt",
"St. Hallvard",
"Stout",
"Strawberries",
"Strawberry juice",
"Strawberry liqueur",
"Strawberry schnapps",
"Strawberry syrup",
"Strawberry vodka",
"Strega",
"Sugar",
"Sugar syrup",
"Sunny delight",
"Surge",
"Swedish Punsch",
"Sweet Tea",
"Sweet Vermouth",
"Sweet and sour",
"Swiss Mocha Cream liqueur",
"Tabasco sauce",
"Taboo",
"Tang",
"Tawny port",
"Tea",
"Tennessee whiskey",
"Tequila",
"Tequila Rose",
"Thunderbird",
"Tia maria",
"Tomato juice",
"Tonic water",
"Triple sec",
"Tropical fruit schnapps",
"Tuaca",
"V8 juice",
"Vanilla",
"Vanilla extract",
"Vanilla ice-cream",
"Vanilla liqueur",
"Vanilla schnapps",
"Vanilla syrup",
"Vanilla vodka",
"Vermouth",
"Vinegar",
"Vodka",
"Water",
"Watermelon",
"Watermelon liqueur",
"Watermelon schnapps",
"Whipped cream",
"Whipping cream",
"Whiskey",
"Whisky",
"White Creme de Menthe",
"White chocolate liqueur",
"White cranberry juice",
"White grape juice",
"White port",
"White rum",
"White wine",
"Wild Spirit liqueur",
"Wild Turkey",
"Wildberry schnapps",
"Wine",
"Worcestershire sauce",
"Wormwood",
"Yeast",
"Yellow Chartreuse",
"Yoghurt",
"Yukon Jack",
"Zima"]


ingredients = [item.lower() for item in ingredients]
#print(ingredients)

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = query
		ings = query.split(',')
		ings = [item.lstrip(' ') for item in ings]
		data = []
		for ing in ings:
			if ing in ingredients:
				print(ing + "is legit")
				data.append(ing)



	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)




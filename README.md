<h1>2018 NBA Scores REST API</h1>
	<h3>By Daniel Lee</h3>
	<h3>January 4, 2019</h3>
	<h2>Description</h2>
	<p>This is a simple REST API that receives GET requests from the client and retrieves 2018 National Basketball Association (NBA) scores.</p> 
	<h2>How to Use the API</h2>
	<h3>Possible Routes</h3>
	<ul>
		<li>/team/&lt;string:team_name&gt;
			<ul>
				<li>e.g. <a href='https://nba-scores-api.herokuapp.com/team/lakers'>/team/lakers</a>
			</ul>
		<li>/city/&lt;string:city_name&gt;
			<ul>
				<li>e.g. <a href='https://nba-scores-api.herokuapp.com/city/los_angeles'>/team/los_angeles</a>
			</ul>
		<li>/date/&lt;string:date&gt;
			<ul>
				<li>e.g. <a href='https://nba-scores-api.herokuapp.com/date/20181016'>/date/20181016</a>
			</ul>
			<li><a href='https://nba-scores-api.herokuapp.com/team_list'>/team_list</a>
			<ul>
				<li>This gives a list of all the team names
			</ul>
		<li><a href='https://nba-scores-api.herokuapp.com/city_list'>/city_list</a>
			<ul>
				<li>This gives a list of all the city names
			</ul>
	</ul>
	<h3><ul><li>/team/&lt;string:team_name&gt;</ul></h3>  
	<p style="margin-left: 40px">Possible values for team_name:</p>
	<ul style="margin-left: 40px">
		<li>warriors
		<li>suns
		<li>clippers
		<li>kings
		<li>spurs
		<li>rockets
		<li>raptors
		<li>knicks
		<li>magic
		<li>pacers
		<li>pistons
		<li>hornets
		<li>celtics
		<li>trail blazers
		<li>jazz
		<li>bucks
		<li>pelicans
		<li>timberwolves
		<li>grizzlies
		<li>nets
		<li>wizards
		<li>76ers
		<li>lakers
		<li>nuggets
		<li>thunder
		<li>cavaliers
		<li>mavericks
		<li>bulls
		<li>heat
		<li>hawks
	</ul>
	<p style="margin-left: 40px">Any other values for team_name will be considered invalid.</p>
	<h3>
		<ul>
			<li>/city/&lt;string:city_name&gt;
		</ul>
	</h3>  
	<p style="margin-left: 40px">Possible values for city_name:</p>
	<ul style="margin-left: 40px">
		<li>golden_state
		<li>phoenix
		<li>la
		<li>sacramento
		<li>san_antonio
		<li>houston
		<li>toronto
		<li>new_york
		<li>orlando
		<li>indiana
		<li>detroit
		<li>charlotte
		<li>boston
		<li>portland
		<li>utah
		<li>milwaukee
		<li>new_orleans
		<li>minnesota
		<li>memphis
		<li>brooklyn
		<li>washington
		<li>philadelphia
		<li>los_angeles
		<li>denver
		<li>oklahoma_city
		<li>cleveland
		<li>dallas
		<li>chicago
		<li>miami
		<li>atlanta
	</ul>
	<p style="margin-left: 40px">Any other values for team_name will be considered invalid.</p>
	<h3><ul><li>/date/&lt;string:date&gt;</ul></h3>
	<ul style="margin-left: 40px">
		<li>date needs to be in YYYYMMDD format
		<li>date begins on 20181016 as this is the first game of the 2018 NBA season
	</ul>
	<h2>Data Scraping Implementation</h2>
	<ul>
		<li>The data is obtained through scraping the <a href="http://www.espn.com">espn.com</a> website using the following:
			<ul>
				<li>Python (v. 3.6.7)
				<li>Scrapy (v. 1.5.1)
				<li>Splash (v. 0.7.2)
			</ul>
		<li>The data is stored in a MongoDB database. 
		<li>The web scraping app is deployed on Heroku. 
		<li>You can find the code <a href="https://github.com/danielhanbitlee/scrape_nba_scores">here</a>.
	</ul>
	<h2>REST API Implementation</h2>
	<ul>
		<li>The REST API is implemented using the following:
		<ul>
			<li>Python (v. 3.6.7)
			<li>Flask (v. 1.0.2)
		</ul>
		<li>This API is connected to a MongoDB database to access the data
		<li>The API is deployed on Heroku.
		<li>You can find the code <a href="https://github.com/danielhanbitlee/nba_scores_api_flask_pymongo">here.</a>
		<li>There's also an /auth route and a /register route for authentication and logging in. This requires Postman to use. For simplicity's sake, I removed the authentication requirements for the routes /team, /city, /date, /team_list, and /city_list.
	</ul>

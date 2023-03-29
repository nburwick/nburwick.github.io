# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt

# Import sqlalchemy modules.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text, inspect

#################################################
# Database Setup
#################################################
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Create Inspector for Exploration
inspector = inspect(engine)

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################

# Instanciate Flask App
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define Home Page
@app.route("/")
def home():
    return (
    f"<h2>Welcome to the Hawaii Climate App</h2>"
    f"<pre>Available routes are:"
    f"<pre><ul><li>Precipitation - /api/v1.0/precipitation</li></ul>"
    f"<pre>         Returns a json containing a year (12 months) data from last data point's date in the database. (2016-08-23 to 2017-08-23)<br>"
    f"<ul><li>Stations - /api/v1.0/stations</li></ul>"
    f"<pre>         Returns a json of 'station_id', 'station_name', 'lat', and 'lng' <br>"
    f"<ul><li>Temperature Observations - /api/v1.0/tobs</li></ul>"
    f"<pre>         Returns a json temperature observations from the 'Most Active Station' in the database.<br>"
    f"<ul><li>Calculated Temperatures (Single Date) - /api/v1.0/start</li></ul>"
    f"<pre>         Returns the minimum, maximum, and average temperatures from the start date given (YYYY-MM-DD) to the latest date included in the database."
    f"<ul><li>Calculated Temperatures (Dual Dates) - /api/v1.0/start/end</li></ul>"
    f"<pre>         Returns the minimum, maximum, and average temperatures from the start date given (YYYY-MM-DD) to the latest date given (YYYY-MM-DD)."
    f"<br><br><b>Note: replace start and end with dates in YYYY-MM-DD format.")

#################################################

# Define API JSON Response - precipitation
@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Find the most recent date in the data set.
    recent_date = session.query(func.max(measurement.date))[0][0]

    # Calculate the date one year from the last date in data set.
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    query_date = dt.date(recent_date.year - 1, recent_date.month, recent_date.day)

    # Design a query to retrieve the last 12 months of precipitation data and plot the results.
    query = f"""
                SELECT date, prcp
                FROM measurement
                WHERE date >= '{str(query_date)}' AND prcp NOT NULL
                GROUP BY station, date
                ORDER BY date
                """
    # Execute Query in sqlite db.
    results = session.execute(text(query)).all()

    # Create a list of dictionaries to hold rows of data
    prcp_list = [{'date': date, 'prcp' : prcp} for date, prcp in results]
    
    # Close Session
    session.close()
    
    # Return API Response Data
    return jsonify(prcp_list)

#################################################
   
# Define API JSON Response - station
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Design Query for Reponse Results - Station ID, Station Name, Lat, Lng
    select = [station.station, station.name, station.latitude, station.longitude]
    results = session.query(*select).all()
    
    # Create list of dictionaries to hold rows of data
    stations_list = [{'station_id' : id,
                      'station_name' : name,
                      'lat' : lat, 
                      'lng' : lng} for id, name, lat, lng in results]
    
    # Close Session
    session.close()
    
    # Return API Response Data
    return jsonify(stations_list)

#################################################

# Define API JSON Response - Temperature Observations for Most Active Station
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Design Query to get Most Active Station
    station = session.execute("""
            SELECT station, COUNT(station) AS Count
              FROM measurement
             GROUP BY station
             ORDER BY Count DESC
             LIMIT 1
          """).first()[0]

    # Find the most recent date in the data set.
    recent_date = session.query(func.max(measurement.date))[0][0]

    # Calculate the date one year from the last date in data set.
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    query_date = dt.date(recent_date.year - 1, recent_date.month, recent_date.day)
    
    # Design Query for Response Data
    query = f"""
             SELECT date, tobs, station
               FROM measurement
              WHERE date >= '{str(query_date)}' and station = '{station}'
              ORDER BY date   
             """
    # Execute Query
    results = session.execute(text(query)).all()
    
    # Create list of dictionaries to hold rows of data
    tobs_list = [{'date': date, 'temp_observation': tobs, 'station_id' : station } for date, tobs, station in results]
    
    # Close Session
    session.close()
        
    # Return API Response Data
    return jsonify(tobs_list)

#################################################
    
# Define Single Date Calculated Temperature List
@app.route("/api/v1.0/<start>")
def single_date(start):
    # Get Start Date
    start_date = str(start)
    
    try:
        check_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    except:
        return jsonify({'error': "An incorrect date format was entered. Please use a YYYY-MM-DD and try again"})
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Design Query
    query = f"""
                SELECT date, MIN(tobs), MAX(tobs), ROUND(AVG(tobs), 1)
                FROM measurement
                WHERE date >= '{start_date}'
                GROUP BY date
                ORDER BY date
             """
    # Execute Query
    results = session.execute(text(query)).all()
    
    # Create list of dictionaries to hold rows of data
    results_list = [{'date': date, 'TMIN' : min, 'TMAX': max, 'TAVG' : avg} for date, min, max, avg in results]

    # Close Session
    session.close()
    
    # Return API Response Data
    return jsonify(results_list)

#################################################    

# Define Dual Date Calculated Temperature List
@app.route("/api/v1.0/<start>/<end>")
def dual_date(start, end):
    # Get Start and End Date
    start_date = str(start)
    end_date = str(end)
    date_range = [start_date, end_date]
    
    try:
        for date in date_range:
            check_date = dt.datetime.strptime(date, '%Y-%m-%d')
    except:
        return jsonify({'error': "An incorrect date format was entered. Please use a YYYY-MM-DD and try again"})
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Design Query
    query = f"""
                SELECT date, MIN(tobs), MAX(tobs), ROUND(AVG(tobs), 1)
                FROM measurement
                WHERE date BETWEEN '{start_date}' AND '{end_date}'
                GROUP BY date
                ORDER BY date
             """
    # Execute Query
    results = session.execute(text(query)).all()
    
    # Create list of dictionaries to hold rows of data
    results_list = [{'date': date, 'TMIN' : min, 'TMAX': max, 'TAVG' : avg} for date, min, max, avg in results]

    # Close Session
    session.close()
    
    # Return API Response Data
    return jsonify(results_list)

#################################################

# Initiate App
if __name__ == "__main__":
    app.run(debug=True)

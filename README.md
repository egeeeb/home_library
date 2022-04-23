# Home Library App

- This pet project is designed to hold records of home libraries
- It also scrapes [goodreads.com](https://www.goodreads.com) to get ratings
- Finally it can produce following visualizations (see [Example Visualisations](#example-visualisations))
 

### Commands
* -setup-db host port user password db_name
* -import filepath
* -list
* -exit
* -draw-status-chart
* -draw-publisher-chart top
* -update-goodreads-ratings
* -draw-read-histogram
* -draw-to-read-histogram


### Setup
- Execute [schema.sql](schema.sql) to initialize tables.
- Run `python home_library.py`
- Import your csv using command `-import filepath`, see example [library_data.csv](library_data.csv)
- To populate goodreads ratings use command ``-update-goodreads-ratings``

### Example Visualisations
- Publisher distribution bar chart:
- <img width="512" src="imgs\publisher_chart.png" alt="publisher chart"/>
- Status pie chart:
- <img width="512" src="imgs\read_status_pie_chart.png" alt="status chart"/>
- Rating histogram of read books:
- <img width="512" src="imgs\read_histogram.png" alt="read histogram"/>
- Rating histogram of to-read books:
- <img width="512" src="imgs\to_read_histogram.png" alt="to-read histogram"/>
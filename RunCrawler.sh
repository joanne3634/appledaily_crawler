# cd /home/joanne3634/appledaily_crawler/
cd /Applications/MAMP/htdocs/appledaily_crawler/

# cd /Applications/MAMP/htdocs/appledaily/start_charity_dev/
# /usr/bin/python /home/joanne3634/appledaily_crawler/AppleDaily.py -o /home/joanne3634/appledaily_crawler/appledaily --interval=86400
# /Applications/MAMP/htdocs/appledaily_crawler/

# python AppleDaily.py -o appledaily --interval=86400
# php purifyHTML.php
python Titles.py
python GetArticles.py

# scp -r db_* /home/joanne3634/public_html/start_charity_dev/
scp -r db_* /Applications/MAMP/htdocs/appledaily/start_charity_dev/

# find /home/joanne3634/appledaily_crawler/db_articles/ -name '*.htm' -exec cp {} db_articles/ \;
# find /Applications/MAMP/htdocs/appledaily_crawler/db_articles/ -name '*.htm' -exec cp {} db_articles/ \;

# find /home/joanne3634/appledaily_crawler/db_lists/ -name '*.json' -exec cp {} db_lists/ \;
# find /Applications/MAMP/htdocs/appledaily_crawler/db_articles/ -name '*.json' -exec cp {} db_articles/ \;

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# print(os.getenv("KEY"))

client = OpenAI(
    api_key=os.getenv("KEY")
)

def get_car_details(user_message):

    query = [
        {"role": "system", "content": "Extract some attributes about the car and determine if it has 'Performance Battery Plus' and 'Adaptive Cruise Control'. Return the result as an object with keys Name, Dealer, HasPerfBattery, HasACC"},
        {"role": "user", "content": user_message }   
    ]

    # Create the chat completion request
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=query
    )

    # Extract the response
    result = response.choices[0].message.content
    # print(result)

    json_result = json.loads(result)

    return json_result


user_message = """
Title: Used 2016 BMW X1 xDrive28i 
Price: $17,990 
Features: <ul class="list columns columns-1 columns-sm-1 columns-md-2 columns-lg-2 padding-0" data-cmp="listColumns"><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div aria-label="MILEAGE" role="img" style="background:url(https://www.autotrader.com/content/static/img/icon/specifications/all_icons_orange.svg) -191px -74px;height:25px;width:30px"></div></div><div class="display-flex col-xs-10 margin-bottom-0">58,050 miles</div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div aria-label="ENGINE_DESCRIPTION" role="img" style="background:url(https://www.autotrader.com/content/static/img/icon/specifications/all_icons_orange.svg) -2px -74px;height:25px;width:30px"></div></div><div class="display-flex col-xs-10 margin-bottom-0">2.0L 4-Cylinder Turbo Gas Engine</div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div aria-label="MPG" role="img" style="background:url(https://www.autotrader.com/content/static/img/icon/specifications/all_icons_orange.svg) -126px -6px;height:25px;width:30px"></div></div><div class="display-flex col-xs-10 margin-bottom-0">22 City / 31 Highway<span><span class="text-blue margin-left-1"><span aria-label="more info" class="glyphicon glyphicon-info" role="button" tabindex="0"></span> </span></span></div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div class="color-swatch margin-bottom-1 margin-left-1" data-cmp="colorSwatch"><div class="swatch contrast" style="background-color:white"> </div></div></div><div class="display-flex col-xs-10 margin-bottom-0">Alpine White Exterior</div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div class="color-swatch margin-bottom-1 margin-left-1" data-cmp="colorSwatch"><div class="swatch" style="background-color:black"> </div></div></div><div class="display-flex col-xs-10 margin-bottom-0">Black Interior</div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div aria-label="TRANSMISSION" role="img" style="background:url(https://www.autotrader.com/content/static/img/icon/specifications/all_icons_orange.svg) -65px -133px;height:25px;width:30px"></div></div><div class="display-flex col-xs-10 margin-bottom-0">8-Speed Automatic Transmission</div></div></li><li class="list-bordered list-condensed"><div class="row text-bold"><div class="col-xs-2"><div aria-label="DRIVE TYPE" role="img" style="background:url(https://www.autotrader.com/content/static/img/icon/specifications/all_icons_orange.svg) -66px -6px;height:25px;width:30px"></div></div><div class="display-flex col-xs-10 margin-bottom-0">All wheel drive</div></div></li></ul>
"""
result = get_car_details(user_message)
print(result)

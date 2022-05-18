# API
#### This API is an API that converts json files created in Sketch2CAD into CAD files. 
#### Therefore, it is optimized for architecture and developed using the ezdxf library. 
([https://ezdxf.readthedocs.io/en/stable/](https://ezdxf.readthedocs.io/en/stable/)) 
#### You can create a json file according to the rules we set, or modify our code in any way you want.

<br><br>
## How to use
We will introduce two methods, one for using as an Android app and one for using only the API.
### 0. Before start
Plaease install exdxf on  your computer.
```
pip install exdxf
```
<br>


### 1. Use with android app
You can use this API most easily in your Android app by connecting it as a server.<br>
We highly recommend this method.<br>
<br>
Check your ip address by ipconfig command. <br>
If you want to use anywhere, you must to port forwarding. <br>
Anyway, put your ip address as ip address of exporter.java of android app. <br>
``` java
public class Exporter {
    JSONObject json;
    StackManager stackManager;
    String ipAddress = "172.30.1.40"; // your ip address
    Socket socket;
    int port = 8080;
```
Then, Execute the API's main.py file.<br>
Draw sketch on your android app and click export button.<br>
Then cad file is on your computer. (API's output folder)<br>
<br>
### 2. Only use API
If you don't use the Android app, just use the API, <br>
you need to understand our rules and create a json file.<br>
This method is very cumbersome.<br>
I recommend using it when you're automating another way.<br>
<br>
#### Here are the rules for generating our json file:<br>
1. In the json file, the architectural element should be included in a list with key value arctObj.
2. A nemoRoom means a rectangular room, and it should include the lower left coordinates, the upper right coordinates, and the wall thickness. It may also include a door object..
3. A door object has a coordinate value, a degree (the door opens in the upward direction at 0 degrees), a door type (determining the left-right direction), and characteristics (width and length of the door frame, the thickness of the door, and the thickness of the frame of the door frame).
4. A window has a coordinate value, a degree (to specify a window frame), a window type, and a characteristic (width and height of the door frame, width and height of the frame).
5. The column has lower-left coordinates and upper-right coordinates
<br><br>

### code example
``` python
jsonInterpreter = JsonInerpreter()
jsonInterpreter.loadJson(FILEPATH) # write your json's file path
dxfHandler = DxfHandler()
dxfHandler.drawJsonInter(jsonInterpreter)
dxfHandler.saveDxf(SAVEPATH, FILENAME) 
```

#### json example:
``` json
{
    "name": "test house",
    "date": "2021-11-26",
    "arctObj": [
        {
            "name": "living room",
            "type": "nemoRoom",
            "leftBot": [
                0,
                0
            ],
            "rightTop": [
                4000,
                4000
            ],
            "thickness": 200
        },
        {
            "type": "door",
            "cord": [
                -200,
                700
            ],
            "degree": 90,
            "doorType": 0,
            "attr": {
                "garo": 1000,
                "sero": 200,
                "doke": 40,
                "frame": 50
            }
        },
        {
            "type": "window",
            "cord": [
                1500,
                -200
            ],
            "degree": 0,
            "windowType": 0,
            "attr": {
                "garo": 1500,
                "sero": 200,
                "frame_garo": 50,
                "frame_sero": 50
            }
        },
        {
            "type" : "column",
            "leftBot":[2000, 2000],
            "rightTop":[2500, 2500]
        },
        {
            "name": "living room",
            "type": "nemoRoom",
            "leftBot": [
                4200,
                0
            ],
            "rightTop": [
                8000,
                3000
            ],
            "thickness": 200
        }
    ]
}
```

#### Result:
![image](https://user-images.githubusercontent.com/44011517/168933227-3556aed7-51f4-4e48-9f5b-c6517ef0063b.png)
<br><br>




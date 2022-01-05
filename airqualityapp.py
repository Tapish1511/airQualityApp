import tkinter as tk
import json
import requests

# https://api.waqi.info/feed/kota/?token=cafcf9e0f70624275161f10ec8401d7165ee60dc
# https://api.waqi.info/search/?token=cafcf9e0f70624275161f10ec8401d7165ee60dc&keyword=bangalore


def search():
    global app_frame
    app_frame.pack_forget()



    try:
        global result_status, background_color, lbl1, result_aqi_lbl, lbl2, result_ltlg_lbl, lbl3,result_status_lbl
        global result_lbl, input_entry

        city = str(input_entry.get())
        city.strip()

        api_request = requests.get(f"https://api.waqi.info/feed/{city}/?token=cafcf9e0f70624275161f10ec8401d7165ee60dc")
        api_result = json.loads(api_request.content)
        result_aqi = api_result["data"]['aqi']
        result_ltlg = api_result['data']["city"]['geo']
        result_status = ""
        background_color = ""
        foreground_color = "white"
        if result_aqi <= 50:
            result_status = "Good"
            background_color = "#009966"
        elif 50 < result_aqi <= 100:
            result_status = "Moderate"
            background_color = "#ffde33"
            foreground_color = "black"
        elif 100 < result_aqi <= 150:
            result_status = "Unhealthy of sensitive groups"
            background_color = "#ff9933"
            foreground_color = "black"
        elif 150 < result_aqi <= 200:
            result_status = "Unhealthy"
            background_color = "#cc0033"
        elif 200 < result_aqi <= 300:
            result_status = "Very unhealthy"
            background_color = "#660099"
        else:
            result_status = "Hazardous"
            background_color = "#7e0023"

        lbl1 = tk.Label(app_frame, text="Air Quality:", font=("calabari", 12), bg=background_color,
                        fg=foreground_color)
        result_aqi_lbl = tk.Label(app_frame, text=result_aqi, font=("calabari", 12), bg=background_color,
                                  fg=foreground_color)

        lbl2 = tk.Label(app_frame, text="latitude and longitude:", font=("calabari", 8), bg=background_color,
                        fg=foreground_color)
        result_ltlg_lbl = tk.Label(app_frame, text=result_ltlg, font=("calabari", 10), bg=background_color,
                                   fg=foreground_color)

        lbl3 = tk.Label(app_frame, text="Status", font=("calabari", 12), bg=background_color, fg=foreground_color)
        result_status_lbl = tk.Label(app_frame, text=result_status, font=("calabari", 12), bg=background_color,
                                     fg=foreground_color)

        lbl1.grid(row=1, column=0, pady=10, padx=(50, 25))
        result_aqi_lbl.grid(row=1, column=1, pady=10, sticky=tk.E+tk.W)
        lbl2.grid(row=2, column=0, padx=(50, 25))
        result_ltlg_lbl.grid(row=2, column=1, sticky=tk.E+tk.W)
        lbl3.grid(row=3, column=0, pady=10, padx=(50, 25))
        result_status_lbl.grid(row=3, column=1, sticky=tk.E+tk.W)
        result_lbl.pack_forget()
        app_frame.config(bg=background_color)
        app_frame.pack()

    except Exception as e:
        try:
            result_lbl.pack_forget()
        except Exception:
            pass

        app_frame.pack_forget()
        result_lbl = tk.Label(root, text="something went wrong....")
        result_lbl.pack()


root = tk.Tk()
app_frame = tk.Frame(root)
input_frame = tk.Frame(root)

city_lbl = tk.Label(input_frame, text="Enter city name:", font=("calabari", 12)).grid(row=0, column=0, padx=(50, 25), pady=10)

input_entry = tk.Entry(input_frame, font=('calabari', 12))
input_entry.grid(row=0, column=1, padx=(25, 10), pady=10)

search_btn = tk.Button(input_frame, text="search", command=search)
search_btn.grid(row=0, column=2, padx=(0, 50))


input_frame.pack()
root.mainloop()

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime

plotly.tools.set_credentials_file(username='zahichemaly', api_key='ZlMftVpKi9qghFCYNcU1')


def create_chart(t1, t2, t3, t4, title, filename):
    L1 = t1[0]
    V1 = t1[1]
    L2 = t2[0]
    V2 = t2[1]
    L3 = t3[0]
    V3 = t3[1]
    L4 = t4[0]
    V4 = t4[1]
    fig = {
        "data": [
        {
            "values": V1,
            "labels": L1,
            "name": "Food Chart",
            "hoverinfo":"label+percent+name",
            "text":L1,
            "textfont":{"size": 12},
            "type": "pie",
            'domain': {'x': [0, .4],
                       'y': [0, .3]}
        },
        {
            "values": V2,
            "labels": L2,
            "name": "Time of occurence",
            "hoverinfo":"label+percent+name",
            "text":L2,
            "textfont":{"size": 12},
            "type": "pie",
            'domain': {'x': [.6, 1],
                       'y': [0, .3]}
        },
        {
            "values": V3,
            "labels": L3,
            "name": "Activities",
            "hoverinfo":"label+percent+name",
            "text":L3,
            "textfont":{"size": 12},
            "type": "pie",
            'domain': {'x': [0, .4],
                       'y': [.6, .9]}
        },
        {
            "values": V4,
            "labels": L4,
            "name": "Mood",
            "hoverinfo":"label+percent+name",
            "text":L4,
            "textfont":{"size": 12},
            "type": "pie",
            'domain': {'x': [.6, 1],
                       'y': [.6, .9]}
        }],
        "layout": {
            "title": title,
            "showlegend": False,
            "annotations": [
            {
                "x": 0.08,
                "y": 0.4,
                "text": "Your food consumption",
                "showarrow": False
            },
            {
                "x": 0.9,
                "y": 0.4,
                "text": "Time of occurence",
                "showarrow": False
            },
            {
                "x": 0.88,
                "y": 1.05,
                "text": "Your mood",
                "showarrow": False
            },
            {
                "x": 0.15,
                "y": 1.05,
                "text": "Your activities",
                "showarrow": False
            }
            ]
        }
    }
    url = py.plot(fig, filename = filename, auto_open = False) + ".jpeg"
    path = 'data/pics/' + filename + '.png'
    py.image.save_as(fig, filename = path)
    return url

def food_stats(crisis):
    food_dict = {}
    for c in crisis:
        for f in c.get_food():
            if food_dict.get(f) is None:
                food_dict[f] = 1
            else:
                val = food_dict.get(f) + 1
                food_dict[f] = val

    return calculate_stats(food_dict)

def mood_stats(api, crisis_list):
    mood_dict = {}
    for c in crisis_list:
        profiles = api.get_profiles(c.get_id())
        for p in profiles:
            mood = p.get_mood()
            if mood_dict.get(mood) is None:
                mood_dict[mood] = 1
            else:
                mood_dict[mood] = mood_dict.get(mood) + 1
    
    return calculate_stats(mood_dict)

def activ_stats(api, crisis_list):
    activ_dict = {}
    for c in crisis_list:
        profiles = api.get_profiles(c.get_id())
        for p in profiles:
            act = p.get_activity()
            if activ_dict.get(act) is None:
                activ_dict[act] = 1
            else:
                activ_dict[act] = activ_dict.get(act) + 1
    
    return calculate_stats(activ_dict)

def time_stats(crisis):
    time_dict = {}
    time_dict['day'] = 0
    time_dict['night'] = 0
    format_str = "%H:%M"
    for c in crisis:
        t = c.get_time()
        d = datetime.strptime(t, format_str)
        hrs = d.time().hour
        if hrs < 18:
            time_dict['day'] = time_dict.get('day') + 1
        else:
            time_dict['night'] = time_dict.get('night') + 1

    return calculate_stats(time_dict)

def calculate_stats(d):
    labels = []
    values = []
    s = sum(d.values())
    for k in d.keys():
        val = d.get(k)
        p = val/s
        labels.append(k)
        values.append(p)
    return (labels, values)

def draw_chart(api, crisis, title, filename):
    T1 = food_stats(crisis)
    T2 = time_stats(crisis)
    T3 = activ_stats(api, crisis)
    T4 = mood_stats(api, crisis)

    return create_chart(T1, T2, T3, T4, title, filename)

